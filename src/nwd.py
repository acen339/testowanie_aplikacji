def nwd(a, b):
    # Algorytm Euklidesa
    while b != 0:
        a, b = b, a % b
    return a
# zmiana żeby zrobić commit
