import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
OUT="assets/img/"   # ejecutar desde la raíz del repositorio
AZ,NA,VE,GR,RO="#2563eb","#ea580c","#16a34a","#6b7280","#dc2626"
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False,"font.family":"DejaVu Sans"})
def save(f,n): f.tight_layout(); f.savefig(OUT+n,dpi=100,facecolor="white"); plt.close(f)

# 1. Broadcasting
def grid(ax,x0,y0,vals,col,ghost=None):
    r,c=vals.shape
    for i in range(r):
        for j in range(c):
            g = ghost is not None and ghost[i,j]
            ax.add_patch(Rectangle((x0+j,y0-i),1,1,fc=col,ec="black",alpha=.25 if g else .8,ls="--" if g else "-"))
            ax.text(x0+j+.5,y0-i+.5,str(vals[i,j]),ha="center",va="center",color="black",alpha=.5 if g else 1)
f,ax=plt.subplots(figsize=(9,3.4))
a=np.array([[0],[10],[20]]); b=np.array([[1,2,3,4]])
A=np.repeat(a,4,1); B=np.repeat(b,3,0)
gA=np.ones((3,4),bool); gA[:,0]=False; gB=np.ones((3,4),bool); gB[0]=False
grid(ax,0,2,A,AZ,gA); ax.text(2,3.3,"a: forma (3, 1)",ha="center")
ax.text(4.6,1.5,"+",fontsize=22,ha="center",va="center")
grid(ax,5.2,2,B,NA,gB); ax.text(7.2,3.3,"b: forma (4,)",ha="center")
ax.text(9.8,1.5,"=",fontsize=22,ha="center",va="center")
grid(ax,10.4,2,A+B,VE); ax.text(12.4,3.3,"a + b: forma (3, 4)",ha="center")
ax.text(6.7,-1.6,"Lo punteado no existe en memoria: NumPy «estira» las dimensiones de tamaño 1",ha="center",color=GR)
ax.set_xlim(-.3,14.7); ax.set_ylim(-2,3.7); ax.axis("off"); save(f,"numpy_broadcasting.png")

# 2. Vistas y copias
f,ax=plt.subplots(figsize=(9,3.2)); ax.axis("off"); ax.set_xlim(0,12); ax.set_ylim(0,4.4)
for k,v in enumerate([1,2,3,4,5,6]):
    ax.add_patch(Rectangle((3+k,2.4),1,.9,fc=AZ,alpha=.75,ec="black")); ax.text(3.5+k,2.85,str(v),ha="center",va="center")
ax.text(1.4,2.85,"memoria",ha="center",color=GR)
ax.text(1.4,4.0,"a = np.arange(1, 7)",ha="center",family="monospace")
ax.annotate("",xy=(3,3.3),xytext=(2.6,3.9),arrowprops=dict(arrowstyle="->"))
ax.text(4.6,4.05,"v = a[1:4]   (vista)",family="monospace",color=VE)
ax.add_patch(Rectangle((4,2.35),3,1.0,fill=False,ec=VE,lw=3))
for k,v in enumerate([2,3,4]):
    ax.add_patch(Rectangle((7+k,0.4),1,.9,fc=NA,alpha=.75,ec="black")); ax.text(7.5+k,0.85,str(v),ha="center",va="center")
ax.text(3.6,0.85,"c = a[[1, 2, 3]]   (copia)",family="monospace",color=NA)
ax.text(6,1.75,"v[0] = 99 cambia también a[1];   c[0] = 99 no toca a",ha="center",color=GR)
save(f,"numpy_vistas.png")

# 3. Árbol del recreo
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
d=pd.DataFrame({"cielo":["sol","sol","nubes","lluvia","lluvia","nubes","sol","lluvia"],"viento":["poco","mucho","poco","mucho","mucho","mucho","poco","poco"],"patio":["sí","sí","sí","no","no","sí","sí","sí"]})
X=pd.get_dummies(d[["cielo","viento"]]).astype(int)
t=DecisionTreeClassifier(criterion="entropy",random_state=0).fit(X,d["patio"])
f,ax=plt.subplots(figsize=(9,4.2))
plot_tree(t,feature_names=list(X.columns),class_names=list(t.classes_),filled=True,impurity=True,proportion=False,ax=ax,fontsize=10)
save(f,"arbol_recreo.png")

# 4. SVM margen + truco del núcleo
from sklearn.svm import SVC
rng=np.random.default_rng(1)
P=np.r_[rng.normal([2,2],.5,(15,2)),rng.normal([4.5,4.5],.5,(15,2))]; yy=np.r_[np.zeros(15),np.ones(15)]
s=SVC(kernel="linear",C=100).fit(P,yy)
f,axs=plt.subplots(1,2,figsize=(10,4))
ax=axs[0]; ax.scatter(*P[yy==0].T,c=AZ,label="clase A"); ax.scatter(*P[yy==1].T,c=NA,marker="s",label="clase B")
xx,yy2=np.meshgrid(np.linspace(0,6.5,200),np.linspace(0,6.5,200))
Z=s.decision_function(np.c_[xx.ravel(),yy2.ravel()]).reshape(xx.shape)
ax.contour(xx,yy2,Z,levels=[-1,0,1],colors=["gray","black","gray"],linestyles=["--","-","--"])
ax.scatter(*s.support_vectors_.T,s=200,facecolors="none",edgecolors=VE,linewidths=2,label="vectores de soporte")
ax.set_title("Frontera con el mayor margen"); ax.legend(fontsize=9,loc="upper left"); ax.set_xlabel("x₁"); ax.set_ylabel("x₂")
ang=rng.uniform(0,2*np.pi,60); r=np.r_[rng.uniform(0,1,30),rng.uniform(1.8,2.6,30)]
C=np.c_[r*np.cos(ang),r*np.sin(ang)]; cl=np.r_[np.zeros(30),np.ones(30)]
ax=axs[1]; r2=(C**2).sum(1)
ax.scatter(C[cl==0,0],r2[cl==0],c=AZ); ax.scatter(C[cl==1,0],r2[cl==1],c=NA,marker="s")
ax.axhline(2.2,color="black"); ax.set_xlabel("x₁"); ax.set_ylabel("nueva columna: x₁² + x₂²")
ax.set_title("Truco del núcleo: con x₁² + x₂²\nun círculo se separa con una recta")
ins=ax.inset_axes([0.62,0.45,0.36,0.36]); ins.scatter(*C[cl==0].T,c=AZ,s=8); ins.scatter(*C[cl==1].T,c=NA,marker="s",s=8); ins.set_xticks([]); ins.set_yticks([]); ins.set_title("antes",fontsize=8)
save(f,"svm_margen_nucleo.png")

# 5. Boosting por rondas
from sklearn.tree import DecisionTreeRegressor
m2=np.array([[50],[60],[70],[80],[90],[100],[110],[120]]); pr=np.array([95,110,120,150,160,175,210,220])
pred=np.full(8,pr.mean()); grid_=np.linspace(45,125,300).reshape(-1,1); G=np.full(300,pr.mean())
f,axs=plt.subplots(1,4,figsize=(12,3.2),sharey=True)
for k,ax in enumerate(axs):
    ax.scatter(m2,pr,c=AZ,zorder=3); ax.plot(grid_,G,c=NA,lw=2)
    for xi,yi,pi in zip(m2.ravel(),pr,pred): ax.plot([xi,xi],[yi,pi],c=GR,lw=1,ls=":")
    ax.set_title(f"ronda {k}: error {np.abs(pr-pred).mean():.1f}"); ax.set_xlabel("m²")
    t_=DecisionTreeRegressor(max_depth=1).fit(m2,pr-pred); pred=pred+.5*t_.predict(m2); G=G+.5*t_.predict(grid_)
axs[0].set_ylabel("precio (miles €)")
save(f,"boosting_rondas.png")

# 6. Dendrograma
from scipy.cluster.hierarchy import linkage, dendrogram
al=pd.DataFrame({"horas_lectura":[1,1.5,6,6.5,3,7],"horas_deporte":[6,7,1,1.5,4,2]},index=["Uxía","Brais","Noa","Iago","Sara","Antía"])
L=linkage(al.values,"ward")
f,axs=plt.subplots(1,2,figsize=(10,3.8))
ax=axs[0]; ax.scatter(al.horas_lectura,al.horas_deporte,c=AZ)
for n,(x,y) in al.iterrows(): ax.annotate(n,(x,y),xytext=(5,4),textcoords="offset points")
ax.set_xlabel("horas de lectura / semana"); ax.set_ylabel("horas de deporte / semana"); ax.set_title("Datos inventados")
ax=axs[1]; dendrogram(L,labels=list(al.index),ax=ax,color_threshold=5); ax.axhline(5,ls="--",c=RO); ax.text(58,5.4,"corte → 2 grupos",color=RO,ha="right")
ax.set_ylabel("distancia al unir"); ax.set_title("Dendrograma (Ward)")
save(f,"dendrograma.png")
print(dendrogram(L,no_plot=True,labels=list(al.index))["ivl"])
from scipy.cluster.hierarchy import fcluster; print(dict(zip(al.index,fcluster(L,2,"maxclust"))))
print(L.round(2))
