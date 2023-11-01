a = str(input())
b = str(input())
arr = [int(a[0]), int(a[1]), int(b[0]), int(b[1])]
mx = max(arr)
mn = min(arr)
arr.pop(arr.index(mn))
arr.pop(arr.index(mx))
if sum(arr) > 9:
    print(str(mx) + str(sum(arr))[1] + str(mn))
else:
    print(str(mx) + str(sum(arr)) + str(mn))