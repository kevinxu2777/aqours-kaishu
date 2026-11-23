import json,re,unicodedata
L=json.load(open('w/live.json'));S=json.load(open('w/songs.json'));C=json.load(open('w/cats.json'))
MEM=['chika','riko','kanan','dia','you','yoshiko','hanamaru','mari','ruby']
CAST=dict(zip(MEM,['Anju Inami','Rikako Aida','Nanaka Suwa','Arisa Komiya','Shuka Saito','Aika Kobayashi','Kanako Takatsuki','Aina Suzuki','Ai Furihata']))
G={'CYaRon!':['chika','you','ruby'],'AZALEA':['kanan','dia','hanamaru'],'Guilty Kiss':['riko','yoshiko','mari'],'GKSS':['riko','yoshiko','mari'],
'YYY':['you','yoshiko','ruby'],'AiScReam':['ruby'],'Angel Kiss':['hanamaru','ruby'],'Stardust Ocean':['kanan','mari'],'Dancing Fairy':['riko','you'],'Unlimited Fantasista':['chika','dia','yoshiko'],
'Hurricane Blossom':['riko','hanamaru','mari'],'Inferno Phoenix':['dia','ruby'],'Unicorn Blizzard':['you','yoshiko'],'Twilight Tiger':['chika','kanan'],'Aqours':MEM,'CYaZALEA☆Kiss':MEM,'Saint Aqours Snow':MEM}
norm=lambda s:re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKC',s.replace('×','x').replace('＝','').replace('…','')).lower())
def clean(x):
    x=re.sub(r'<ref.*?(</ref>|/>)','',x)
    x=re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]",r'\1',x); x=re.sub(r"'{2,}|\[\[File:[^\]]*\]\]|</?(small|font|center|nowiki|big)[^>]*>",'',x)
    x=re.sub(r'\{\{[Nn]ihongo\s*\|([^|{}]*)(?:\|([^{}]*))?\}\}',lambda m:m.group(1).strip(),x)
    return x
def mem(t,default):
    t=re.sub(r'\(You & Yoshiko as back-up dancers\)','',t)
    if re.search(r'\bAll\b',t) and not re.search('All songs',t): return list(MEM)
    r=set()
    for k in sorted(G,key=len,reverse=True):
        if k in t: r|=set(G[k]); t=t.replace(k,' ')
    for m in MEM:
        if re.search(r'\b'+m.capitalize()+r'\b',t) or CAST[m] in t or (m=='yoshiko' and re.search(r'\bYohane\b',t)): r.add(m)
    return [m for m in MEM if m in r] if r else (list(default) if not re.search(r'\bby\b',t) else [])
# songs
MON={m:i+1 for i,m in enumerate('January February March April May June July August September October November December'.split())}
def date(s):
    m=re.search(r'([A-Z][a-z]+) (\d+), (20\d\d)',s); 
    return f'{m[3]}-{MON[m[1]]:02d}-{int(m[2]):02d}' if m and m[1] in MON else ''
songs={}
skip=re.compile(r'LoveLive!|Love Live!|^Aqours (C|U|E|F|O|W|\d)|Animelo|Anisong|Lantis M|CARNIVAL$|Ijigen|Musical Perf|TWO-MAN|Journey to the S|Sailing to|Minna no Oto|Yohane the P')
SS={'After The Rain','Believe again','CRASH MIND','DROPOUT!?','Dazzling White Town','Lonely Snow Planet','SELF CONTROL!!','WHITE OUT'}
for t in C['songs']:
    if skip.search(t) or t in SS: continue
    x=S[t]; a=re.search(r'\|\s*Artist\s*=\s*(.*)',x); r=re.search(r'\|\s*Released\s*=\s*(.*)',x)
    nm={'I-n-g, I TRY!!':'i-n-g, I TRY!!','Not ALONE not HITORI':'not ALONE not HITORI','Peace piece pizza':'peace piece pizza','Smile smile ship Start!':'smile smile ship Start!'}.get(t,t)
    pat=re.escape(nm)
    m=re.search(r"\{\{[Nn]ihongo\|'*\s*"+pat+r"\s*'*\s*\|+([^|}]*)",x) or re.search(r"'''\s*"+pat+r"\s*'''\s*\(([^)]*)",x) or re.search(r"'''[^'\n]{2,60}'''\s*\(([^)]*)",x) or re.search(r"\{\{[Nn]ihongo\|'''[^']*'''\s*\|+([^|}]*)",x)
    jp=re.sub(r'\s*(,\s*)?\'*lit\..*|\(.*','',m.group(1)).strip(" ,'") if m else ''
    if not re.search(r'[ぁ-んァ-ヶ一-龠]',jp): jp=nm
    aud=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',a.group(1)) if a else ''
    songs[t]=dict(id=t,rom=nm,title=jp,artist=re.sub('<.*?>','',aud).strip(),rel=date(r.group(1)) if r else '',orig=mem(aud,[]))
EXTRA={}
keys={norm(k):k for k in songs}; keys[norm('Yume + Mirai = Mugendai')]='Yume + Mirai = Mugendai'; keys['hopstepwaai']='Hop Step Waai!'
klist=sorted(keys,key=len,reverse=True)
unm={}
def line(l,default):
    l=re.sub(r'^\s*#3','##',l)
    star='*' in l[:5]; t=re.sub(r'^\s*[#*]+\s*','',l); t=re.sub(r'^Encore:\s*','',t).strip()
    n=norm(t)
    for k in klist:
        if n.startswith(k):
            # locate end of title in raw
            i=0;acc=''
            while i<len(t) and len(acc)<len(k): acc+=norm(t[i]);i+=1
            rest=t[i:]
            if rest[:1].isalnum(): continue
            return keys[k],rest,star,t
    unm[t]=unm.get(t,0)+1
    return None,t,star,t
def blocks(page,joint=False):
    x=L[page]; m=re.search(r'\n==[^=\n]*(Set ?-?list|Set Lists)[^=\n]*==',x,re.I)
    x=x[m.start():] if m else x
    x=re.split(r'\n==(?!=)\s*(?!Set|Anisong|Lantis|20)',x[3:])[0]
    x=clean(x); out=[];leg='';tab='';cur=None;parent=''
    for l in x.split('\n'):
        h=re.match(r'\s*===?=?\s*([^=]+?)\s*=+\s*$',l); tb=re.match(r'^(?:\{\{Aqours Tab\|(?:1=)?\s*)?(?:<tabber>\s*)?((?:Day|Both|Night|Noon|Evening)[^=#]*?)\s*=\s*$',l.replace('|-|','').strip()); ne=re.match(r'^(Noon|Evening):',l)
        if h: leg=h[1];tab='';cur=None
        elif tb: tab=tb[1];cur=None
        elif ne: cur=dict(leg=leg,tab=(tab+' '+ne[1]).strip(),lines=[]);out.append(cur)
        elif re.match(r'\s*#',l):
            if cur is None: cur=dict(leg=leg,tab=tab,lines=[]);out.append(cur)
            cur['lines'].append(l)
    return out
def parse(b,default,joint):
    r=[];parent=''
    for l in b['lines']:
        star='*' in l[:5]
        if not star: parent=l
        if star and re.search('Intermission|intermission',parent): continue
        s,rest,st,t=line(l,default)
        if not s: continue
        if re.search('Intermission',rest): continue
        ms=mem(rest,[] if joint else default)
        if not ms: continue
        e=dict(s=s,m=ms)
        if star or re.search(r'short|TV anime version|TV Size',rest,re.I): e['short']=1
        v=re.search(r'(Remix|Punk Rock|Hard Rock|Digital Rock|Melodious Hardcore|Cute Rock)',rest)
        if v: e['v']=v[1]+' Ver.'
        if 'Uranohoshi Symphony' in rest: e['v']='オーケストラ'
        r.append(e)
    return r
def perf(page):
    x=clean(L[page]); return [m for m in MEM if CAST[m] in x]
if __name__=='__main__':
    for t in L:
        if t in C['ss'] or t in C['songs']:
            j=not t in C['ss'] or 'Fest' in t and 'Numazu' not in t or t in('Lantis Matsuri','Animelo Summer Live','Anisong World Matsuri')
            print('##',t,'perf',len(perf(t)),[m for m in MEM if m not in perf(t)])
            for b in blocks(t): print('   ',b['leg'][:40],'|',b['tab'],'|',len(b['lines']),len(parse(b,MEM,j)))
    print({k:v for k,v in unm.items() if not re.match(r'MC|Intermission|Opening|Anime I|Talk',k)}.keys().__len__())
    A=[k for k in unm if re.search('Aqours|CYaRon|AZALEA|Guilty Kiss|Chika|Riko|Kanan|Dia K|You W|Yoshiko|Hanamaru|Ohara|Ruby|YYY',k) and not k.startswith('MC')]
    print('\n'.join(A))
    for s in songs.values(): print(s['id'],'|',s['title'],'|',s['artist'],'|',s['rel'],'|',len(s['orig']))
