# import os
#
# path = "C:\\Users\\User\\Desktop\\new folder"
#
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("That's a directory!")
# else:
#     print("That location doesn't exist!")


# Practice:

import os

path = "C:\\Users\\User\\Desktop\\new folder"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That's a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That file doesn't exists!")