# def recursion(n):
#     for i in range(1, n):
#         n = n * i
#     return n
#
#
# number = int(input('请输入一个数字:'))
# print(recursion(number))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input('请输入一个数字:'))
print(factorial(number))

