import pandas as pd

def normalizeStr(x: str) -> str:
    return str(x).lower().strip().replace(" ", "")

def normalizeUrl(url: str) -> str:
    url = url.split('?')[0]
    url = url.split('#')[0]
    url = url.replace('https://', '').replace('www.', '')
    return url

def strictMatch(df : pd.DataFrame, urlColumn : str, score_explicatif : str) -> list:
    clusters_forts = df.groupby(urlColumn)["id"].apply(list).reset_index()
    clusters_forts = clusters_forts[clusters_forts["id"].apply(len) > 1]
    # ajouter les clusters forts au result en json [{cluster_id, ids, score_explicatif}]

    clusters_forts["cluster_id"] = clusters_forts.index
    clusters_forts["ids"] = clusters_forts["id"]
    clusters_forts["score_explicatif"] = score_explicatif
    clusters_forts = clusters_forts[["cluster_id", "ids", "score_explicatif"]]
    

    return clusters_forts.to_dict(orient="records")

def softMatch(df : pd.DataFrame, urlColumn : str) -> list: