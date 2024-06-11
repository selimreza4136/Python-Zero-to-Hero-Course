# *args = parameter that will pack all arguments into a tuple
#         It is useful so that a function can accept a varying amount of arguments

# def hello(x,y):
#     result = x*y
#     return result
#
# print(hello(1,2))
# It's a normal function

# def hello(x,y):
#     result = x*y
#     return result
#
# print(hello(1,2,3))
# It will an error because the function has 2 positional arguments but 3 were given

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3))
# instead of *args we can write any name. But there must be and * with it.
# *args means we can put any number of arguments

# def add(*stuff):
#     sum = 0
#  #   stuff[0] = 0 #It won't work because tuple is immutable
#     stuff = list(stuff) # It works fine beacuse it is now list instead of tuple
#     stuff[0] = 0 # this will assign the first element as 0. so the result will be 20
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum+=i
#     return sum
#
# print(add(1,2,3,4,5))

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0]= 0
#     for i in args:
#         sum +=i
#     return sum
# print(add(1,2,3,4,5))