# exception = events detected during execution that interrupt the flow of a program

# numerator = int(input("Enter a number to divide: "))
# denominator = int(input("Enter a number to divide: "))
# result = numerator/ denominator
# print(result)

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide: "))
#     result = numerator / denominator
#
# except ZeroDivisionError as e: # Here e as alias
#     print(e)
#     print("It's not possible to divide by zero")
# except ValueError as e:
#     print(e)
#     print("Enter only number plz")
# except Exception as e:
#     print("something went wrong!")
# else:
#     print(result)
#
# finally:
#     print("This will always execute")


# exception = events detected during execution that interrupt the flow of the program
# try:
#     numerator = int(input("Enter a value to divide: "))
#     denominator = int(input("Enter a value to divide: "))
#     result = numerator / denominator
#
# except ZeroDivisionError as e:
#     print(e)
#     print("It is not possible to divide by zero")
# except ValueError as e:
#     print(e)
#     print("Enter only number please!")
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# else:
#     print(round(result))
#
# Practice :
# Exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide :"))
    denumerator = int(input("Enter a number to divide :"))
    result = numerator / denumerator
    # print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero")
except ValueError as e:
    print(e)
    print("Enter only number please")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This will always execute")