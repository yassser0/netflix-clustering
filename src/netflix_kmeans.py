import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import time

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

start = time.time()

# Charger les données
df_full = pd.read_csv('dataset/netflix.csv')
df = df_full[['title', 'listed_in', 'rating', 'duration', 'release_year']].dropna()

# Nettoyage
df['duration'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['release_year'] = df['release_year'].astype(float)

# Encodage One-Hot des genres
genres_encoded = df['listed_in'].str.get_dummies(sep=', ')
df = pd.concat([df.drop('listed_in', axis=1), genres_encoded], axis=1)

# Encodage des ratings
df['rating'] = df['rating'].astype('category').cat.codes

# Normalisation (sans la colonne 'title')
X_scaled = StandardScaler().fit_transform(df.drop(columns=['title']))

# Méthode du coude
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertias, marker='o')
plt.title("Méthode du coude pour choisir K")
plt.xlabel("Nombre de clusters")
plt.ylabel("Inertie")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/elbow_method.png")

# Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualisation durée vs rating
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='duration', y='rating', hue='cluster', palette='Set2')
plt.title("Clustering des émissions Netflix")
plt.xlabel("Durée (minutes)")
plt.ylabel("Rating (encodé)")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/clusters.png")

# PCA 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='cluster', palette='Set1')
plt.title("Clustering PCA (2D)")
plt.tight_layout()
plt.savefig("output/pca_clusters.png")

# Barplot des clusters
plt.figure(figsize=(6, 4))
sns.countplot(x='cluster', data=df, palette='Set2')
plt.title("Nombre de shows par cluster")
plt.xlabel("Cluster")
plt.ylabel("Nombre de shows")
plt.tight_layout()
plt.savefig("output/cluster_counts.png")

# Analyse genres dominants
genre_columns = genres_encoded.columns
top_genres_per_cluster = df.groupby('cluster')[genre_columns].sum().idxmax(axis=1)

print("\n📚 Genre principal par cluster :")
for cluster_id, genre in top_genres_per_cluster.items():
    print(f" - Cluster {cluster_id} → {genre}")

# Moyennes numériques
print("\n📊 Moyenne des variables par cluster :")
print(df.groupby('cluster')[['duration', 'rating', 'release_year']].mean())

# Export CSV
df.to_csv("output/netflix_clustered.csv", index=False)

end = time.time()
print(f"\n✅ Clustering terminé en {end - start:.2f} secondes.")
print("📁 Résultats enregistrés dans le dossier 'output'")
