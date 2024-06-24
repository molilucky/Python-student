# def fab(n):
#     a1 = 1
#     a2 = 1
#     a3 = 1
#
#     if n < 1:
#         print('数据有误')
#         return -1
#
#     while n > 2:
#         a3 = a1 + a2
#         a1 = a2
#         a2 = a3
#         n = n - 1
#     return a3
#
#
# n = int(input('请输入一个数字：'))
# result = fab(n)
# if result != -1:
#     print(fab(n))

def fab(n):
    if n < 1:
        print('数据有误')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)


result = fab(12)
if result != -1:
        print(result)
