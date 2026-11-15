import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, FancyArrowPatch
OUT="assets/img/"   # ejecutar desde la raíz del repositorio
AZ,NA,VE,GR,RO,MO="#2563eb","#ea580c","#16a34a","#6b7280","#dc2626","#7c3aed"
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
def save(f,n): f.tight_layout(); f.savefig(OUT+n,dpi=100,facecolor="white"); plt.close(f); print("ok",n)
def caja(ax,x,y,w,h,t,c,fs=11):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.15",fc=c,ec="black",alpha=.9)); ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs)
def flecha(ax,a,b,**k): ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=16,lw=1.5,**k))

# UD1 · capas de la IA
f,ax=plt.subplots(figsize=(8,5.2)); ax.axis("off"); ax.set_aspect("equal")
for r,c,t,y in [(4,"#dbeafe","Inteligencia artificial\nbuscar, razonar, planificar, aprender",3.1),(3,"#bfdbfe","Aprendizaje automático (ML)\naprende de datos",2.0),(2,"#93c5fd","Aprendizaje profundo\nredes neuronales de muchas capas",1.0),(1,"#60a5fa","IA generativa\ncrea texto e imágenes",0.0)]:
    ax.add_patch(Circle((0,r-4),r,fc=c,ec="#1e3a8a")); ax.text(0,y-4+ (0.35 if r==1 else 0)+ (r-1)*0.0,t,ha="center",va="center",fontsize=10)
ax.text(5,-1,"Ejemplos\n• A* en un GPS, ajedrez clásico\n• filtro de spam, recomendador\n• reconocer caras, traducir\n• ChatGPT, generar imágenes",fontsize=10,va="center")
ax.set_xlim(-4.3,9); ax.set_ylim(-8.3,0.3); save(f,"ud1_capas_ia.png")

# UD1 · historia
f,ax=plt.subplots(figsize=(10,3.4))
ev=[(1950,"Test de Turing"),(1956,"Dartmouth:\nnace «IA»"),(1966,"ELIZA"),(1997,"Deep Blue\ngana a Kaspárov"),(2012,"AlexNet:\nvisión profunda"),(2016,"AlphaGo"),(2017,"Transformer"),(2022,"ChatGPT")]
for a,b,t in [(1974,1980,"1.er invierno"),(1987,1993,"2.º invierno")]: ax.axvspan(a,b,color="#bfdbfe",alpha=.7); ax.text((a+b)/2,1.5,t,ha="center",color="#1e3a8a")
ax.axhline(0,color="black",lw=1.5)
for k,(y,t) in enumerate(ev):
    h=0.9 if k%2==0 else -0.9; ax.plot([y,y],[0,h*0.8],c=GR,lw=1); ax.plot(y,0,"o",c=NA); ax.text(y,h,f"{y}\n{t}",ha="center",va="center",fontsize=9)
ax.set_xlim(1945,2027); ax.set_ylim(-1.7,1.9); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.set_title("Veranos e inviernos de la IA (las franjas azules son épocas de poca financiación)")
save(f,"ud1_historia.png")

# UD1 · pirámide DIKW
f,ax=plt.subplots(figsize=(8,4.2)); ax.axis("off")
niv=[("Datos","22, 25, 31, 19 (°C)","#dbeafe"),("Información","temperatura en Marín a las 12 h, de lunes a jueves","#bfdbfe"),("Conocimiento","el miércoles fue el día más caluroso; la tendencia sube","#93c5fd"),("Decisión","mañana, abrir las ventanas del aula antes","#60a5fa")]
for i,(n,e,c) in enumerate(niv):
    w=8-i*1.6; ax.add_patch(plt.Polygon([(-w/2,i),(w/2,i),(w/2-0.8,i+1),(-w/2+0.8,i+1)],fc=c,ec="#1e3a8a")); ax.text(0,i+.5,n,ha="center",va="center",fontsize=12,weight="bold"); ax.text(4.5,i+.5,e,va="center",fontsize=9.5)
ax.annotate("",xy=(-4.6,4),xytext=(-4.6,0),arrowprops=dict(arrowstyle="->",lw=2)); ax.text(-4.8,2,"más contexto\ny más valor",ha="right",va="center",fontsize=9)
ax.set_xlim(-6.5,11.5); ax.set_ylim(-.2,4.2); save(f,"ud1_dikw.png")

# UD1 · agente
f,ax=plt.subplots(figsize=(8,3.6)); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,4)
caja(ax,0.3,1.3,2.4,1.4,"ENTORNO\ncarretera, peatones,\nsemáforos","#e5e7eb")
caja(ax,4,2.6,2.2,1.0,"Sensores\ncámara, radar","#bbf7d0"); caja(ax,7.4,1.3,2.3,1.4,"Decidir\nreglas o modelo\naprendido","#ddd6fe"); caja(ax,4,0.3,2.2,1.0,"Actuadores\nvolante, freno","#fed7aa")
flecha(ax,(2.7,2.4),(4,3.1)); ax.text(3.1,3.2,"percepción",fontsize=9); flecha(ax,(6.2,3.1),(7.4,2.4)); flecha(ax,(7.4,1.6),(6.2,0.8)); flecha(ax,(4,0.8),(2.7,1.6)); ax.text(2.9,0.6,"acción",fontsize=9)
ax.text(5,1.95,"el bucle se repite\nmuchas veces por segundo",ha="center",fontsize=9,color=GR); save(f,"ud1_agente.png")

# UD1 · descenso del gradiente
f,axs=plt.subplots(1,2,figsize=(10,3.8)); x=np.linspace(-1,7,200); L=lambda w:(w-3)**2+1
for ax,lr,t in [(axs[0],0.3,"tasa 0,3: baja hacia el mínimo"),(axs[1],1.05,"tasa 1,05: se pasa y diverge")]:
    ax.plot(x,L(x),c=GR); w=0.0; pts=[w]
    for _ in range(6): w=w-lr*2*(w-3); pts.append(w)
    pts=np.array(pts); ax.plot(pts,L(pts),"o-",c=NA); ax.plot(3,1,"*",ms=15,c=VE)
    ax.set_title(t); ax.set_xlabel("peso w"); ax.set_ylim(0,30)
axs[0].set_ylabel("error (pérdida)"); save(f,"ud1_gradiente.png")

# Datos · Anscombe
xs=[10,8,13,9,11,14,6,4,12,7,5]
A=[(xs,[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]),(xs,[9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]),(xs,[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]),([8]*7+[19]+[8]*3,[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89])]
f,axs=plt.subplots(1,4,figsize=(12,3.2),sharey=True)
for i,(ax,(x_,y_)) in enumerate(zip(axs,A)):
    x_,y_=np.array(x_,float),np.array(y_); m,b=np.polyfit(x_,y_,1)
    ax.scatter(x_,y_,c=AZ); g=np.linspace(3,20,10); ax.plot(g,m*g+b,c=NA)
    ax.set_title(f"media y = {y_.mean():.2f}\nr = {np.corrcoef(x_,y_)[0,1]:.2f}",fontsize=10); ax.set_xlabel(["I","II","III","IV"][i])
save(f,"datos_anscombe.png")

# Datos · tipos de gráfico
rng=np.random.default_rng(3); notas=np.clip(rng.normal(6.2,1.6,120),0,10)
f,axs=plt.subplots(1,4,figsize=(13,3.3))
axs[0].hist(notas,bins=10,color=AZ,ec="white"); axs[0].set_title("Histograma\n¿cómo se reparten?"); axs[0].set_xlabel("nota")
bp=axs[1].boxplot([notas[:40],notas[40:80],notas[80:]+.8],tick_labels=["1A","1B","1C"],patch_artist=True)
for p in bp["boxes"]: p.set_facecolor("#bfdbfe")
axs[1].set_title("Caja y bigotes\n¿comparar grupos?"); q1,q2,q3=np.percentile(notas[:40],[25,50,75])
axs[1].annotate("mediana",xy=(1.25,q2),xytext=(1.5,9.5),fontsize=8,arrowprops=dict(arrowstyle="->"))
h=rng.uniform(0,10,60); axs[2].scatter(h,np.clip(3+0.5*h+rng.normal(0,1,60),0,10),c=NA,s=15); axs[2].set_title("Dispersión\n¿se relacionan?"); axs[2].set_xlabel("horas de estudio")
axs[3].bar(["bus","pie","bici","coche"],[42,31,9,18],color=VE); axs[3].set_title("Barras\n¿comparar categorías?"); axs[3].set_ylabel("%")
save(f,"datos_tipos_grafico.png")

# Datos · escalado
X=np.c_[rng.uniform(150,195,40),rng.uniform(0,6,40)]
from sklearn.preprocessing import StandardScaler, MinMaxScaler
f,axs=plt.subplots(1,3,figsize=(12,3.4))
for ax,(Z,t) in zip(axs,[(X,"Original: altura (cm) y horas"),(MinMaxScaler().fit_transform(X),"MinMaxScaler: de 0 a 1"),(StandardScaler().fit_transform(X),"StandardScaler: media 0, desv. 1")]):
    ax.scatter(Z[:,0],Z[:,1],c=AZ,s=15); ax.set_title(t,fontsize=10); ax.set_aspect("equal","datalim")
save(f,"datos_escalado.png")

# UD3 · imagen como matriz
img=np.zeros((8,8,3)); yy,xx=np.mgrid[:8,:8]; img[...,0]=(xx/7); img[...,2]=(yy/7); img[2:6,2:6,1]=0.9
img8=(img*255).astype(int)
f,axs=plt.subplots(1,4,figsize=(13,3.4))
axs[0].imshow(img8.astype(np.uint8)); axs[0].set_title("Imagen 8 × 8 píxeles")
for k,(n,cm) in enumerate([("R (rojo)","Reds"),("G (verde)","Greens"),("B (azul)","Blues")]):
    ax=axs[k+1]; ax.imshow(img8[...,k],cmap=cm,vmin=0,vmax=255); ax.set_title(f"Canal {n}")
    for i in range(0,8,2):
        for j in range(0,8,2): ax.text(j,i,img8[i,j,k],ha="center",va="center",fontsize=7,color="black" if img8[i,j,k]<150 else "white")
for ax in axs: ax.set_xticks([]); ax.set_yticks([])
f.suptitle("Una imagen en color es un array de forma (alto, ancho, 3) con números de 0 a 255",y=1.0); save(f,"ud3_imagen_matriz.png")

# UD3 · convolución
from scipy.signal import convolve2d
g=np.zeros((40,40)); g[10:30,10:30]=1; g[18:22,:]=.5
K=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
f,axs=plt.subplots(1,4,figsize=(12,3.2))
axs[0].imshow(g,cmap="gray"); axs[0].set_title("Original")
axs[1].imshow(K,cmap="coolwarm",vmin=-2,vmax=2)
for i in range(3):
    for j in range(3): axs[1].text(j,i,K[i,j],ha="center",va="center",fontsize=13)
axs[1].set_title("Filtro (Sobel x)")
axs[2].imshow(np.abs(convolve2d(g,K,mode="same")),cmap="gray"); axs[2].set_title("Bordes verticales")
axs[3].imshow(convolve2d(g,np.ones((5,5))/25,mode="same"),cmap="gray"); axs[3].set_title("Desenfoque (media 5×5)")
for ax in axs: ax.set_xticks([]); ax.set_yticks([])
save(f,"ud3_convolucion.png")

# UD3 · IoU
f,axs=plt.subplots(1,3,figsize=(11,3.3))
for ax,(b,t) in zip(axs,[((1,1),"IoU = 0,47 · aceptable"),((2.2,2.2),"IoU = 0,08 · mala"),((0.2,0.2),"IoU = 0,82 · muy buena")]):
    r=(0,0,4,4); p=(b[0],b[1],4,4)
    ax.add_patch(Rectangle(r[:2],4,4,fill=False,ec=VE,lw=3,label="real")); ax.add_patch(Rectangle(p[:2],4,4,fill=False,ec=NA,lw=3,ls="--",label="predicha"))
    ix=max(0,min(4,b[0]+4)-max(0,b[0])); iy=max(0,min(4,b[1]+4)-max(0,b[1])); inter=ix*iy; iou=inter/(32-inter)
    ax.add_patch(Rectangle((max(0,b[0]),max(0,b[1])),ix,iy,fc=MO,alpha=.35)); ax.set_title(f"IoU = {iou:.2f}"); ax.set_xlim(-1,7.5); ax.set_ylim(-1,7.5); ax.set_aspect("equal"); ax.axis("off")
axs[0].legend(loc="upper right",fontsize=9)
f.suptitle("IoU = área común (morado) / área total de las dos cajas",y=1.0); save(f,"ud3_iou.png")

# UD4 · temperatura
logit=np.array([3.0,2.2,1.5,0.5,-0.5]); pal=["patio","biblioteca","gimnasio","cafetería","tejado"]
f,axs=plt.subplots(1,3,figsize=(12,3.3),sharey=True)
for ax,T in zip(axs,[0.5,1.0,2.0]):
    p=np.exp(logit/T); p/=p.sum(); ax.bar(pal,p,color=AZ); ax.set_title(f"temperatura {T}"); ax.tick_params(axis="x",rotation=35)
    for i,v in enumerate(p): ax.text(i,v+.01,f"{v:.2f}",ha="center",fontsize=8)
axs[0].set_ylabel("probabilidad de la\nsiguiente palabra"); f.suptitle("«El recreo de hoy será en el …»: baja temperatura = más predecible; alta = más variado",y=1.0); save(f,"ud4_temperatura.png")

# UD4 · embeddings (ilustrativo)
pts={"rey":(4,4),"reina":(4,1.6),"hombre":(1.2,3.6),"mujer":(1.2,1.2),"gato":(-3,-2.6),"can":(-2.5,-3.4),"perro":(-2.1,-2.4),"Vigo":(5,-3),"Marín":(5.8,-3.6),"Pontevedra":(6.2,-2.6)}
f,ax=plt.subplots(figsize=(7.5,5))
for w,(x,y) in pts.items(): ax.scatter(x,y,c=AZ); ax.annotate(w,(x,y),xytext=(5,4),textcoords="offset points")
for a,b in [("hombre","mujer"),("rey","reina")]: ax.annotate("",xy=pts[b],xytext=pts[a],arrowprops=dict(arrowstyle="->",color=NA,lw=2))
ax.text(4.2,2.8,"misma dirección:\n«masculino → femenino»",color=NA,fontsize=9)
ax.set_title("Mapa de embeddings (ilustrativo, 2 dimensiones)\nlas palabras parecidas quedan cerca"); ax.set_xticks([]); ax.set_yticks([]); save(f,"ud4_embeddings.png")

# UD4 · máscara causal
tok=["El","gato","come","pescado"]; rng2=np.random.default_rng(1); S=rng2.normal(0,1,(4,4))
M=np.triu(np.ones((4,4)),1).astype(bool); S[M]=-np.inf; W=np.exp(S-S.max(1,keepdims=True)); W/=W.sum(1,keepdims=True)
f,ax=plt.subplots(figsize=(5.2,4.3)); ax.imshow(W,cmap="Blues",vmin=0,vmax=1)
for i in range(4):
    for j in range(4): ax.text(j,i,"—" if M[i,j] else f"{W[i,j]:.2f}",ha="center",va="center",color="black")
ax.set_xticks(range(4),tok); ax.set_yticks(range(4),tok); ax.set_xlabel("palabra a la que mira"); ax.set_ylabel("palabra que se calcula"); ax.set_title("Atención con máscara causal\ncada fila suma 1; no se mira al futuro"); ax.spines[:].set_visible(False)
save(f,"ud4_atencion_causal.png")

# UD5 · sobreajuste
from sklearn.pipeline import make_pipeline; from sklearn.preprocessing import PolynomialFeatures; from sklearn.linear_model import LinearRegression
x=np.sort(rng.uniform(0,1,15)); y=np.sin(2*np.pi*x)+rng.normal(0,.25,15); g=np.linspace(0,1,300)
f,axs=plt.subplots(1,3,figsize=(12,3.4),sharey=True)
for ax,d,t in zip(axs,[1,4,14],["grado 1: subajuste","grado 4: equilibrio","grado 14: sobreajuste"]):
    m=make_pipeline(PolynomialFeatures(d),LinearRegression()).fit(x[:,None],y)
    ax.scatter(x,y,c=AZ,zorder=3); ax.plot(g,m.predict(g[:,None]),c=NA); ax.plot(g,np.sin(2*np.pi*g),c=GR,ls=":",label="regla real"); ax.set_ylim(-2,2); ax.set_title(t)
axs[0].legend(fontsize=9); save(f,"ud5_sobreajuste.png")

# UD5 · validación cruzada
f,ax=plt.subplots(figsize=(9,3.2)); ax.axis("off")
for i in range(5):
    for j in range(5):
        caja(ax,1.6+j*1.5,4-i*0.85,1.4,0.7,"prueba" if i==j else "entrena","#fed7aa" if i==j else "#bfdbfe",9)
    ax.text(0.2,4.35-i*0.85,f"Ronda {i+1}",va="center"); ax.text(9.3,4.35-i*0.85,f"→ nota {['0,84','0,88','0,81','0,86','0,85'][i]}",va="center")
ax.text(5.3,-0.3,"Resultado: media 0,85 ± desviación (5 particiones; cada dato se usa una vez para probar)",ha="center",color=GR)
ax.set_xlim(0,11.5); ax.set_ylim(-0.6,4.9); save(f,"ud5_validacion_cruzada.png")

# UD5 · matriz de confusión y ROC
from sklearn.datasets import load_breast_cancer; from sklearn.linear_model import LogisticRegression; from sklearn.model_selection import train_test_split; from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
Xb,yb=load_breast_cancer(return_X_y=True); Xtr,Xte,ytr,yte=train_test_split(Xb,yb,test_size=.3,random_state=0,stratify=yb)
mdl=make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000)).fit(Xtr,ytr); pr=mdl.predict_proba(Xte)[:,1]
cm=confusion_matrix(yte,pr>.5); f,axs=plt.subplots(1,2,figsize=(10,4))
ax=axs[0]; ax.imshow(cm,cmap="Blues")
nm=[["VN","FP"],["FN","VP"]]
for i in range(2):
    for j in range(2): ax.text(j,i,f"{nm[i][j]}\n{cm[i,j]}",ha="center",va="center",fontsize=13,color="white" if cm[i,j]>60 else "black")
ax.set_xticks([0,1],["pred. maligno","pred. benigno"]); ax.set_yticks([0,1],["real maligno","real benigno"]); ax.set_title("Matriz de confusión (umbral 0,5)"); ax.spines[:].set_visible(False)
fpr,tpr,th=roc_curve(yte,pr); ax=axs[1]; ax.plot(fpr,tpr,c=AZ,lw=2,label=f"modelo (AUC = {roc_auc_score(yte,pr):.3f})"); ax.plot([0,1],[0,1],ls="--",c=GR,label="azar (AUC = 0,5)")
ax.set_xlabel("tasa de falsos positivos"); ax.set_ylabel("exhaustividad (tasa de verdaderos positivos)"); ax.set_title("Curva ROC: cada punto es un umbral"); ax.legend(loc="lower right",fontsize=9)
save(f,"ud5_confusion_roc.png"); print(cm.tolist(), round(roc_auc_score(yte,pr),3))

# UD5 · k-means pasos
from sklearn.datasets import make_blobs
P,_=make_blobs(150,centers=[(0,0),(4,4),(0,5)],cluster_std=.8,random_state=2); C=np.array([[3.0,0.0],[3.5,1.0],[4.0,0.5]])
f,axs=plt.subplots(1,4,figsize=(13,3.3),sharey=True); cols=np.array([AZ,NA,VE])
for k,ax in enumerate(axs):
    lab=((P[:,None,:]-C[None])**2).sum(2).argmin(1)
    ax.scatter(*P.T,c=cols[lab] if k>0 else GR,s=10); ax.scatter(*C.T,c="black",marker="X",s=150); ax.set_title(["0: centros al azar","1: asignar y mover","2: asignar y mover","3: casi no se mueven"][k])
    C=np.array([P[lab==i].mean(0) for i in range(3)])
save(f,"ud5_kmeans_pasos.png")

# UD5 · neurona
f,ax=plt.subplots(figsize=(9,3.8)); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,4)
for i,(n,w) in enumerate([("x₁ horas de estudio","w₁ = 0,8"),("x₂ horas de sueño","w₂ = 0,5"),("x₃ horas de móvil","w₃ = −0,6")]):
    y=3.3-i*1.2; ax.add_patch(Circle((1.2,y),.32,fc="#bfdbfe",ec="black")); ax.text(0.8,y,n,ha="right",va="center",fontsize=9); flecha(ax,(1.52,y),(4.3,2.0)); ax.text(2.2,y-(y-2)*0.3+0.18,w,fontsize=9,color=NA)
ax.add_patch(Circle((4.8,2),.55,fc="#ddd6fe",ec="black")); ax.text(4.8,2,"Σ + b",ha="center",va="center")
flecha(ax,(5.35,2),(6.5,2)); caja(ax,6.5,1.5,1.6,1,"activación\nsigmoide","#fed7aa",9); flecha(ax,(8.1,2),(8.9,2)); ax.text(9.0,2,"ŷ\n0,0–1,0",va="center")
ax.text(4.8,0.4,"z = w₁x₁ + w₂x₂ + w₃x₃ + b      ŷ = 1 / (1 + e⁻ᶻ)",ha="center",family="DejaVu Sans")
save(f,"ud5_neurona.png")
