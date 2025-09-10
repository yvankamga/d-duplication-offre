import pandas as pd
from utils import normalizeStr, normalizeUrl, strictMatch, similarlyMatch


couplageFort = []
couplageProbable = []

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

couplageFort.extend(strictMatch(df, "url_norm", "url_match"))
couplageFort.extend(strictMatch(df, "key_canonique", "titre+entreprise+ville+date_match"))
couplageFort.extend(strictMatch(df, "base_id", "external_id_match"))

couplageProbable.extend(similarlyMatch(df, "description", "similarité_description≥0.85"))
couplageProbable.extend(similarlyMatch(df, "key_canonique", "similarité_titre+entreprise+ville+date≥0.85"))

result ={
    "Forts": couplageFort,
    "Probables": couplageProbable
}

with open('result.json', 'w') as f:
    json.dump(result, f)

print("Resultat ecrit dans result.json")