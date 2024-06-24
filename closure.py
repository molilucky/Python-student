def funX(x):
    # def funY(y):
    #     return x * y
    #
    # return funY
    """
    lambda表达式写法

    """
    return lambda y: x * y


temp = funX(8)
print(temp(5))
