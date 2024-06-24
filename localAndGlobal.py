# def discount(price, rate):
#     """
#     其中final_price为局部变量，函数外部无法访问
#     :param price:
#     :param rate:
#     :return:
#     """
#     final_price = price * rate
#     return final_price
#
#
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率'))
# new_price = discount(old_price, rate)
# print('打折后的价格是%s' % new_price)

# def fun1():
#     """
#     嵌套函数中，内部函数可以使用外部函数的局部变量
#     """
#     print("fun1()正在被调用")
#     x = 88
#
#     def fun2():
#         print(x)
#
#     fun2()
#
#
# print(fun1())
# print(fun1.__doc__)

x = 520


def fun1():
    x = 88

    def fun2():
        x = 11
        print(x)

    fun2()


print(fun1())
