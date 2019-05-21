# import os

# def list_sub_dirs(string):
#     if os.listdir(string) == []:
#         return [string]
#     elif os.path.isdir(string + "/" + os.listdir(string)[-1]):
#         return list_sub_dirs(string) + list_sub_dirs(string + "/" + os.listdir(string)[-1])

# print(list_sub_dirs("C:/Test"))

#to_be_continued