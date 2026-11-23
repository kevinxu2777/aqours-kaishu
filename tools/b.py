from api import api
import json,os
def cat(c):
    o=[];k={}
    while 1:
        r=api(action='query',list='categorymembers',cmtitle=c,cmlimit=500,**k); o+=[x['title'] for x in r['query']['categorymembers'] if x['ns']==0]
        if 'continue' in r:k={'cmcontinue':r['continue']['cmcontinue']}
        else:return o
live=cat('Category:Live Concerts'); ss=set(cat('Category:Love Live! Sunshine!!'))
songs=set(cat('Category:Discography:Aqours'))
print(len(live)); print('\n'.join(('*' if t in ss else ' ')+t for t in live))
json.dump(dict(live=live,ss=sorted(ss),songs=sorted(songs)),open('w/cats.json','w'))
def get(ts):
    d={}
    ts=sorted(ts)
    for i in range(0,len(ts),40):
        r=api(action='query',titles='|'.join(ts[i:i+40]),prop='revisions',rvprop='content',rvslots='main')
        for p in r['query']['pages']:
            if 'revisions' in p: d[p['title']]=p['revisions'][0]['slots']['main']['content']
    return d
L=get(set(live)|{'Love Live! Sunshine!! Numazu Jimo Ai Festival','Anisong World Matsuri','Animelo Summer Live','LoveLive! Series 15th Anniversary Love Live! Fest','Aqours'})
json.dump(L,open('w/live.json','w'),ensure_ascii=False)
S=get(songs|ss); json.dump(S,open('w/songs.json','w'),ensure_ascii=False); print(len(L),len(S),sum('Infobox' in v for v in S.values()))
