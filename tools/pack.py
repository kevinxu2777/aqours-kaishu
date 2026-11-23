import os
d=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
r=lambda f:open(os.path.join(d,f),encoding='utf8').read()
open(os.path.join(d,'index.html'),'w',encoding='utf8').write(r('template.html').replace('/*DATA*/',r('data.json').replace('</','<\\/')))
