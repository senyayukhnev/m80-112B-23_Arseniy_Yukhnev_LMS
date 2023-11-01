def table(n: int, m: int):
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        a[i][0] = i + 1
        a[0][i] = i + 1
    for i in range(1, n):
        for j in range(1, n):
            a[i][j] = a[i][0] * a[0][j]
    for i in range(n):
        for j in range(n):
            if j != n - 1:
                print(f"{a[i][j]:^{m}}", end="|")
            else:
                print(f"{a[i][j]:^{m}}", end="")
        if i != n - 1:
            print()
            print(f"{'-' * (n * (m + 1) - 1)}")


def main():
    n = int(input())
    m = int(input())
    table(n, m)


if __name__ == "__main__":
    main()
