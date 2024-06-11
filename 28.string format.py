# str.format = optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item)) # positional argument
# print("The {0} jumped over the {0}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))
# print("The {animal} jumped over the {item} ".format(animal = "cow",item = "moon")) # keyword argument
# print("The {item} jumped over the {animal} ".format(animal = "cow",item = "moon"))

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {1}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))
# print("The {animal} jumped over the {item}".format(animal = "cow",item= "moon"))
# print("The {item} jumped over the {animal}".format(animal = "cow",item= "moon"))

# animal = "cow"
# item = "moon"
# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# Adding padding

# name = "Bro"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}.Nice to meet you".format(name)) # This is by  default left align
# print("Hello, my name is {:<10}.Nice to meet you".format(name)) # This is left align
# print("Hello, my name is {:>10}.Nice to meet you".format(name)) #This is right align
# print("Hello, my name is {:^10}.Nice to meet you".format(name)) # This is ceter align


# Format numbers

# number = 3.14159
#
# print("the number pi is {:.2f}".format(number)) # It will take upto 2 decimal places

number = 1000
print("the number pi is {:.3f}".format(number)) # It will take upto 3 decimal places
print("the number pi is {:,}".format(number)) # It will take comma after 3
print("the number pi is {:b}".format(number)) # It will make the number as binary
print("the number pi is {:X}".format(number)) # It will make the number as Hexadecimal
print("the number pi is {:E}".format(number)) # It will make the number as scientific number


