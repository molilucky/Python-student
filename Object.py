# class Ball:
#     def setName(self, name):
#         self.name = name
#
#     def kick(self):
#         print('我叫%s,嗷~谁踢我！' % self.name)
#
#
# a = Ball()
# a.setName('飞火流星')
#
# b = Ball()
# b.setName('团队之星')
#
# c = Ball()
# c.setName('世界之星')
#
# a.kick()
# b.kick()
# c.kick()
class Potato:
    __name = '老乌龟'#__表示私有变量
    __code = '绿豆'

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def kick(self):
        print("我叫%s，我爱吃%s" % (self.name, self.code))


p = Potato('小甲鱼', '大米')
p.kick()
