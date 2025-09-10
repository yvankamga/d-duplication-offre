import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from spacy.lang.fr.stop_words import STOP_WORDS



def normalizeStr(x: str) -> str:
    return str(x).lower().strip()

def normalizeUrl(url: str) -> str:
    url = url.split('?')[0]
    url = url.split('#')[0]
    url = url.replace('https://', '').replace('http://', '').replace('www.', '')
    return url

def strictMatch(df : pd.DataFrame, column : str, score_explicatif : str) -> list:
    clusters_forts = df.groupby(column)["id"].apply(list).reset_index()
    clusters_forts = clusters_forts[clusters_forts["id"].apply(len) > 1]
    clusters_forts["cluster_id"] = clusters_forts.index
    clusters_forts["ids"] = clusters_forts["id"]
    clusters_forts["score_explicatif"] = score_explicatif
    clusters_forts = clusters_forts[["cluster_id", "ids", "score_explicatif"]]
    

    return clusters_forts.to_dict(orient="records")

def similarlyMatch(df : pd.DataFrame, column : str, score_explicatif : str) -> list:
    vectorizer = TfidfVectorizer(stop_words=list(STOP_WORDS))
    X = vectorizer.fit_transform(df[column])
    similarity_matrix = cosine_similarity(X)
    clustering = AgglomerativeClustering(
        n_clusters=None,             # pas de nombre fixe de clusters
        metric='precomputed',      # distance calculée
        linkage='complete',          # lien complet
        distance_threshold=0.15      # 1 - similarité ≈ distance
    )

    clustering_labels = clustering.fit_predict(1 - similarity_matrix)
    df['cluster_proximity'] = clustering_labels
    print(clustering_labels)
    return strictMatch(df, "cluster_proximity", score_explicatif)

