n = int(input())
m = int(input())
manka = []
ovsyanka = []
kusha = []
for _ in range(n + m):
    s = str(input())
    kusha.append(s)

coun = []
for i in kusha:
    if kusha.count(i) == 1:
        coun.append(i)
if len(coun) == 0:
    print('Таких нет')
else:
    for i in sorted(coun):
        print(i)
