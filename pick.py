import pickle

# list = [123, 3.14, "你好", ['another list']]
#
# pickle_file = open('D:\\my_list.pkl', 'wb')
# pickle.dump(list, pickle_file)
# pickle_file.close()

pickle_file = open('D:\\my_list.pkl', 'rb')
list = pickle.load(pickle_file)
print(list)