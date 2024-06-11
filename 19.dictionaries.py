# dictionary = A changeable, ordered, unordered collection of unique key: value pairs
#          Fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Whashinton DC",
            "India":"New Delhi",
            "Bangladesh":"Dhaka",
            "China":"Beijing"}


capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Los Angeles"})
# capitals.pop("China")
# capitals.clear()

# print(capitals["USA"])
# print(capitals["Bangladesh"])
# print(capitals["Germany"])
# print(capitals.get("Germany"))

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())


for key, value in capitals.items():
    print(key,value)