# nested function calls = function calls inside other function calls
#                    inner most function calls are resolved first
#                returned value is used as argument for the next outer function

# num = input("Enter a whole positve number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)


# we can write the above code by just in one line as a
# nested function calls

print(round(abs(float(input("Enter a whole positve number: ")))))