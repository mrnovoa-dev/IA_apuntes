"""Figuras de pandas: tipos de merge y melt/pivot. Ejecutar desde la raíz del repositorio."""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
OUT = "assets/img/"
AZ, NA, VE, GR = "#bfdbfe", "#fed7aa", "#bbf7d0", "#e5e7eb"

def tabla(ax, x, y, df, colores=None, w=1.05, h=0.42, titulo=None):
    cols = list(df.columns)
    if titulo: ax.text(x, y + 0.25, titulo, fontsize=10, weight="bold")
    for j, c in enumerate(cols):
        ax.add_patch(Rectangle((x + j * w, y - h), w, h, fc="#374151", ec="white")); ax.text(x + j * w + w / 2, y - h / 2, c, ha="center", va="center", color="white", fontsize=9)
    for i, (_, fila) in enumerate(df.iterrows()):
        c = colores[i] if colores else "white"
        for j, col in enumerate(cols):
            v = fila[col]; t = "NaN" if pd.isna(v) else (str(int(v)) if isinstance(v, float) and v == int(v) else str(v))
            ax.add_patch(Rectangle((x + j * w, y - h * (i + 2)), w, h, fc=c, ec="#9ca3af"))
            ax.text(x + j * w + w / 2, y - h * (i + 1.5), t, ha="center", va="center", fontsize=9, color="#b91c1c" if t == "NaN" else "black")

al = pd.DataFrame({"id": [1, 2, 3, 4], "nombre": ["Uxía", "Brais", "Noa", "Iago"]})
no = pd.DataFrame({"id": [1, 2, 2, 5], "materia": ["Mates", "Mates", "Lingua", "Mates"], "nota": [8, 6, 7, 9]})
f, ax = plt.subplots(figsize=(12, 6.2)); ax.axis("off"); ax.set_xlim(0, 15.2); ax.set_ylim(-3.6, 4)
tabla(ax, 0.3, 3.4, al, ["white", "white", AZ, AZ], titulo="alumnado")
tabla(ax, 4.0, 3.4, no, ["white", "white", "white", NA], titulo="notas")
ax.text(0.3, 0.95, "Verde: id en las dos tablas · azul: solo en alumnado (Noa, Iago) · naranja: solo en notas (id 5) · NaN: hueco. Brais tiene 2 notas: sale 2 veces.", fontsize=10)
pos = [(0.3, -0.9), (11.3, 3.4), (0.3, -0.9 + 0), (11.3, -0.9)]
for k, (como, (x, y)) in enumerate(zip(["inner", "left", "right", "outer"], [(8.6, 3.4), (0.3, 0.2), (5.4, 0.2), (10.5, 0.2)])):
    u = pd.merge(al, no, on="id", how=como, indicator=True)
    col = [VE if m == "both" else (AZ if m == "left_only" else NA) for m in u["_merge"]]
    tabla(ax, x, y, u.drop(columns="_merge"), col, w=0.95, titulo=f'how="{como}" → {len(u)} filas')
f.tight_layout(); f.savefig(OUT + "pandas_merge.png", dpi=100, facecolor="white"); plt.close(f)

ancha = pd.DataFrame({"nombre": ["Uxía", "Brais"], "Mates": [8, 6], "Lingua": [7, 9]})
larga = ancha.melt(id_vars="nombre", var_name="materia", value_name="nota")
f, ax = plt.subplots(figsize=(11, 3.6)); ax.axis("off"); ax.set_xlim(0, 13); ax.set_ylim(-2.6, 1.2)
tabla(ax, 0.3, 0.6, ancha, [AZ, NA], titulo="ancha: una columna por materia")
tabla(ax, 7.6, 0.6, larga, [AZ, NA, AZ, NA], titulo="larga: una fila por dato")
ax.add_patch(FancyArrowPatch((3.9, 0.0), (7.3, 0.0), arrowstyle="-|>", mutation_scale=18, lw=2, color="#2563eb")); ax.text(5.6, 0.2, 'melt(id_vars="nombre")', ha="center", fontsize=9, family="monospace")
ax.add_patch(FancyArrowPatch((7.3, -1.2), (3.9, -1.2), arrowstyle="-|>", mutation_scale=18, lw=2, color="#ea580c")); ax.text(5.6, -1.0, 'pivot(index="nombre",\ncolumns="materia")', ha="center", va="bottom", fontsize=9, family="monospace")
f.tight_layout(); f.savefig(OUT + "pandas_melt_pivot.png", dpi=100, facecolor="white"); plt.close(f)
print("ok")
