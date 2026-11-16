"""Ciclo completo de un proyecto de datos y perfil que lidera cada fase (datos.html)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fases = [("1. Entender\nel problema", "neg"), ("2. Recoger\nlos datos", "ing"),
         ("3. Limpiar y\npreparar", "ing"), ("4. Explorar\n(EDA)", "ana"),
         ("5. Modelar", "cie"), ("6. Evaluar", "cie"),
         ("7. Desplegar", "ml"), ("8. Vigilar y\nmejorar", "ml")]
color = {"neg": "#fde68a", "ing": "#bfdbfe", "ana": "#bbf7d0", "cie": "#fbcfe8", "ml": "#ddd6fe"}
nombre = {"neg": "Quien tiene el problema (el «cliente»)", "ing": "Ingeniería de datos",
          "ana": "Análisis de datos", "cie": "Ciencia de datos", "ml": "Ingeniería de ML (MLOps)"}

fig, ax = plt.subplots(figsize=(8, 9.4), dpi=100)
fig.patch.set_facecolor("white"); ax.set_aspect("equal"); ax.axis("off")
R = 3.0
ang = np.pi / 2 - np.arange(8) * 2 * np.pi / 8
RX, RY = 3.25, 3.55
pos = [(RX * np.cos(a), RY * np.sin(a)) for a in ang]
for k, ((txt, rol), (x, y)) in enumerate(zip(fases, pos)):
    ax.add_patch(plt.matplotlib.patches.FancyBboxPatch((x - 0.92, y - 0.45), 1.84, 0.9,
                 boxstyle="round,pad=0.05", fc=color[rol], ec="#334155", lw=1.5))
    ax.text(x, y, txt, ha="center", va="center", fontsize=12)
    x2, y2 = pos[(k + 1) % 8]
    a1, a2 = ang[k] - 0.27, ang[(k + 1) % 8] + 0.27
    ax.annotate("", xy=(RX * np.cos(a2), RY * np.sin(a2)), xytext=(RX * np.cos(a1), RY * np.sin(a1)),
                arrowprops=dict(arrowstyle="-|>", color="#475569", lw=1.8,
                                connectionstyle="arc3,rad=-0.25"))
ax.text(0, 0.35, "Ciclo de un\nproyecto de datos", ha="center", va="center", fontsize=14, fontweight="bold")
ax.text(0, -0.65, "Se vuelve atrás cuando hace falta:\nla evaluación o la vigilancia\npueden obligar a recoger más\ndatos o a cambiar la pregunta.",
        ha="center", va="center", fontsize=10.5, color="#334155")
for i, rol in enumerate(["neg", "ing", "ana", "cie", "ml"]):
    y = -4.75 - i * 0.55
    ax.add_patch(plt.Rectangle((-3.6, y - 0.18), 0.5, 0.36, fc=color[rol], ec="#334155"))
    ax.text(-2.95, y, nombre[rol], va="center", fontsize=12)
ax.text(-3.6, -7.65, "Color = quién lidera la fase. En equipos pequeños, una misma persona hace varias.",
        fontsize=10.5, color="#334155")
ax.set_xlim(-4.3, 4.3); ax.set_ylim(-7.95, 4.3)
fig.tight_layout()
fig.savefig("assets/img/ciclo_roles.png", facecolor="white")
