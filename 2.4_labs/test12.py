n = int(input())
m = int(input())
num_tab = [[0] * m for i in range(n)]
c = 0
for i in range(n):
    for j in range(m):
        c += 1
        num_tab[i][j] = c
for row in num_tab:
    for elem in row:
        print(f"{' ' * (len(str(n * m)) - len(str(elem)))}{elem}", end=" ")
    print()
