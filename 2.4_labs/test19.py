def square(n: int):
    start = 0
    finish = n - 1
    a = [[0 for j in range(n)] for i in range(n)]
    if n % 2 != 0:
        n += 1
    for i in range(n // 2):
        for j in range(start, finish + 1):
            a[start][j] = start + 1
            a[j][finish] = start + 1
            a[finish][j] = start + 1
            a[j][start] = start + 1
        start += 1
        finish -= 1
    for i in range(len(a)):
        for j in range(len(a)):
            print(f"{' ' * (len(str(a[n // 2 - 1][n // 2 - 1])) - len(str(a[i][j])))}"
                  f"{a[i][j]}", end=" ")
        print("\n", end="")


def main():
    n = int(input())
    square(n)


if __name__ == "__main__":
    main()
