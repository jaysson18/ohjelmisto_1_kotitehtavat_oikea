import random

def laske_pi(n):
    n_ympyra = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)


        if x ** 2 + y ** 2 < 1:
            n_ympyra += 1


    return 4 * n_ympyra / n

if __name__ == "__main__":
    n = int(input("Kuinka monta pistettä arvotaan? "))
    pi_likiarvo = laske_pi(n)
    print(f"π:n likimääräinen arvo on {pi_likiarvo}")s
