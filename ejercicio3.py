"""Ejercicio 3: pares de tuberias que se interceptan (doble for con j = i+1)."""
from ejercicio2 import interseccion


def contar_intersecciones(tubos):
    """Devuelve (pares que se cruzan, llamadas a interseccion)."""
    n = len(tubos)
    cruces = llamadas = 0
    for i in range(n):
        for j in range(i + 1, n):          # j = i+1: sin (i,i) ni pares repetidos
            llamadas += 1
            if interseccion(*tubos[i], *tubos[j]):
                cruces += 1
    return cruces, llamadas


def T(n):
    return n * (n - 1) // 2


def tabla_iteraciones(n):
    print(f"N = {n}")
    total = 0
    for i in range(n):
        c = n - 1 - i
        total += c
        print(f"  i={i}: j va de {i+1} a {n-1} -> {c} llamadas")
    print(f"  Total = {total} = T({n}) = {T(n)}")


if __name__ == "__main__":
    tabla_iteraciones(5)
    tabla_iteraciones(8)
    for n in (100, 1000, 10000):
        print(f"n={n}: {T(n):,} comprobaciones")
    # verificacion con tubos de ejemplo
    tubos = [((0, 0), (4, 4)), ((0, 4), (4, 0)), ((5, 5), (6, 6)), ((10, 10), (12, 12)), ((6, 6), (8, 8))]
    cruces, llamadas = contar_intersecciones(tubos)
    print(f"Ejemplo: {cruces} cruces en {llamadas} llamadas (T(5) = {T(5)})")
