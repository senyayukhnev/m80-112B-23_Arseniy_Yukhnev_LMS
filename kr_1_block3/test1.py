n = int(input())
for _ in range(n):
    s = str(input())
    border_ind = []
    for i in range(len(s)):
        if s[i] == '^':
            border_ind.append(i)
    left_border = int(s[border_ind[0] + 1:border_ind[1]])
    right_border = int(s[border_ind[1] + 1::])
    if left_border == right_border:
        new_s = s[:left_border:len(s[0:border_ind[0]]) % 4]
    else:
        new_s = s[left_border:right_border:len(s[0:border_ind[0]]) % 4]

    print(new_s)
