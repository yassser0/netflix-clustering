# 🎬 Netflix Show Clustering (K-Means)

Ce projet applique l’algorithme de **K-Means Clustering** pour regrouper des émissions et films Netflix similaires en fonction de leur **genre**, **durée**, **classification (rating)**, et **année de sortie**.

## 📌 Objectif

- Regrouper les shows en **clusters** de contenu homogène
- Identifier les **genres dominants** et tendances de durée
- Visualiser les clusters à l’aide de **graphiques interactifs**
- Créer une interface web pour explorer les résultats

---

## 🧠 Technologies utilisées

- Python 3.10+
- Pandas, Scikit-learn, Matplotlib, Seaborn
- Streamlit (interface web)
- K-Means Clustering, PCA

---

## 📁 Structure du projet

![image](https://github.com/user-attachments/assets/3d9e9a10-dcc6-4b69-9127-a58dc1143f7a)


## 📊 Résultats visuels

- 📌 `clusters.png` – Clustering selon durée et rating
- 📌 `pca_clusters.png` – Vue 2D par PCA
- 📌 `cluster_counts.png` – Nombre d’émissions par cluster
- 📌 `elbow_method.png` – Sélection du meilleur `k

## 🧪 Fonctionnalités de l’interface Streamlit

- Rechercher un **titre d’émission**
- Explorer le contenu d’un **cluster**
- Visualiser les **graphiques** générés automatiquement

## 🚀 Lancer le projet

### 1. Cloner le repo et installer les dépendances

```bash
git clone https://github.com/yassser0/netflix-clustering.git
cd netflix-clustering
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate sur Linux/Mac
pip install -r requirements.txt


### 2. Lancer le traitement de clustering
python src/netflix_kmeans.py

### 3. Lancer l’interface Streamlit
streamlit run streamlit_app.py 

📌 Auteur 
Mohammed Yasser 
🎓 Étudiant Master Big Data & Data Science FSBM 
📧 rachihyasser@gmail.com
