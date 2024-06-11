# return statement = functions send python values/objects back to the caller
#               these values/objects are known as the function's return value

# def cal(x,y):
#     result = x*y
#     # result = x -y
#     return result
#
# print(cal(2,5))

# def cal(x,y):
#     return x*y
# print(cal(4,5))


def cal(x,y):
    result = x*y
    # result = x -y
    return result
z = cal(2,5)
print(z)