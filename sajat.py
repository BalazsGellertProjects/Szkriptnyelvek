import os

directory = "GeeksforGeeks"

parent_dir = "D:/Pycharm"

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

directory = "Geeks"

parent_dir = "D:\PyCharm\GeeksforGeeks"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path, mode)
print("Directory '% s' created" % directory)
