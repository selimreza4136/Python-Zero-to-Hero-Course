#
# try:
#     with open("C:\\Users\\User\\Desktop\\test.txt") as file:
#         print(file.read())
#
# except FileNotFoundError:
#     print("That file was not found")

# print(file.closed)


# practice:
# try:
#     with open("C:\\Users\\User\\Desktop\\test.txt") as file:
#         print(file.read())
#
# except FileNotFoundError:
#     print("That file was not found")

# print(file.closed)


try:
    with open("C:\\Users\\User\\Desktop\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")