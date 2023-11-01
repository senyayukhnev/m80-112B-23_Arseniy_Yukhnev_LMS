s = str(input()).split()
nums = []
operations = []
stack = []
mn_ind = 0
# for j in s:
#     if j == '*' or j == '-' or j == '+':
#         mn_ind = s.index(j)
#         break
# # print(mn_ind)
# stack.append(s[mn_ind - 2])
# stack.append(s[mn_ind - 1])
# s.pop(mn_ind - 1)
# s.pop(mn_ind - 2)
# # print(s)
# for i in range(len(s)):
#     if s[i] not in '*-+':
#         nums.append(s[i])
#     else:
#         operations.append(s[i])
# # print(operations, nums)
# # print(stack)
# # for i in range(len(nums)):
# for i in range(len(nums)):
#     for operation in operations:
#         # print(operation)
#         if operation == '-':
#             stack.append(nums[i])
#             stack.append(int(stack[i]) - int(stack[i + 1]))
#
#             stack.pop(0)
#             stack.pop(0)
#
#         if operation == '+':
#             stack.append(nums[i])
#             stack.append(int(stack[i]) + int(stack[i + 1]))
#
#             stack.pop(0)
#             stack.pop(0)
#
#         if operation == '*':
#             stack.append(nums[i])
#             stack.append(int(stack[i]) * int(stack[i + 1]))
#
#             stack.pop(0)
#             stack.pop(0)
#
# print(stack[1])
for i in range(len(s)):
    if s[i] not in '+-*':
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
print(stack[0])
