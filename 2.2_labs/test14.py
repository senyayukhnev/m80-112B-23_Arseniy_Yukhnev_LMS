num = int(input())
num_arr = [num // 100, num // 10 % 10, num % 10]
mn = min(num_arr)
sred = sum(num_arr) - (min(num_arr) + max(num_arr))
mx = max(num_arr)
if mn == 0:
    print(str(sred) + str(mn), str(mx) + str(sred))
else:
    print(str(mn) + str(sred), str(mx) + str(sred))