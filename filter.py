# def odd(x):
#     return x % 2
#
#
# temp = filter(odd, range(10))
temp = filter(lambda x: x % 2, range(10))
print(list(temp))