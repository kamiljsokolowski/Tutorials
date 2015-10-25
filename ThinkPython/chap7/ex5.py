import math

def estimate_pi():
    k = 0.0
    term_sum = 0.0
    while True:
        term = (math.factorial(4 * k) * (1103 + (26390 * k))) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
        if term < 1e-15:
            return pi
            break
        term_sum = term_sum + term
        pi = 1 / ((2 * math.sqrt(2) / 9801) * term_sum)
        print pi, ' ', math.pi
        k += 1.0

estimate_pi()

