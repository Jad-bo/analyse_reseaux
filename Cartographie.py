import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#  Chargement des fichiers 
batiments = gpd.read_file("batiments.shp")
lignes = gpd.read_file("lignes.shp")
reseau = pd.read_csv("reseau_en_arbre.csv")

# Harmonisation des systèmes de coordonnées 
lignes = lignes.to_crs(batiments.crs)

# Visualisation simple 
fig, ax = plt.subplots(figsize=(10, 10))
lignes.plot(ax=ax, color='orange', linewidth=1, label="Lignes électriques")
batiments.plot(ax=ax, color='skyblue', markersize=10, label="Bâtiments")

plt.title("Carte du réseau électrique")
plt.legend()
plt.show()
