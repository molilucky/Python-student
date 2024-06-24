import os

print(os.getcwd())

os.chdir('D:\\安装包')
print(os.getcwd())
# listdir = os.listdir()
# print(listdir)
#
# os.system('calc')
for i in os.walk(os.getcwd()):
    print(i)
