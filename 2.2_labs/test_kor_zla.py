def f(a, b, c, d, x1, x2):
    if a == 0:
        if b == 0:
            if c == 0:
                print('Infinite solutions')
            else:
                print('No solution')
        else:
            print(-c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            print('No solution')
        elif d == 0:
            print(-b / (2 * a))
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            if x1 < x2:
                print(f'{x1:.2f} {x2:.2f}')
            else:
                print(f'{x2:.2f} {x1:.2f}')
                
                
def main():
    a = float(input())
    b = float(input())
    c = float(input())
    d = 0
    x1 = 0
    x2 = 0
    return f(a, b, c, d, x1, x2)


if __name__ == '__main__':
	main()