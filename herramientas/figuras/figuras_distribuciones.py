"""Figura de la teoría 6.10: uniforme, binomial y normal (simuladas con semilla fija)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
fig, (a, b, c) = plt.subplots(3, 1, figsize=(7.5, 10.5), dpi=100)
fig.patch.set_facecolor("white")

dado = rng.integers(1, 7, size=60_000)
a.bar(range(1, 7), np.bincount(dado)[1:] / len(dado), color="#93c5fd", edgecolor="#1e3a8a")
a.axhline(1 / 6, color="#b91c1c", ls="--"); a.text(0.6, 1 / 6 + 0.008, "1/6", color="#b91c1c", fontsize=11)
a.set_title("Uniforme: lanzar un dado 60 000 veces", loc="left", fontsize=13)
a.set_xticks(range(1, 7)); a.set_ylim(0, 0.22); a.set_ylabel("proporción")

ac = rng.binomial(n=10, p=0.25, size=100_000)
frec = np.bincount(ac, minlength=11) / len(ac)
b.bar(range(11), frec, color=["#fca5a5" if k >= 5 else "#c4b5fd" for k in range(11)], edgecolor="#334155")
b.set_title("Binomial: aciertos al azar en un test de 10 preguntas (4 opciones)", loc="left", fontsize=12)
b.text(5.3, 0.17, "5 o más aciertos:\n7,8 % de las veces", color="#991b1b", fontsize=11)
b.set_xticks(range(11)); b.set_ylabel("proporción"); b.set_xlabel("aciertos")

alt = rng.normal(170, 8, size=100_000)
c.hist(alt, bins=80, color="#bbf7d0", edgecolor="#166534", lw=0.3, density=True)
for k, col, txt in [(3, "#fef9c3", "99,7 %"), (2, "#fde68a", "95,4 %"), (1, "#fdba74", "68,3 %")]:
    c.axvspan(170 - 8 * k, 170 + 8 * k, color=col, alpha=0.45, zorder=0)
    c.text(170 + 8 * k - 4, 0.0585, txt, ha="center", fontsize=10.5)
c.set_title("Normal: alturas inventadas (media 170 cm, desviación 8)", loc="left", fontsize=13)
c.set_xlabel("altura (cm)"); c.set_yticks([]); c.set_ylim(0, 0.064)
c.set_xticks([146, 154, 162, 170, 178, 186, 194])
fig.tight_layout()
fig.savefig("assets/img/distribuciones.png", facecolor="white")
