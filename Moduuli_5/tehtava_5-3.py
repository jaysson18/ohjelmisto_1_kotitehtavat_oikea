def is_prime (number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <=number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    try:
        num = int(input("Syötä kokonaisluku: "))
        if is_prime(num):
            print(f"{num} on alkuluku.")
        else:
            print(f"{num} ei ole alkuluku.")
    except ValueError:
        print("Vihreellinen syöte, syötä kokonaisluku.")

if __name__ == "__main__":
    main()