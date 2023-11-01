s = str(input()).split()
stack = []


def factorial(n):
    if n == 1:
        return n
    return factorial(n - 1) * n


for i in range(len(s)):
    if s[i] not in '+-*/~!#@':
        stack.append(int(s[i]))
    elif s[i] == '+':
        num = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num + num2)
    elif s[i] == '-':
        num = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num2 - num)
    elif s[i] == '*':
        num = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num * num2)
    elif s[i] == '/':
        num = stack.pop(-1)
        num2 = stack.pop(-1)
        stack.append(num // num2)
    elif s[i] == '~':
        num = stack.pop(-1)
        stack.append(num * -1)
    elif s[i] == '!':
        num = stack.pop(-1)
        stack.append(factorial(num))
    elif s[i] == '#':
        stack.append(stack[-1])
    elif s[i] == '@':
        num2 = stack.pop(-2)
        stack.append(num2)
        num3 = stack.pop(-2)
        stack.append(num3)
        num = stack.pop(-3)
        stack.append(num)

print(stack[-1])
