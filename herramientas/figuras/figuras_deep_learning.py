import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
OUT="assets/img/"
AZ,NA,VE,GR,RO,MO="#2563eb","#ea580c","#16a34a","#6b7280","#dc2626","#7c3aed"
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
def save(f,n): f.tight_layout(); f.savefig(OUT+n,dpi=100,facecolor="white"); plt.close(f); print("ok",n)
def caja(ax,x,y,w,h,t,c,fs=10):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.12",fc=c,ec="black")); ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs)
def flecha(ax,a,b,c="black",ls="-"): ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=14,lw=1.4,color=c,ls=ls))

# 1. Activaciones y derivadas
from math import erf
z=np.linspace(-4,4,400); sig=1/(1+np.exp(-z)); gelu=0.5*z*(1+np.vectorize(erf)(z/np.sqrt(2)))
F={"sigmoide":(sig,sig*(1-sig),AZ),"tanh":(np.tanh(z),1-np.tanh(z)**2,VE),"ReLU":(np.maximum(0,z),(z>0).astype(float),NA),"Leaky ReLU (0,1)":(np.where(z>0,z,.1*z),np.where(z>0,1,.1),MO),"GELU":(gelu,np.gradient(gelu,z),RO)}
f,axs=plt.subplots(1,2,figsize=(11,3.8))
for n,(y,d,c) in F.items(): axs[0].plot(z,y,c=c,lw=2,label=n); axs[1].plot(z,d,c=c,lw=2,label=n)
axs[0].set_ylim(-1.5,3); axs[0].set_title("Funciones de activación"); axs[1].set_title("Sus derivadas: lo que pasa hacia atrás")
axs[1].axhline(.25,ls=":",c=GR); axs[1].text(-4,.3,"máximo de la sigmoide: 0,25",color=GR,fontsize=9)
for a in axs: a.axhline(0,c="black",lw=.5); a.axvline(0,c="black",lw=.5); a.set_xlabel("z")
axs[0].legend(fontsize=9); save(f,"dl_activaciones.png")

# 2. Optimizadores
g=lambda p: np.array([2*p[0],20*p[1]]); fz=lambda x,y: x**2+10*y**2
def run(kind,steps=40):
    p=np.array([-4.5,1.6]); v=np.zeros(2); m=np.zeros(2); s=np.zeros(2); P=[p.copy()]
    for t in range(1,steps+1):
        gr=g(p)
        if kind=="SGD": p=p-0.09*gr
        elif kind=="Momento": v=0.8*v+gr; p=p-0.02*v
        else:
            m=.9*m+.1*gr; s=.999*s+.001*gr**2; p=p-0.2*(m/(1-.9**t))/(np.sqrt(s/(1-.999**t))+1e-8)
        P.append(p.copy())
    return np.array(P)
X,Y=np.meshgrid(np.linspace(-5,5,200),np.linspace(-2,2,200))
f,ax=plt.subplots(figsize=(9,4)); ax.contour(X,Y,fz(X,Y),levels=15,colors=GR,linewidths=.6)
for k,c in [("SGD",AZ),("Momento",NA),("Adam",VE)]:
    P=run(k); ax.plot(P[:,0],P[:,1],"o-",ms=3,c=c,label=f"{k}: pérdida final {fz(*P[-1]):.3f}")
ax.plot(0,0,"*",ms=16,c="black"); ax.set_title("40 pasos hacia el mínimo (★) en un valle alargado: f = x² + 10·y²\nzigzag de SGD, inercia del momento, pasos «a medida» de Adam (con estas tasas; no hay ganador universal)"); ax.legend(fontsize=9,loc="lower right"); ax.set_aspect("equal")
save(f,"dl_optimizadores.png")

# 3. Dropout
def red(ax,drop,title):
    capas=[3,5,5,2]; pos={}
    for i,n in enumerate(capas):
        for j in range(n): pos[(i,j)]=(i*2.2,(j-(n-1)/2)*1.0)
    for i in range(3):
        for a in range(capas[i]):
            for b in range(capas[i+1]):
                off=(i,a) in drop or (i+1,b) in drop
                ax.plot(*zip(pos[(i,a)],pos[(i+1,b)]),c="#d1d5db" if off else GR,lw=.8,ls=":" if off else "-")
    for k,(x,y) in pos.items():
        off=k in drop; ax.add_patch(Circle((x,y),.3,fc="white" if off else "#bfdbfe",ec="#9ca3af" if off else "black"))
        if off: ax.text(x,y,"×",ha="center",va="center",color=RO,fontsize=16)
    ax.set_title(title); ax.set_xlim(-.6,7.2); ax.set_ylim(-3,3); ax.set_aspect("equal"); ax.axis("off")
f,axs=plt.subplots(1,3,figsize=(12,3.8))
red(axs[0],{(1,1),(1,4),(2,2)},"Entrenamiento, lote 1")
red(axs[1],{(1,0),(1,3),(2,0),(2,4)},"Entrenamiento, lote 2")
red(axs[2],set(),"Predicción: todas activas")
f.suptitle("Dropout (p = 0,4): cada lote apaga neuronas al azar, y ninguna puede «depender» de otra",y=1.0); save(f,"dl_dropout.png")

# 4. Generativos
f,axs=plt.subplots(3,1,figsize=(10,7.2))
for ax in axs: ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,2)
ax=axs[0]; caja(ax,0,.6,1.3,.8,"x\nimagen","#e5e7eb"); caja(ax,2,.6,1.6,.8,"Codificador","#bfdbfe"); caja(ax,4.4,.7,.9,.6,"z\n8 nº","#fde68a"); caja(ax,6,.6,1.6,.8,"Decodificador","#bfdbfe"); caja(ax,8.3,.6,1.4,.8,"x̂\nreconstruida","#e5e7eb")
for a,b in [((1.3,1),(2,1)),((3.6,1),(4.4,1)),((5.3,1),(6,1)),((7.6,1),(8.3,1))]: flecha(ax,a,b)
ax.set_title("Autoencoder: comprimir y reconstruir. Pérdida = diferencia entre x y x̂",loc="left")
ax=axs[1]; caja(ax,0,.6,1.3,.8,"x","#e5e7eb"); caja(ax,2,.6,1.6,.8,"Codificador","#bfdbfe"); caja(ax,4.1,1.1,1.0,.55,"μ  media","#fde68a",9); caja(ax,4.1,.35,1.0,.55,"σ  desv.","#fde68a",9)
caja(ax,5.6,.6,1.6,.8,"z = μ + σ·ε\nε al azar","#fed7aa",9); caja(ax,7.6,.6,1.4,.8,"Decodificador → x̂","#bfdbfe",9)
for a,b in [((1.3,1),(2,1)),((3.6,1.2),(4.1,1.35)),((3.6,.8),(4.1,.62)),((5.1,1.3),(5.6,1.1)),((5.1,.62),(5.6,.85)),((7.2,1),(7.6,1))]: flecha(ax,a,b)
ax.set_title("VAE: el código es una nube de probabilidad. Para generar, se toma un z al azar y se decodifica",loc="left")
ax=axs[2]; caja(ax,0,.6,1.2,.8,"ruido z","#fde68a"); caja(ax,1.8,.6,1.6,.8,"Generador","#bbf7d0"); caja(ax,4,.95,1.5,.55,"falsa","#fecaca",9); caja(ax,4,.15,1.5,.55,"real (datos)","#e5e7eb",9)
caja(ax,6.2,.6,1.8,.8,"Discriminador","#ddd6fe"); caja(ax,8.6,.6,1.3,.8,"¿real o\nfalsa?","#e5e7eb",9)
for a_,b_ in [((1.2,1),(1.8,1)),((3.4,1.1),(4,1.2)),((5.5,1.2),(6.2,1.1)),((5.5,.45),(6.2,.8)),((8,1),(8.6,1))]: flecha(ax,a_,b_)
ax.add_patch(FancyArrowPatch((7.1,1.4),(2.6,1.4),connectionstyle="arc3,rad=0.2",arrowstyle="-|>",mutation_scale=14,lw=1.4,color=RO,ls="--"))
ax.text(4.85,2.12,"el error del discriminador enseña al generador a engañarlo mejor",ha="center",color=RO,fontsize=9)
ax.set_ylim(0,2.3)
ax.set_title("GAN: dos redes compiten; el generador nunca ve las imágenes reales",loc="left")
save(f,"dl_generativos.png")

# 5. Transferencia
f,ax=plt.subplots(figsize=(10,3.6)); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,3.6)
ax.text(0,3.3,"1 · Modelo preentrenado (millones de fotos, 1000 clases)",weight="bold")
for i,(t,c) in enumerate([("bordes","#bfdbfe"),("texturas","#bfdbfe"),("partes","#bfdbfe"),("objetos","#bfdbfe"),("1000 clases","#fecaca")]):
    caja(ax,0.2+i*1.5,2.2,1.3,.7,t,c,9)
ax.text(0,1.5,"2 · Reutilizar en el aula (pocas fotos: «reciclable» o «no»)",weight="bold")
for i,(t,c) in enumerate([("bordes\n(congelada)","#e5e7eb"),("texturas\n(congelada)","#e5e7eb"),("partes\n(congelada)","#e5e7eb"),("objetos\n(congelada)","#e5e7eb"),("2 clases (nueva)","#bbf7d0")]):
    caja(ax,0.2+i*1.5,.4,1.3,.7,t,c,9)
ax.text(7.9,2.55,"se quita la última capa",fontsize=9,color=RO); ax.text(7.9,.75,"solo se entrena esta;\nluego, si hace falta,\najuste fino con tasa baja",fontsize=9,color=VE)
ax.text(3.2,0.05,"congelada = no se entrena: conserva lo aprendido",ha="center",color=GR,fontsize=9)
save(f,"dl_transferencia.png")

# 6. RNN desenrollada
f,ax=plt.subplots(figsize=(10,3.2)); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,3.2)
pal=["El","gato","come","pescado"]
for i,w in enumerate(pal):
    x=1+i*2.2; caja(ax,x,1.2,1.2,.8,f"h{'₁₂₃₄'[i]}","#bfdbfe"); ax.text(x+.6,.3,f"x{'₁₂₃₄'[i]} = «{w}»",ha="center",fontsize=9)
    flecha(ax,(x+.6,.55),(x+.6,1.2)); flecha(ax,(x+.6,2),(x+.6,2.6)); ax.text(x+.6,2.8,f"y{'₁₂₃₄'[i]}",ha="center",fontsize=9)
    if i<3: flecha(ax,(x+1.2,1.6),(x+2.2,1.6),c=NA)
ax.text(0.1,1.6,"h₀ →",va="center"); ax.text(5.5,0.0,"la misma red (los mismos pesos) en cada paso; la flecha naranja es la memoria",ha="center",color=GR,fontsize=9)
save(f,"dl_rnn_desenrollada.png")
