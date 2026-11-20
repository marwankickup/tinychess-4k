import json,os,urllib.request as UQ
PS="777777767789889:999;<<<=AAAA7777-/11/377179:18:;17:;189:/378-/11;=97;;775333311/1//-1//-1//-1//--111117715;=15=?15=?15;=1357-/13"
VM=[100,320,330,500,950,0];VA=VM+[-x for x in VM]
VE=[130,320,350,540,1020,0];VEa=VE+[-x for x in VE];PW=[0,1,1,2,4,0]
def dc(si):
 r=[0]*128
 for i in range(64):
  f=i%8;r[(i//8)*16+f]=(ord(PS[si*32+(i//8)*4+min(f,7-f)])-55)*5
 return r
PM=[dc(0),dc(1),[0]*128,[0]*128,[0]*128,dc(2)]
for t in range(6):PM.append([-PM[t][q^112]for q in range(120)])
PE=PM[:];PE[5]=dc(3)
PE[11]=[-PE[5][q^112]for q in range(120)]
ND=[-33,-31,-18,-14,14,18,31,33];KD=[-17,-16,-15,-1,1,15,16,17]
DR=[0,0,ND,[-17,-15,15,17],[-16,-1,1,16],KD,KD]
B=[0]*128;S=1;EV=[0,0];PH=0;KS=[0,0];TT={}
N=[0,0];F="abcdefgh"
def ky():return bytes([v+6 for v in B]+[S+1])
def RS(v):
 global S,PH;B[:],S,EV[:],PH,KS[:]=v
def at(s,by):
 for ds,vv in(((15,17),1),(ND,2),(KD,6)):
  for d in ds:
   t=s+d*(-by if vv==1 else 1)
   if not t&0x88 and B[t]==vv*by:return 1
 for d in KD:
  t=s+d
  while not t&0x88:
   p=B[t]
   if p:
    if p*by in(5,3 if d in DR[3] else 4):return 1
    break
   t+=d
 return 0
def gn(cp):
 ms=[];s=S;ap=ms.append;lr=7 if s>0 else 0
 for f in range(120):
  p=B[f]
  if p*s<=0:continue
  a=abs(p)
  if a==1:
   for dd in(16,15,17):
    t=f+dd*s
    if t&0x88:continue
    if dd==16:
     if B[t]:continue
     if t>>4==lr:ap(f|t<<7|5<<14)
     elif not cp:
      ap(f|t<<7)
      if f>>4==(1 if s>0 else 6)and not B[f+32*s]:ap(f|(f+32*s)<<7)
    elif B[t]*s<0:ap(f|t<<7|(5<<14 if t>>4==lr else 0))
  else:
   for d in DR[a]:
    t=f+d
    while not t&0x88 and not B[t]:
     if not cp:ap(f|t<<7)
     if a==2 or a==6:break
     t+=d
    if not t&0x88 and B[t]*s<0:ap(f|t<<7)
 return ms
def mk(m):
 global S,PH;f=m&127;t=m>>7&127;pr=m>>14;p=B[f];s=S;cap=B[t];cs=t;a=abs(p)
 if a==1 and not cap and f&7^t&7:cs=t-16*s;cap=B[cs]
 zi=p-1 if p>0 else 5-p;B[f]=0
 if cap:
  zc=cap-1 if cap>0 else 5-cap;B[cs]=0;EV[0]-=VA[zc]+PM[zc][cs];EV[1]-=VEa[zc]+PE[zc][cs];PH-=PW[abs(cap)-1]
 if pr:
  zn=pr-1 if s>0 else 5+pr;B[t]=pr*s;EV[0]+=VA[zn]+PM[zn][t]-VA[zi]-PM[zi][f];EV[1]+=VEa[zn]+PE[zn][t]-VEa[zi]-PE[zi][f];PH+=PW[pr-1]
 else:
  B[t]=p;EV[0]+=PM[zi][t]-PM[zi][f];EV[1]+=PE[zi][t]-PE[zi][f]
 if a==6:
  KS[s<0]=t
  if abs(t-f)==2:
   rf,rt=(f+3,f+1)if t>f else(f-4,f-1)
   rp=B[rf];B[rt]=rp;B[rf]=0
 S=-s
def sr(d,a,b,ply):
 N[0]+=1
 if N[0]>6e4:1/0
 k0=ky();ic=at(KS[S<0],-S)
 tm=0;best=-1e5;bm=-1
 if d>0:
  e=TT.get(k0)
  if e:
   tm,td,fl,sc=e
   if ply>0 and td>=d and((fl==1 and sc>=b)or(fl==2 and sc<=a)):return sc
 elif not ic:
  best=(EV[0]*PH+EV[1]*(24-PH))//24*(-1)**(S<0)
  if best>=b:return best
  if best>a:a=best
 sv=(B[:],S,EV[:],PH,KS[:])
 for s0,m in sorted([(9000000 if m==tm else 8000000+abs(B[m>>7&127])*32-abs(B[m&127])if B[m>>7&127]else 0,m)for m in gn(0 if ic or d>0 else 1)],reverse=True):
  mk(m)
  if at(KS[-S<0],S):RS(sv);continue
  sc=-sr(d-1 if d>0 else 0,-b,-a,ply+1);RS(sv)
  if sc>best:
   best=sc;bm=m
   if ply==0:N[1]=m
   if sc>a:
    a=sc
    if a>=b:break
 if bm<0:return-9999 if ic else 0 if d>0 else best
 if d>0:TT[k0]=(bm,d,1 if best>=b else 2,best)
 return best
bk=[4,2,3,5,6,3,2,4]
for f in range(8):
 for q,p in((f,bk[f]),(16+f,1),(96+f,-1),(112+f,-bk[f])):B[q]=p
KS[:]=[4,116];PH=24
SN=(B[:],S,EV[:],PH,KS[:])
def u2m(u):
 m=(ord(u[0])-97+(ord(u[1])-49)*16)|((ord(u[2])-97+(ord(u[3])-49)*16)<<7)
 if len(u)>4:m|="nbrq".index(u[4])+2<<14
 return m
def th():
 if len(TT)>3e5:TT.clear()
 N[1]=0;N[0]=0
 try:
  for d in range(80):sr(d,-1e5,1e5,0)
 except:pass
 return N[1]
def post(p,b):return json.load(UQ.urlopen(URL+p,json.dumps(b).encode()))
if __name__=="__main__":
 URL=os.environ["MAKEFUN_ENV_URL"]
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   RS(SN)
   for u in g["moves"]:mk(u2m(u))
   try:
    m=th();f=m&127;t=m>>7&127
    u=F[f&7]+chr(49+(f>>4))+F[t&7]+chr(49+(t>>4))+("nbrq"[(m>>14)-2]if m>>14 else"")
   except:u=""
   if u not in g["legal_moves"]:u=g["legal_moves"][0]
   g=post("/move",{"game":g["game"],"move":u})
