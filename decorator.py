def log(func):
    def wrapper(*params):
        print('开始调用eat()函数...')
        func(*params)
        print('结束调用eat()函数...')

    return wrapper


@log
def eat(name, food):
    print('%s开始享用%s' % (name, food))


# eat = log(eat)

print(eat('小甲鱼', '甲鱼'))
