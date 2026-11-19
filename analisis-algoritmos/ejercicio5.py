"""Ejercicio 5: comparacion de algoritmos n^3 (A) vs n^2 (B)."""

if __name__ == "__main__":
    print(f"{'n':>6} {'T_A=n^3':>16} {'T_B=n^2':>12} {'T_A/T_B':>8}")
    for n in (10, 100, 1000):
        ta, tb = n ** 3, n ** 2
        print(f"{n:>6} {ta:>16,} {tb:>12,} {ta // tb:>8}")
