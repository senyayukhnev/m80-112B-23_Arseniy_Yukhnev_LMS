n = int(input())
m = int(input())
manka = []
ovsyanka = []
for _ in range(n):
    s = str(input())
    manka.append(s)
for _ in range(m):
    s = str(input())
    ovsyanka.append(s)
mnka = set(manka)
ovsynka = set(ovsyanka)
c = 0
if mnka.isdisjoint(ovsynka):
    print('Таких нет')
else:
    for i in mnka:
        for j in ovsynka:
            if i == j:
                c += 1
    print(c)
