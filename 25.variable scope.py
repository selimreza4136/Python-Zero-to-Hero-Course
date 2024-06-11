# scope = the region that a  variable is recognized
#       A variable is only available from inside the region it is created
#       A global and locally scoped versions of a variable  can be created

# LEGB --->> Local Enclosing Global Built-in

# def  display_name():
#     name = "Selim"  # local scope(variable only available inside this function)
#     print(name)
# print(name)
# It will show error because we didn't write any  global variable.
# It can show only global variable.

# name="Shahin" # global scope(available both inside and outside function)

# def  display_name():
#     name = "Selim"  # local scope(variable only available inside this function)
#     print(name)
# print(name) #It will print global version of name
# display_name() # It will print local version of name


# name = "Shahin" # global scope(available both inside and outside function)
# def  display_name():
#     #name = "Selim"  # local scope(variable only available inside this function)
#     print(name)
#
# display_name()
# print(name)
# In this case there is no local scope. So the global scope will work both inside and
# outside the function

#practice:


name = "Code"
def display_name():
    name = "Bro"
    print(name)

# print(name)# It won't  work because we did't mention global scope
print(name) # this works fine because of global scope. Global scope can work both inside and  outside the function
display_name() # this will show the name inside the function

name = "Hey"

def display_name():
    print(name)

display_name() # this works fine because global scope can work both inside and outside the function


