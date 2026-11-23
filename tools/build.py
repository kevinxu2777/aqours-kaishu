from parse import *
import datetime,os
LL='ラブライブ！サンシャイン!! '
P={}
for t in L: P[re.sub(r'[^A-Za-z0-9]','',t)]=t
def pg(s):
    c=[t for t in L if s in t]; assert len(c)>=1,s; return c[0]
N='夜';H='昼'
def days(*ds): return [(f'Day {i+1}',d) for i,d in enumerate(ds)]
def hn(d,p=''): return [(p+'昼公演',d),(p+'夜公演',d)]
CFG=[]  # append only: share links depend on order
def ev(name,kind,page,legs,default=MEM,absent=(),joint=False,pick=None,online=False,rep=None):
    CFG.append(dict(name=name,kind=kind,page=page,legs=legs,default=default,absent=absent,joint=joint,pick=pick,online=online,rep=rep))
CY,AZ,GK=G['CYaRon!'],G['AZALEA'],G['Guilty Kiss']
ev('Aqours First LoveLive! ～Step! ZERO to ONE～','live','Aqours First',[('','横浜アリーナ',days('2017-02-25','2017-02-26'))])
ev('Aqours 2nd LoveLive! HAPPY PARTY TRAIN TOUR','live','HAPPY PARTY TRAIN TOUR',[('名古屋公演','日本ガイシホール',days('2017-08-05','2017-08-06')),('神戸公演','神戸ワールド記念ホール',days('2017-08-19','2017-08-20')),('埼玉公演','メットライフドーム',days('2017-09-29','2017-09-30'))])
ev('Aqours クラブ活動 LIVE & FAN MEETING ～Landing action Yeah!!～','fan','Landing action Yeah!!',[
 ('大阪公演','オリックス劇場',[('Day 1','2017-11-04')]+hn('2017-11-05','Day 2 ')),('札幌公演','札幌市文化芸術劇場系ホール',[('Day 1','2017-12-09')]+hn('2017-12-10','Day 2 ')),
 ('沼津公演','沼津市民文化センター',hn('2017-12-16')),('福岡公演','福岡サンパレス',hn('2018-01-06')),('名古屋公演','名古屋国際会議場 センチュリーホール',hn('2018-02-03')),('千葉公演','幕張メッセ イベントホール',[('Day 1','2018-03-10')]+hn('2018-03-11','Day 2 ')),
 ('ソウル公演','KBSアリーナ',hn('2017-11-18')),('上海公演','静安体育中心',hn('2018-01-20')),('台北公演','台北国際会議センター',[('','2018-02-10')])])
CFG[-1]['legs'][1]=('札幌公演','ニトリ文化ホール',CFG[-1]['legs'][1][2])
ev('Saint Snow PRESENTS HAKODATE UNIT CARNIVAL','live','HAKODATE',[('','函館アリーナ',days('2018-04-27','2018-04-28'))])
ev('Aqours 3rd LoveLive! Tour ～WONDERFUL STORIES～','live','WONDERFUL STORIES～',[('埼玉公演','メットライフドーム',days('2018-06-09','2018-06-10')),('大阪公演','大阪城ホール',days('2018-06-16','2018-06-17')),('福岡公演','マリンメッセ福岡',days('2018-07-07','2018-07-08'))])
ev('Aqours World LoveLive! in LA ～Beyond the Pacific～','live','Beyond the Pacific',[('','Microsoft Theater（ロサンゼルス）',[('','2018-07-04')])])
ev('Aqours クラブ活動 LIVE & FAN MEETING 2018 ユニット対抗全国ツアー','fan','Unit Battle',[
 ('名古屋公演（AZALEA）','日本特殊陶業市民会館 フォレストホール',hn('2018-09-22','Day 1 ')+[('Day 2','2018-09-23')]),('松山公演（CYaRon!）','松山市民会館',hn('2018-09-24')),('福岡公演（Guilty Kiss）','福岡サンパレス',hn('2018-12-02')),('仙台公演（AZALEA）','仙台サンプラザホール',hn('2018-12-15')),
 ('千葉公演（Guilty Kiss）','幕張メッセ イベントホール',[('Day 1','2019-01-05')]+hn('2019-01-06','Day 2 ')),('広島公演（AZALEA）','広島文化学園HBGホール',hn('2019-01-13')),('金沢公演（CYaRon!）','本多の森ホール',hn('2019-01-19')),
 ('旭川公演（Guilty Kiss）','旭川市民文化会館',[('Day 1','2019-01-26')]+hn('2019-01-27','Day 2 ')),('沼津公演','沼津市民文化センター',[('CYaRon!','2019-02-09'),('AZALEA（昼）','2019-02-10'),('Guilty Kiss（夜）','2019-02-10')]),('大阪公演（CYaRon!）','オリックス劇場',[('Day 1','2019-02-16')]+hn('2019-02-17','Day 2 ')),
 ('東京公演（Aqours）','武蔵野の森総合スポーツプラザ',hn('2019-03-02','Day 1 ')+hn('2019-03-03','Day 2 '))],rep=lambda b:b[:-2]+[b[-2],b[-2],b[-1],b[-1]])
ev('Aqours 4th LoveLive! ～Sailing to the Sunshine～','live','4th LoveLive! ～Sailing',[('','東京ドーム',days('2018-11-17','2018-11-18'))])
ev('Aqours World LoveLive! ASIA TOUR 2019','live','ASIA TOUR 2019',[('上海公演','国家会展中心（上海）',days('2019-03-23','2019-03-24')),('台北公演','台北国際会議センター',days('2019-04-06','2019-04-07')),('千葉公演','幕張メッセ イベントホール',days('2019-04-13','2019-04-14')),('ソウル公演','KBSアリーナ',days('2019-04-20','2019-04-21'))],rep=lambda b:b*4,absent={i:['dia'] for i in (1,3,4,5,6,7)})
ev('Aqours 5th LoveLive! ～Next SPARKLING!!～','live','5th LoveLive! ～Next',[('','メットライフドーム',days('2019-06-08','2019-06-09'))])
ev('Aqours World LoveLive! in LA ～BRAND NEW WAVE～','live','in LA ～BRAND',[('','The Novo（ロサンゼルス）',days('2019-07-05','2019-07-06'))],absent=['dia'])
ev('Unit LIVE ADVENTURE 2020','live','Unit Live Adventure',[('Guilty Kiss ～New Romantic Sailors～','武蔵野の森総合スポーツプラザ',days('2020-02-08','2020-02-09')),('CYaRon! ～Braveheart Coaster～','西日本総合展示場 新館',days('2020-02-22','2020-02-23'))])
ev('Aqours ONLINE LoveLive!','live','Aqours ONLINE LoveLive!',[('～LOST WORLD～','オンライン',days('2020-10-10','2020-10-11')),('COUNTDOWN ～WHITE ISLAND～','オンライン',days('2020-12-30','2020-12-31'))],online=True,absent={2:['hanamaru'],3:['hanamaru']})
ev('AZALEA 1st LoveLive! ～In The Dark /*秘密の物語*/～','live','AZALEA 1st',[('','ゼビオアリーナ仙台',days('2021-08-14','2021-08-15'))],default=AZ,absent=['hanamaru'])
ev('Guilty Kiss 2nd LoveLive! ～Return To Love ♡ Kiss Kiss Kiss～','live','Guilty Kiss 2nd',[('','東京ガーデンシアター',days('2021-09-25','2021-09-26'))],default=GK)
ev('CYaRon! 2nd LoveLive! ～大革命☆Wake Up Kingdom～','live','CYaRon! 2nd',[('','幕張メッセ 国際展示場1-3',days('2021-10-16','2021-10-17'))],default=CY)
ev('AZALEA 2nd LoveLive! ～Amazing Travel DNA Reboot～','live','AZALEA 2nd',[('','横浜アリーナ',days('2021-11-15','2021-11-16'))],default=AZ,absent=['hanamaru'])
ev('Aqours EXTRA LoveLive! ～DREAMY CONCERT 2021～','live','DREAMY CONCERT',[('','ぴあアリーナMM',days('2021-12-29','2021-12-30'))])
ev('Aqours 6th LoveLive! ～KU-RU-KU-RU Rock ‘n’ Roll TOUR～','live','Aqours 6th',[('<OCEAN STAGE>','バンテリンドーム ナゴヤ',days('2022-02-12','2022-02-13')),('<SUNNY STAGE>','ベルーナドーム',days('2022-03-05','2022-03-06')),('<WINDY STAGE>','東京ドーム',days('2022-06-25','2022-06-26'))])
ev('沼津地元愛まつり（2022）','fan','Numazu Jimo Ai Festival',[('8月13日','',hn('2022-08-13')),('8月14日','',hn('2022-08-14'))])
ev('Aqours EXTRA ラブライブ！ 2023 ～It’s a 無限大☆WORLD～','live','Mugendai',[('【Valentine’s Day Concert】','武蔵野の森総合スポーツプラザ',days('2023-02-11','2023-02-12')),('【White Day Concert】','幕張メッセ イベントホール',days('2023-03-11','2023-03-12'))])
ev('浦の星女学院RADIO!!! JMA出張放送局 ～バブ卒大集合！～','fan','Station ~Babu',[('沼津公演','沼津市民文化センター',hn('2023-05-28')),('東京公演','J:COMホール八王子',hn('2023-06-24'))],default=G['YYY'],absent={0:['ruby'],1:['ruby']})
ev('沼津地元愛まつり 2023','fan','Festival 2023',[('10月7日','',hn('2023-10-07')),('10月8日','',hn('2023-10-08')),('10月9日','',hn('2023-10-09'))])
ev('幻日のヨハネ -The Story of the Sound of Heart-','live','Yohane the Parhelion: The Story',[('','武蔵野の森総合スポーツプラザ',days('2023-12-15','2023-12-16','2023-12-17'))])
ev('浦の星女学院RADIO!!! JMA出張放送局2 ～かえってきたバブ卒達！～','fan','Station 2 ~',[('神戸公演','神戸国際会館こくさいホール',hn('2024-04-06')),('東京公演','豊洲PIT',hn('2024-04-13')),('沼津公演','沼津市民文化センター',hn('2024-07-20'))],default=G['YYY'])
ev('沼津地元愛まつり 2024','fan','Festival 2024',[('9月14日','',hn('2024-09-14')),('9月15日','',hn('2024-09-15')),('9月16日','',hn('2024-09-16'))])
ev('Aqours Finale LoveLive! ～永久stage～','live','Aqours Finale LoveLive! ~Eikyuu stage~',[('','ベルーナドーム',days('2025-06-21','2025-06-22'))])
ev('沼津地元愛まつり 2025','fan','Festival 2025',[('11月1日','',hn('2025-11-01')),('11月2日','',hn('2025-11-02')),('11月3日','',hn('2025-11-03'))])
ev('Guilty Kiss × Saint Snow TWO-MAN LIVE "VS"','live','TWO-MAN',[('','ぴあアリーナMM',days('2026-07-04','2026-07-05'))],default=GK)
ev('Guilty Kiss Musical Performance 漆黒のWanted Ghost','live','Musical Perf',[('','沼津市民文化センター',hn('2026-11-22')+hn('2026-11-23'))],default=GK)
ev('沼津地元愛まつり 2027','fan','Festival 2027',[('3月20日','',hn('2027-03-20')),('3月21日','',hn('2027-03-21')),('3月22日','',hn('2027-03-22'))])
J=lambda *a,**k:ev(*a,joint=True,**k)
J('Anisong World Matsuri / STAR PHASE 2017','joint','Anisong World',[('～Japan Kawaii Live～','Microsoft Theater（ロサンゼルス）',[('','2017-06-30')]),('BILIBILI MACRO LINK','メルセデス・ベンツアリーナ（上海）',[('','2017-07-22')])])
J('Animelo Summer Live','joint','Animelo',[],pick='anisama')
J('ランティス祭り2019','joint','Lantis Matsuri',[],pick='lantis')
J('LoveLive! Series 9th Anniversary ラブライブ！フェス','joint',None,[('','さいたまスーパーアリーナ',days('2020-01-18','2020-01-19'))],pick='Love Live! Fest')
J('COUNTDOWN LoveLive! 2021→2022 ～LIVE with a smile!～','joint','COUNTDOWN',[('','ぴあアリーナMM',[('','2021-12-31')])])
J('異次元フェス アイドルマスター★♥ラブライブ！歌合戦','joint','Uta Gassen',[('','東京ドーム',days('2023-12-09','2023-12-10'))])
J('ユニット甲子園 2024','joint','Koushien',[('','Kアリーナ横浜',days('2024-03-09','2024-03-10'))],absent=['hanamaru'])
J('LoveLive! Series Asia Tour 2024 ～みんなで叶える物語～','joint','Asia Tour 2024',[('上海公演','国家会展中心 虹館',[('','2024-10-06')]),('台北公演','Zepp New Taipei',days('2024-11-09','2024-11-10')),('横浜公演','Kアリーナ横浜',days('2025-02-01','2025-02-02'))],rep=lambda b:[b[1],b[2],b[3],b[5],b[6]],absent=[m for m in MEM if m not in G['YYY']])
J('U-NEXT MUSIC FES ラブライブ！シリーズ EXPO 2025 STAGE','joint','U-NEXT',[('','EXPOアリーナ「Matsuri」',[('','2025-08-14')])],absent=[m for m in MEM if m not in G['YYY']])
J('AiScReam presents TOPPING LIVE','joint','TOPPING',[('','パシフィコ横浜 国立大ホール',days('2025-09-06','2025-09-07'))])
J('LoveLive! Series 15th Anniversary ラブライブ！フェス','joint',None,[('名古屋公演','バンテリンドーム ナゴヤ',days('2026-11-14','2026-11-15'))],pick='LoveLive! Series 15th Anniversary Love Live! Fest',absent=['kanan','dia','mari','ruby'])
J('ラブライブ！フェス Encore in TOKYO DOME','joint','Encore in TOKYO',[('','東京ドーム',days('2027-02-13','2027-02-14'))])
def manual(kind):
    x=clean(L[pg('Animelo' if kind=='anisama' else 'Lantis Matsuri')]); out=[]
    ls=x.split('\n')
    if kind=='anisama':
        yr='';cur={}
        for l in ls:
            m=re.match(r'\s*==\s*(20\d\d)',l)
            if m: yr=m[1]
            if re.match('#',l) and 'by Aqours' in l: cur.setdefault(yr,[]).append(l)
        D={'2017':('2017-08','The Card'),'2018':('2018-08','OK!'),'2019':('2019-08-31','STORY')}
        return [dict(leg=f'{y} {D[y][1]}',venue='さいたまスーパーアリーナ',label='',date=D[y][0],lines=v) for y,v in cur.items()]
    d1=[l for l in ls if re.match(r'#[^#]',l) and re.search('by Aqours',l)]
    d3=[l for l in ls if l.startswith('##') and re.search('CYaRon|AZALEA|Guilty',l)]
    ny=[l for l in ls if re.match(r'#[^#]',l) and 'by Guilty Kiss' in l]
    return [dict(leg='千葉公演',venue='幕張メッセ',label='Day 1',date='2019-06-21',lines=d1),dict(leg='千葉公演',venue='幕張メッセ',label='Day 3',date='2019-06-23',lines=d3),dict(leg='ニューヨーク公演',venue='Javits Center',label='',date='2019-11-15',lines=ny)]
fix={'Future flight':'Future flight','U-CYU':'U-CYU'}
for k,v in fix.items(): songs[k]['title']=v
for k in [k for k in songs if 'TOPPING' in k or 'GIG' in k]: del songs[k]
keys_=[k for k,v in keys.items() if v not in songs]
for k in keys_: del keys[k]; klist.remove(k)
YO={'BLOOM OF COLORS','Be as one!!!','Best wishes','Far far away','Forever U & I','Futari de Hitotsu','GAME ON!','GIRLS!!','Genjitsu Mysterium','Hey, dear my friends','Kimi no Tame Boku no Tame','Koukishin Journey','La la Yuuki no Uta','Numazu Yassa Yoisa Uta','R・E・P','SILENT PAIN','Special Holidays','Te・ki・na Music','Tick-Tack, Tick-Tack','Wonder sea breeze'}
songs['La la Yuuki no Uta']['orig']=MEM if False else songs['La la Yuuki no Uta']['orig']
def grp(s):
    if s['id'] in YO: return 'yohane'
    a=s['artist']
    for g,k in [('CYaRon!','cyaron'),('AZALEA','azalea'),('Guilty Kiss','gk'),('GKSS','gk'),('YYY','mini')]:
        if a.startswith(g) : return k
    if len(s['orig'])>=6: return 'aqours'
    return 'solo' if len(s['orig'])==1 and a.count(' ')==1 else 'mini'
sid={k:i for i,k in enumerate(sorted(songs))}
# stable ids from slug
slug=lambda k:norm(k)[:40]
outS=[dict(id=slug(k),t=s['title'],r=s['rom'] if s['rom']!=s['title'] else '',a=s['artist'].rstrip('.'),d=s['rel'],o=s['orig'],g=grp(s)) for k,s in songs.items()]
assert len({s['id'] for s in outS})==len(outS)
outE=[];n=0
for c in CFG:
    shows=[]
    if c['pick'] in('anisama','lantis'): bl=manual(c['pick'])
    else:
        page=c['pick'] or pg(c['page']); bl=blocks(page)
        if c['rep']: bl=c['rep'](bl)
        slots=[(lg,v,lab,d) for lg,v,ds in c['legs'] for lab,d in ds]
        if not bl: bl=[dict(lines=[]) for _ in slots]
        assert len(bl)==len(slots),(c['name'],len(bl),len(slots))
        bl=[dict(b,leg=s[0],venue=s[1],label=s[2],date=s[3]) for b,s in zip(bl,slots)]
    for i,b in enumerate(bl):
        ab=c['absent'].get(i,[]) if isinstance(c['absent'],dict) else c['absent']
        L_=[]
        for e in parse(b,c['default'],c['joint']):
            m=[x for x in e['m'] if x not in ab]
            if m: L_.append(dict(e,s=slug(e['s']),m=''.join(str(MEM.index(x)) for x in m)))
        shows.append(dict(id=n,leg=b['leg'],venue=b['venue'],label=b['label'],date=b['date'],set=L_,**({'approx':1} if b.get('approx') else {})));n+=1
    outE.append(dict(name=c['name'],kind=c['kind'],online=c['online'],shows=shows))
# BML as its own event; 2017 keeps its id, 2019 is appended (source: setlist.fm; Dia absent per attendee report)
asia=next(e for e in outE if 'ASIA TOUR 2019' in e['name'])
for i in (0,2): asia['shows'][i]['note']=1
awm=next(e for e in outE if e['name'].startswith('Anisong World Matsuri'))
b17=next(s for s in awm['shows'] if s['leg']=='BILIBILI MACRO LINK')
awm['shows'].remove(b17);awm['name']='Anisong World Matsuri 2017 ～Japan Kawaii Live～';awm['shows'][0]['leg']=''
AR='メルセデス・ベンツアリーナ（上海）'
b17.update(leg='BML-SP 2017',venue=AR)
outE.append(dict(name='BILIBILI MACRO LINK - STAR PHASE（BML-SP）',kind='joint',online=False,shows=[b17,dict(id=n,leg='BML-SP 2019',venue=AR,label='',date='2019-07-21',set=[dict(s=slug(k),m='01245678') for k in ['Mirai no Bokura wa Shitteru yo','WATER BLUE NEW WORLD','WONDERFUL STORIES','Yuuki wa doko ni? Kimi no Mune ni!']])]));n+=1
for s in outS: s['o']=''.join(str(MEM.index(x)) for x in s['o'])
json.dump(dict(songs=outS,events=outE),open(os.path.expanduser('~/Developer/aqours-kaishu/data.json'),'w'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(len(outS),Counter(s['g'] for s in outS),len(outE),n,sum(len(x['set']) for e in outE for x in e['shows']))
pf={x['s'] for e in outE for x in sum([y['set'] for y in e['shows']],[])}
print('never',[s['t'] for s in outS if s['id'] not in pf])
for e in outE[-13:]: print(e['name'],[(x['date'],len(x['set'])) for x in e['shows']])
print([ (s['t'],s['g'],s['a']) for s in outS if s['g'] in('mini',)])
print('nodate',[s['t'] for s in outS if not s['d']])
