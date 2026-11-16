"""Figura de la ficha «Sistemas de recomendación» (algoritmos.html). Datos inventados."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

personas = ["Uxía", "Brais", "Noa", "Iago", "Sara"]
libros = ["Memorias", "O lapis", "Cartas", "Dragón", "Marte", "Torre"]
M = np.array([[5, 4, 0, 1, 2, 0], [4, 5, 4, 0, 1, 1], [1, 0, 2, 5, 4, 5],
              [0, 1, 1, 4, 5, 4], [5, 0, 4, 2, 0, 1]], dtype=float)
normas = np.linalg.norm(M, axis=0)
S = (M.T @ M) / np.outer(normas, normas)

fig, (a, b) = plt.subplots(2, 1, figsize=(7.5, 10), dpi=100, gridspec_kw={"height_ratios": [5, 6]})
fig.patch.set_facecolor("white")
a.imshow(np.where(M == 0, np.nan, M), cmap="YlOrRd", vmin=0, vmax=5)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        a.text(j, i, "?" if M[i, j] == 0 else int(M[i, j]), ha="center", va="center", fontsize=14,
               color="#555" if M[i, j] == 0 else "black", fontweight="bold")
a.set_xticks(range(6), libros, fontsize=11); a.set_yticks(range(5), personas, fontsize=12)
a.set_title("1. Notas del alumnado (? = no lo ha leído)", fontsize=13, loc="left")
a.add_patch(plt.Rectangle((-0.5, 3.5), 6, 1, fill=False, ec="#1d4ed8", lw=3))
a.text(1, 4.75, "", fontsize=1)

b.imshow(S, cmap="Blues", vmin=0, vmax=1)
for i in range(6):
    for j in range(6):
        b.text(j, i, f"{S[i, j]:.2f}", ha="center", va="center", fontsize=11,
               color="white" if S[i, j] > 0.7 else "black")
b.set_xticks(range(6), libros, fontsize=11); b.set_yticks(range(6), libros, fontsize=11)
b.set_title("2. Parecido entre libros (coseno de sus columnas)", fontsize=13, loc="left")
fig.text(0.02, 0.01, "Galegos clásicos (Memorias, O lapis, Cartas) se parecen entre sí;\n"
         "fantasía y ciencia ficción (Dragón, Marte, Torre), también. Sara puntuó alto\n"
         "los clásicos: se le recomienda «O lapis» (3,9) antes que «Marte» (2,3).",
         fontsize=11, va="bottom")
fig.tight_layout(rect=(0, 0.07, 1, 1))
fig.savefig("assets/img/recomendacion.png", facecolor="white")
