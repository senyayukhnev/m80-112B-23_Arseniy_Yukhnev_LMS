a = float(input())
b = float(input())
c = float(input())
mx = max(a, b, c)
mn = min(a, b, c)
sred = (a + b + c) - mx - mn
if mn ** 2 + sred ** 2 > mx ** 2:
    print('велика')
if mn ** 2 + sred ** 2 < mx ** 2:
    print('крайне мала')
if mn ** 2 + sred ** 2 == mx ** 2:
    print('100%')
