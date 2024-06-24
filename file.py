# boy = []
# girl = []
# count = 1
# file_name_record2 = open(r"C:\Users\38430\Desktop\record2.txt", encoding="utf-8")
#
# for each_line in file_name_record2:
#     print(each_line)
#     if each_line[:6] != '======':
#         (role, line_spoken) = each_line.split(':', 1)
#         if role == '小甲鱼':
#             boy.append(line_spoken)
#         if role == '小客服':
#             girl.append(line_spoken)
#     else:
#         file_name_boy = 'boy_' + str(count) + '.text'
#         file_name_girl = 'girl_' + str(count) + '.text'
#
#         boy_file = open(file_name_boy, 'w', encoding="utf-8")
#         girl_file = open(file_name_girl, 'w', encoding="utf-8")
#
#         boy_file.writelines(boy)
#         girl_file.writelines(girl)
#
#         boy = []
#         girl = []
#         count += 1
#
# file_name_boy = 'boy_' + str(count) + '.text'
# file_name_girl = 'girl_' + str(count) + '.text'
#
# boy_file = open(file_name_boy, 'w', encoding="utf-8")
# girl_file = open(file_name_girl, 'w', encoding="utf-8")
# boy_file.writelines(boy)

def save_file(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.text'
    file_name_girl = 'girl_' + str(count) + '.text'

    boy_file = open('%s' % file_name_boy, 'w', encoding='utf-8')
    girl_file = open('%s' % file_name_girl, 'w', encoding='utf-8')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    count = 1
    boy = []
    girl = []

    f = open(file_name, encoding='utf-8')

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)
    f.close()


split_file(r"C:\Users\38430\Desktop\record2.txt")

