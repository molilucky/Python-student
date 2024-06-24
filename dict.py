# dict1 = {'李宁': '一切皆有可能', '耐克': 'Just do it', '鱼C': '编程改变世界'}
# print(f'dict1的内容是:')
# for each in dict1:
#     print('%s --> %s' % (each, dict1[each]))
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# # print(dict1[4])
# print(dict1.get('李白', '没有'))
#
# print('李宁' not in dict1)
#
# dict2 = {}
# dict2 = dict2.fromkeys((1, 2, 3), 'numbers')
# print(dict2)
#
# dict2.clear()
# print(dict2)
#
# dict3 = dict1.copy()
# dict3.update(鱼C='www')
# print(dict3)

def test(**params):
    print('有%d个参数' % len(params))
    print(('它们分别是：', params))


a = dict(a=1, b=2, c=3)
print(test(**a))

