import json,os,urllib.request as UQ
PS="777777767789889:999;<<<=AAAA7777-/11/377179:18:;17:;189:/378-/11;=97;;775333311/1//-1//-1//-1//-"
VA=[100,320,330,500,950,0];VA+=[-x for x in VA]
VEa=[130,320,350,540,1020,0];VEa+=[-x for x in VEa]
PW=[0,1,1,2,4,0]
def dc(si):
 r=[0]*128
 for i in range(64):
  f=i%8;r[i//8*16+f]=(ord(PS[si*32+i//8*4+min(f,7-f)])-55)*5
 return r
PM=[dc(0),dc(1),[0]*128,[0]*128,[0]*128,dc(2)]
PM+=[[-PM[t][q^112]for q in range(120)]for t in range(6)]
ND=[-33,-31,-18,-14,14,18,31,33];KD=[-17,-16,-15,-1,1,15,16,17]
DR=[0,0,ND,[-17,-15,15,17],[-16,-1,1,16],KD,KD]
B=[0]*128;S=1;EV=[0,0];PH=0;KS=[0,0];TT={};KL=[0]*999;CM={4:12,0:13,7:14,116:3,112:7,119:11};N=[0,0]
def RS(v):
 global S,PH;B[:],S,EV[:],PH,KS[:]=v
def at(s,by):
 for ds,vv,pc in(((15,17),-by,1),(ND,1,2),(KD,1,6)):
  for d in ds:
   t=s+d*vv
   if not t&0x88 and B[t]==pc*by:return 1
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
 ms=[];s=S;ap=ms.append;lr=7*(s>0)
 for f in range(120):
  p=B[f]
  if p*s<=0:continue
  a=abs(p)
  if a==1:
   t=f+16*s
   if not B[t]:
    if t>>4==lr:ap(f|t<<7|5<<14)
    elif not cp:
     ap(f|t<<7)
     if f>>4==(s<0)*5+1 and not B[f+32*s]:ap(f|(f+32*s)<<7)
   for dd in(15,17):
    t=f+dd*s
    if not t&0x88 and(B[t]*s<0 or t==B[121]):ap(f|t<<7|((t>>4==lr)*5)<<14)
  else:
   for d in DR[a]:
    t=f+d
    while not t&0x88 and not B[t]:
     if not cp:ap(f|t<<7)
     if a in(2,6):break
     t+=d
    if not t&0x88 and B[t]*s<0:ap(f|t<<7)
 if not cp and B[(e:=4+112*(s<0))]==6*s:
  for g,w,r in((1,1,3),(-1,2,-4)):
   if B[120]>>(s<0)*2&w and B[e+r]==4*s and not(B[e+g]or B[e+2*g]or g<0 and B[e-3])and not at(e,-s)and not at(e+g,-s):ap(e|(e+2*g)<<7)
 return ms
def mk(m):
 global S,PH;f=m&127;t=m>>7&127;pr=m>>14;p=B[f];s=S;cap=B[t];cs=t;a=abs(p)
 B[120]&=CM.get(f,15)&CM.get(t,15)
 B[121]=f+16*s if a==1 and t-f==32*s else-1
 if a==1 and not cap and f&7^t&7:cs=t-16*s;cap=B[cs]
 zi=p-1 if p>0 else 5-p;B[f]=0
 if cap:
  zc=abs(cap)-1+6*(cap<0);B[cs]=0;EV[0]-=VA[zc]+PM[zc][cs];EV[1]-=VEa[zc]+PM[zc][cs];PH-=PW[abs(cap)-1]
 B[t]=p;EV[0]+=PM[zi][t]-PM[zi][f];EV[1]+=PM[zi][t]-PM[zi][f]
 if pr:
  zn=pr-1+6*(s<0);B[t]=pr*s;EV[0]+=VA[zn]+PM[zn][t]-VA[zi]-PM[zi][t];EV[1]+=VEa[zn]+PM[zn][t]-VEa[zi]-PM[zi][t];PH+=PW[pr-1]
 if a==6:
  KS[s<0]=t
  if abs(t-f)==2:
   rf,rt=(f+3,f+1)if t>f else(f-4,f-1)
   rp=B[rf];B[rt]=rp;B[rf]=0
 S=-s
def sr(d,a,b,ply):
 N[0]+=1
 if N[0]>6e4:1/0
 k0=bytes([v+6 for v in B]+[S+1]);ic=at(KS[S<0],-S)
 tm=0;best=-1e5;bm=-1
 if d>0:
  e=TT.get(k0)
  if e:
   tm=e[0]
   if ply>0 and e[1]>=d and(e[3]>=b if e[2]else e[3]<=a):return e[3]
 elif not ic:
  best=(EV[0]*PH+EV[1]*(24-PH))//24*S
  if best>=b:return best
  a=max(a,best)
 sv=(B[:],S,EV[:],PH,KS[:])
 for m in sorted(gn(0 if ic or d>0 else 1),key=lambda m:-(9000000 if m==tm else 8000000+v*-S*32-B[m&127]*S if(v:=B[m>>7&127])else 7000000*(m==KL[ply]))):
  mk(m)
  if at(KS[-S<0],S):RS(sv);continue
  sc=-sr(max(d-1,0),-b,-a,ply+1);RS(sv)
  if sc>best:
   best=sc;bm=m
   if ply==0:N[1]=m
   if sc>a:
    a=sc
    if a>=b:
     if not B[m>>7&127]:KL[ply]=m
     break
 if bm<0:return-9999 if ic else 0 if d>0 else best
 if d>0:TT[k0]=(bm,d,best>=b,best)
 return best
for f,p in enumerate([4,2,3,5,6,3,2,4]):
 B[f]=p;B[16+f]=1;B[96+f]=-1;B[112+f]=-p
KS[:]=[4,116];PH=24;B[120]=15
SN=(B[:],S,EV[:],PH,KS[:])
SQ=["abcdefgh"[i&7]+chr(49+(i>>4))for i in range(120)]
def post(p,b):return json.load(UQ.urlopen(URL+p,json.dumps(b).encode()))
if __name__=="__main__":
 URL=os.environ["MAKEFUN_ENV_URL"]
 while 1:
  g=post("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   RS(SN)
   for u in g["moves"]:mk(SQ.index(u[:2])|SQ.index(u[2:4])<<7|(len(u)>4 and("nbrq".index(u[4])+2)<<14))
   TT.clear()
   N[:]=[0,0]
   try:
    for d in range(80):sr(d,-1e5,1e5,0)
   except:pass
   m=N[1];f=m&127;t=m>>7&127
   u=SQ[f]+SQ[t]+("nbrq"[(m>>14)-2]if m>>14 else"")
   if u not in g["legal_moves"]:u=g["legal_moves"][0]
   g=post("/move",{"game":g["game"],"move":u})
