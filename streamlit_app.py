import streamlit as st
import pandas as pd
from PIL import Image

# Titre principal
st.title("🎬 Netflix Show Clustering Explorer")
st.markdown("Explore Netflix shows grouped by genres, ratings, and durations using **K-Means clustering**.")

# Charger les données
df = pd.read_csv("output/netflix_clustered.csv")

# Affichage des images de clustering
st.subheader("Visualisations des Clusters")

with st.expander("📌 PCA 2D Clustering"):
    st.image("output/pca_clusters.png")

with st.expander("🎯 Duration vs Rating"):
    st.image("output/clusters.png")

with st.expander("📊 Cluster Counts"):
    st.image("output/cluster_counts.png")

with st.expander("📈 Méthode du Coude (Elbow Method)"):
    st.image("output/elbow_method.png")

# 🔍 Recherche de titre
st.subheader("🔍 Rechercher un show Netflix")
search_title = st.text_input("Entrez un titre (exact)", "")
if search_title:
    result = df[df['title'].str.lower() == search_title.lower()]
    if not result.empty:
        st.success(f"✅ Trouvé dans le cluster {result.iloc[0]['cluster']}")
        st.dataframe(result)
    else:
        st.error("❌ Aucun show trouvé avec ce titre.")

# 📂 Explorer un cluster
st.subheader("📂 Explorer les shows par cluster")
cluster_selected = st.selectbox("Choisissez un cluster", sorted(df['cluster'].unique()))
st.dataframe(df[df['cluster'] == cluster_selected][['title', 'duration', 'rating', 'release_year']].head(20))
