# def exchangeRate(dollar):
#     """
#     功能：汇率转换，美元-->人民币
#     汇率：6.54
#     日期：2018-06-25
#     """
#     return dollar * 6.54
#
#
# print(exchangeRate(10))
#
# print(exchangeRate.__doc__)


# def eat(somebody, something):
#     return '%s把%s吃了' % (somebody, something)
#
#
# print(eat('小甲鱼', '蛋糕'))

def saySomething(name='小甲鱼', word='让编程拯救世界'):
    return name + '->' + word


print(saySomething())
print(saySomething('苏轼', '不识庐山真面目，只缘身在此山中'))
