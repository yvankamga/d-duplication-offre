def normalizeStr(x: str) -> str:
    return str(x).lower().strip()

def normalizeUrl(url: str) -> str:
    url = url.split('?')[0]
    url = url.split('#')[0]
    url = url.replace('https://', '').replace('www.', '')
    return url