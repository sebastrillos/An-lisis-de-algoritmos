"""Ejercicio 4: triangulacion de poligonos (ear clipping)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

P = {"A": (0, 0), "B": (8, 0), "C": (8, 6), "D": (4, 3), "E": (0, 6)}
ORDEN = ["A", "B", "C", "D", "E"]


def cruz(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def area_signo(pts):
    n = len(pts)
    return sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1]
               for i in range(n)) / 2


def tipo_vertice(prev, cur, nxt):
    d = (cur[0] - prev[0]) * (nxt[1] - cur[1]) - (cur[1] - prev[1]) * (nxt[0] - cur[0])
    return d, ("convexo" if d > 0 else "concavo" if d < 0 else "colineal")


def en_triangulo(p, a, b, c):
    """Incluye el borde (triangulo en antihorario)."""
    return cruz(a, b, p) >= 0 and cruz(b, c, p) >= 0 and cruz(c, a, p) >= 0


def es_oreja(poly, i):
    n = len(poly)
    a, b, c = poly[i - 1], poly[i], poly[(i + 1) % n]
    if cruz(a, b, c) <= 0:                 # debe ser convexo
        return False
    for p in poly:
        if p in (a, b, c):
            continue
        if en_triangulo(p, a, b, c):       # ningun vertice dentro ni en el borde
            return False
    return True


def ear_clipping(nombres):
    """Poligono en antihorario. Devuelve lista de triangulos y diagonales."""
    v = list(nombres)
    triangulos, diagonales = [], []
    while len(v) > 3:
        poly = [P[x] for x in v]
        for i in range(len(v)):
            if es_oreja(poly, i):
                a, b, c = v[i - 1], v[i], v[(i + 1) % len(v)]
                print(f"  oreja en {b}: triangulo {a}{b}{c}, diagonal {a}{c}")
                triangulos.append((a, b, c))
                diagonales.append((a, c))
                v.pop(i)
                break
        else:
            raise ValueError("No se encontro oreja (poligono no simple)")
    triangulos.append(tuple(v))
    return triangulos, diagonales


def diagonales_internas(n):
    if n < 3:
        raise ValueError("Un poligono necesita al menos 3 vertices")
    return n - 3


def triangulos(n):
    return n - 2


if __name__ == "__main__":
    pts = [P[x] for x in ORDEN]
    print("Area con signo:", area_signo(pts))
    for i, nombre in enumerate(ORDEN):
        d, t = tipo_vertice(pts[i - 1], pts[i], pts[(i + 1) % 5])
        print(f"  {nombre}: det = {d:>4} -> {t}")
    print("Triangulos:", triangulos(5), "| Diagonales internas:", diagonales_internas(5))
    print("Ear clipping:")
    tri, diag = ear_clipping(ORDEN)
    print("Triangulos obtenidos:", ["".join(t) for t in tri])

    # dibujo: triangulacion valida (DA y DB)
    plt.figure(figsize=(5, 5))
    plt.plot(*zip(*[P[x] for x in ORDEN + ["A"]]), "k-o")
    for a, b in [("D", "A"), ("D", "B")]:
        plt.plot(*zip(P[a], P[b]), "r--")
    for n, p in P.items():
        plt.annotate(n, p, textcoords="offset points", xytext=(5, 5))
    plt.title("Triangulacion: diagonales DA y DB")
    plt.grid(True)
    plt.axis("equal")
    plt.savefig("img/ej4_triangulacion.png", dpi=120, bbox_inches="tight")
