# * kwargs = parameter that will pack all the arguments into a dictionary
#     It is useful so that a function can accept a varying amount of keyword arguments

# def hello(first,last):
#     print("Hello "+first+" "+last)
#
# hello(first = "Bro",last = "Code")

# def hello(first,last):
#     print("Hello "+first+" "+last)
#
# hello(first = "Bro",middle = "Dude",last = "Code")
# It will show an error because of the unexpected argument middle

# Use of *kwargs
# def hello(**kwargs):
#     print("Hello "+kwargs['first']+" "+ kwargs['last'])
#
# hello(first = "Bro",middle = "Dude",last = "Code")

# def hello(**kwargs): # We can write anything in the position of kwargs
#     #print("Hello "+kwargs['first']+" "+ kwargs['last'])
#     print("Hello", end=" ")
#     for key,value in kwargs.items():
#         print(value,end = " ")
#
# hello(titlle = "Mr",first = "Bro",middle = "Dude",last = "Code")



# def hello(**kwargs):
#     print("Hello", end = " ")
#     for key,value in kwargs.items():
#         print(value, end = " ")
#
# hello(tille = "Data Scientist", first = "Selim", last = "Reza", loc = "USA")

def hello(**kwargs):
    print("Hello")
    for key,value in kwargs.items():
        print(value)

hello(title = "Mr",first = "Selim",last = "Reza",end = " ")

