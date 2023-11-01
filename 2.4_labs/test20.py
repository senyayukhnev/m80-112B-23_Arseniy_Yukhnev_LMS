def convert(num10: int, sistema: int):
    k = 1
    num = 1
    ans = 0
    a = []
    while k <= num10:
        k = k * sistema
    k = k // sistema
    while k != 0:
        while num10 >= k:
            num10 -= k
            num += 1
        a.append(num)
        num = 0
        k = k // sistema
    for i in range(len(a)):
        ans += a[i]
    return ans


def best_opportunity(num10: int):
    ans = 0
    maximum = 0
    for i in range(2, 11):
        if convert(num10, i) > maximum:
            maximum = convert(num10, i)
            ans = i
    return ans


def main():
    num10 = int(input())
    print(best_opportunity(num10))


if __name__ == "__main__":
    main()
