def contador(inc, fim, pas):
    for c in range(1, 11):
        print(c)

    for c in range(10, 0, -2):
        print(c)

    for c in range(inc, fim, pas):
        print(c)


if __name__ == '__main__':
    contador(1, 20, 3)