"""Ejercicio 1: giro del robot (determinante / producto cruz)."""


def determinante(a, b, c):
    """det = (Bx-Ax)(Cy-By) - (By-Ay)(Cx-Bx). A=anterior, B=actual, C=destino."""
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def clasificar(a, b, c):
    d = determinante(a, b, c)
    if d > 0:
        return "antihorario"
    if d < 0:
        return "horario"
    return "colineal"


CASOS = [
    ((1, 2), (5, 3), (3, 7)),
    ((2, 1), (6, 5), (8, 2)),
    ((1, 1), (3, 3), (6, 6)),
    ((0, 4), (5, 4), (3, 1)),
]

if __name__ == "__main__":
    for i, (a, b, c) in enumerate(CASOS, 1):
        print(f"Caso {i}: det = {determinante(a, b, c):>4} -> {clasificar(a, b, c)}")
