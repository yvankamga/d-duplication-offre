import pandas as pd
from utils import normalizeStr, normalizeUrl, strictMatch


result = []

df = pd.read_csv('data.csv')

df["titre_norm"] = df["title"].apply(normalizeStr)
df["entreprise_norm"] = df["company"].apply(normalizeStr)
df["ville_norm"] = df["city"].apply(normalizeStr)
df["url_norm"] = df["url"].apply(normalizeUrl)


df["key_canonique"] = (
    df["titre_norm"] + "_" +
    df["entreprise_norm"] + "_" +
    df["ville_norm"] + "_" +
    df["posted_date"].astype(str)
)

result.extend(strictMatch(df, "url_norm", "url_match"))
result.extend(strictMatch(df, "key_canonique", "titre+entreprise+ville+date_match"))
result.extend(strictMatch(df, "base_id", "external_id_match"))

print(result)