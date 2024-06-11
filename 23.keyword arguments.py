# Keyword arguments = arguments preceded by an identifier when we pass them to a function
#                   The order of the arguments doesn't matter, unlike positional arguments
#               Python knows the name of the arguments that our function receives

# def hello(first,middle, last):
#     print("Hello "+first+" "+middle+" "+last)
#
# hello("Mohammad","Selim","Reza")
# Here we have used positional arguments. So the order matters.

# def hello(first,middle, last):
#     print("Hello "+first+" "+middle+" "+last)
#
# hello(last="Reza",first= "Mohammad",middle = "Selim",)
#This is keyword arguments. So the order doesn't matter.But we need to use identifier like
# first,middle, last


# def products(Grocery, Gadget, Cosmetics):
#     print("Did you buy "+Grocery+", "+Gadget+",and "+Cosmetics+"?")
#
# products("chicken","phone","soap")
# Here we have used positional arguments. So the order matters.

def products(Grocery, Gadget, Cosmetics):
    print("Did you buy "+Grocery+", "+Gadget+",and "+Cosmetics+"?")

products(Cosmetics = "soap",Gadget="chicken",Grocery = "phone")

