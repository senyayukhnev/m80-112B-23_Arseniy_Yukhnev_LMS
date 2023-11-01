s1 = str(input())
s2 = str(input())
s1 = set(s1)
s2 = set(s2)
answ = ''
for i in s1:
    for j in s2:
        if i == j:
            answ += i
print(answ)
