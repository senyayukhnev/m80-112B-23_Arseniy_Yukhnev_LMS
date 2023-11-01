# new_str = ''
# last_str = ''
# last_str_len = 0
# last_str_arr = []
# n = int(input())
# all_num = [int(i) for i in range(1, n + 1)]
# last_num = all_num[-1]
# for i in range(n):
#     last_num -= i
#     if last_num == 0:
#         last_str_len = i
#         break
#     if last_num == -1:
#         last_str_len = i - 1
#         break
#     if last_num < -1:
#         last_str_len = last_num + i + i - 1
#         break
# last_str_arr += (all_num[len(all_num) - last_str_len:len(all_num)])
# for elem in last_str_arr:
#     if elem != last_str_arr[-1]:
#         last_str += str(elem) + ' '
#     else:
#         last_str += str(elem)
# symb_in_lines = 0
# c = 0
# for i in range(n):
#     f = 0
#     symb_in_lines += 1
#     for j in range(symb_in_lines):
#         c += 1
#         if symb_in_lines > last_str_len:
#             f = 1
#         else:
#             new_str += str(c) + ' '
#     if f == 1:
#         new_str = last_str
#         break
#     for y in range((len(last_str) + 1) // 2):
#         if len(' ' * y + new_str + ' ' * (y + 1)) == len(last_str):
#             print(' ' * (y + 1) + new_str + ' ' * (y + 1))
#         if len(' ' * y + new_str + ' ' * y) == len(last_str):
#             print(' ' * y + new_str + ' ' * y)
#         if len(new_str) == len(last_str):
#             print(new_str)
#     new_str = ''
# print(last_str)
# if n == 1:
#     print(n)
# if n == 2:
#     print(1)
#     print(2)
#      1
#     2 3
#    4 5 6
#  7 8 9 10
# 11 12 13 14
#      1
#     2 3
#    4 5 6
#  7 8 9 10
# 11 12 13 14
# def elka(num: int):
#     elochka_part = 1
#     chislo_vivod = 1
#     line = ""
#     strs = []
#     fl = False
#     while True:
#         for j in range(elochka_part):
#             line += str(chislo_vivod) + " "
#             if chislo_vivod == num:
#                 fl = True
#                 break
#             chislo_vivod += 1
#         strs.append(line)
#         stroka = ""
#         if fl:
#             break
#         elochka_part += 1
#     for i in range(len(strs)):
#         print(f"{strs[i]:^{len(strs[-1])}}")
#
#
# def main():
#     num = int(input())
#     elka(num)
#
#
# if __name__ == "__main__":
#     main()

def happy_new_year_tree(n):
    lines = []
    c = 1
    str_len = 0
    while c <= n:
        str_len += 1
        s = ''
        for i in range(str_len):
            if c <= n:
                s += str(c) + ' '
                c += 1
        lines.append(s[:len(s) - 1:])
    for i in range(len(lines)):
        print(f"{lines[i]: ^{len(lines[len(lines) - 1])}}")
    pass


def main():
    n = int(input())
    happy_new_year_tree(n)


if __name__ == '__main__':
    main()
