# slicing = create a substring by extracting elements from
# another string
# indexing[] or slice()
# [start:stop:step]


name = "Selim Reza"
first_name = name[0:5] # or [:5]
last_name = name[6:10] # or [6:]
funcky_name=name[0:10:2]
reversed_name = name[::-1]
# by default the step for indexing is 1. But we have taken it as 2
# first character is including and last character is excluding


# print(first_name)
# print(last_name)
# print(funcky_name)
# print(reversed_name)

#slicing
website1 = "http://google.com"
website2 = "http://facebook.com"
website3= "http://wikipedia.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])
print(website3[slice])