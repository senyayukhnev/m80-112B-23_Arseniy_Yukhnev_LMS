n = int(input())
m = int(input())
manka = []
ovsyanka = []
kusha = []
for _ in range(n + m):
    s = str(input())
    kusha.append(s)

coun = 0
for i in kusha:
    if kusha.count(i) == 1:
        coun += 1
if coun == 0:
    print('Таких нет')
else:
    print(coun)
