import json,urllib.request,urllib.parse
def api(**k):
    k.update(format='json',formatversion=2)
    r=urllib.request.Request('https://love-live.fandom.com/api.php?'+urllib.parse.urlencode(k),headers={'User-Agent':'Mozilla/5.0 generic-client'})
    return json.load(urllib.request.urlopen(r,timeout=30))
