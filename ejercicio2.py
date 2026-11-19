"""Ejercicio 2: interseccion de segmentos con orientaciones."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def orientacion(p, q, r):
    """1 antihorario, -1 horario, 0 colineal."""
    v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return 0 if v == 0 else (1 if v > 0 else -1)


def en_segmento(p, q, r):
    """r es colineal con pq: esta dentro del segmento?"""
    return (min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and
            min(p[1], q[1]) <= r[1] <= max(p[1], q[1]))


def interseccion(a, b, c, d):
    """True si AB y CD se cruzan, se tocan o se superponen. Costo O(1)."""
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    if o1 != o2 and o3 != o4:                       # caso general
        return True
    if o1 == 0 and en_segmento(a, b, c): return True  # contacto / superposicion
    if o2 == 0 and en_segmento(a, b, d): return True
    if o3 == 0 and en_segmento(c, d, a): return True
    if o4 == 0 and en_segmento(c, d, b): return True
    return False


def dibujar(a, b, c, d, archivo, titulo):
    plt.figure(figsize=(5, 5))
    plt.plot(*zip(a, b), "o-", label="AB")
    plt.plot(*zip(c, d), "s-", label="CD")
    for n, p in zip("ABCD", (a, b, c, d)):
        plt.annotate(n, p, textcoords="offset points", xytext=(5, 5))
    plt.title(titulo)
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.savefig(archivo, dpi=120, bbox_inches="tight")
    plt.close()


# Caso 3: el enunciado no trae C ni D; se asumen C(3,2), D(9,2) (superposicion).
CASOS = {
    "Caso 1": ((1, 1), (7, 5), (2, 6), (8, 1)),
    "Caso 2": ((1, 1), (3, 3), (5, 5), (7, 7)),
    "Caso 3": ((0, 2), (6, 2), (3, 2), (9, 2)),
}

if __name__ == "__main__":
    for k, (nombre, (a, b, c, d)) in enumerate(CASOS.items(), 1):
        o = (orientacion(a, b, c), orientacion(a, b, d),
             orientacion(c, d, a), orientacion(c, d, b))
        print(f"{nombre}: o1..o4 = {o} -> interseccion = {interseccion(a, b, c, d)}")
        dibujar(a, b, c, d, f"img/ej2_caso{k}.png", nombre)
