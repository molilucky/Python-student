# set1 = {"甲鱼", "鲤鱼", "鱿鱼", "甲鱼"}
# print(set1)
list1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]
# temp = list1.copy()
# list1.clear()
# for each in temp:
#     if each not in list1:
#         list1.append(each)
# print(list1)
print(list(set(list1)))
# 不可变集合
set1 = frozenset({1, 2, 3, 4, 5})
set1.add(6)
print(set1)
