# logical operators(and,or,not)= used to check if two or more conditional statements are True
temp = int(input("What is the temperature outside?: "))

# if temp >=0 and temp <= 30:
#     print("The temperature is good today")
#     print("Go outside.")
# elif temp <0 or temp >30:
#     print("The temperature is bad today")
#     print("Stay inside.")


# not is opposite of the given condition

if not (temp >=0 and temp <= 30):
    print("The temperature is bad today")
    print("Stay inside.")

elif not (temp <0 or temp >30):
    print("The temperature is good today")
    print("Go outside.")
