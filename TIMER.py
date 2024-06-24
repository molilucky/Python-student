# t1 = MyTimer()
# t1
# #未开始计时
# t1.stop()
# #提示：请先调用start（）开始计时！
# t1.start()
# #计时开始
# t1
# #请先调用stop结束计时!
# t1.stop()
# #计时结束！
# t1
# #总共运行了5秒
import time


class MyTimer:
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = time.localtime()
        print("计时开始...")

    def stop(self):
        self.end = time.localtime()
        self._calc()
        print("计时结束！")

    #
    # def _calc(self):
    #     self.lasted = []
    #     self.prompt = '总共运行了'
    #     for index in range(6):
    #         self.lasted.append(self.end[index] - self.begin[index])
    #         self.prompt += str(self.lasted[index])
    #     print(self.prompt)
    #
    #
    # t1 = MyTimer()
    # t1.start()
    # t1.stop()

    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = '未开始计时！'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def _calc(self):
        self.lasted = []
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])


t1 = MyTimer()

print(t1)
