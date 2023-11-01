def solution():
    arr = []
    while True:
        s = str(input())
        if s == 'Приехали!':
            break
        else:
            arr += s.split()
    print(arr.count('зайка'))


if __name__ == '__main__':
    solution()