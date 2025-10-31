import pandas as pd

# === 1. Lecture du fichier Excel ===
fichier = "./reseau_en_arbre.xlsx"
reseau = pd.read_excel(fichier)

print("=== Aperçu du fichier réseau ===")
print(reseau.head(), "\n")
print(f"Nombre total de lignes : {len(reseau)}")
print(f"Colonnes disponibles : {reseau.columns.tolist()}\n")

# === 2. Vérification de cohérence ===
if reseau.isna().sum().sum() > 0:
    print("⚠️  Attention : des valeurs manquantes ont été détectées !")
else:
    print("✅ Aucune valeur manquante détectée.\n")

# === 3. Analyse bâtiment par bâtiment ===
etat_batiments = []

# On parcourt chaque bâtiment unique
for id_batiment in reseau["id_batiment"].unique():
    sous_df = reseau[reseau["id_batiment"] == id_batiment]

    # On vérifie si au moins une infra est à remplacer
    if "a_remplacer" in sous_df["infra_type"].values:
        etat = "a_reparer"
    else:
        etat = "intact"

    # On calcule aussi quelques infos utiles
    nb_infra = len(sous_df)
    longueur_totale = sous_df["longueur"].sum()
    nb_maisons = sous_df["nb_maisons"].max()

    etat_batiments.append({
        "id_batiment": id_batiment,
        "etat": etat,
        "nb_infra": nb_infra,
        "longueur_totale": round(longueur_totale, 2),
        "nb_maisons": nb_maisons
    })

# === 4. Création du DataFrame final ===
etat_df = pd.DataFrame(etat_batiments)

# === 5. Affichage console clair ===
print("\n=== État des bâtiments ===")
print(etat_df.head(15))

# === 6. Quelques statistiques globales ===
nb_total = len(etat_df)
nb_reparer = (etat_df["etat"] == "a_reparer").sum()
nb_intact = (etat_df["etat"] == "intact").sum()

print("\n=== Statistiques globales ===")
print(f"Nombre total de bâtiments : {nb_total}")
print(f"Bâtiments à réparer       : {nb_reparer}")
print(f"Bâtiments intacts         : {nb_intact}")
print(f"Pourcentage à réparer     : {nb_reparer / nb_total * 100:.2f}%")

# === 7. Sauvegarde dans un CSV ===
etat_df.to_csv("etat_batiments_v2.csv", index=False)
print("\n✅ Fichier 'etat_batiments_v2.csv' enregistré avec succès !")
