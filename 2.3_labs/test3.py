def solution(start, finish):
    while start <= finish:
        print(start, end=' ')
        start += 1


def main():
    start = int(input())
    finish = int(input())
    return solution(start, finish)


if __name__ == '__main__':
    main()
