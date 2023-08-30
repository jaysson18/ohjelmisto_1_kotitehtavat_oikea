import random

def heita_noppaa():
    return random.randint(1, 6)

def main():
    while True:
        silmaluku = heita_noppaa()
        print(f"Heitto: {silmaluku}")
        if silmaluku == 6:
            break

if __name__ == "__main__":
    main()