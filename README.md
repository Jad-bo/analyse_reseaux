# ⚡ Planification du Raccordement Électrique des Bâtiments

## 👥 Groupe de travail

| Nom complet | Rôle dans le projet |
|--------------|--------------------|
| **MEHIYDDINE Abdelhakim** | Responsable de la modélisation orientée objet (`Infra`, `Batiment`) et de la conception de la métrique de difficulté |
| **ELBACHARI Oussama** | Responsable de l’analyse du réseau (`analyse_reseau.py`) et du traitement des données Excel |
| **BOUSFIHA Jad** | Responsable de la documentation technique, de la validation des résultats et de la coordination du plan de raccordement |

---

## 🏗️ Contexte du projet

Ce projet consiste à planifier le **raccordement électrique** des bâtiments d’une petite ville dont une partie du réseau a été endommagée à la suite d’intempéries.

L’objectif principal est de :

> **Rétablir le réseau électrique en priorisant les bâtiments les plus simples à raccorder**,  
tout en **minimisant les coûts** et **maximisant le nombre de bâtiments reconnectés**.

---

## 🚀 Objectif des premières étapes

Ces premières étapes visent à :
1. **Analyser les données du réseau** contenues dans le fichier `reseau_en_arbre.xlsx`.  
2. **Modéliser les entités principales** du problème : les *bâtiments* et les *infrastructures*.  
3. **Déterminer l’état initial de chaque bâtiment** (intact ou à réparer) selon les infrastructures qui le relient.

---

## 🧱 Étape 1 – Modélisation orientée objet

### 📁 `infra.py`
Ce fichier définit la classe **`Infra`**, représentant une **infrastructure électrique**.

#### 🔹 Rôle :
- Stocke les informations de base : `infra_id`, `longueur`, `infra_type`, `nb_houses`
- Calcule une **métrique de difficulté** :
  ```python
  difficulté = longueur / nombre_de_maisons
