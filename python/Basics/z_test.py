print("######Numbers and Math######")
name = "nana"
num = 5
print(name)
print(num)

print("######Variables and Strings######")
print(f"{name} is {num} years old")

first = "nana"
last = "lau"

formatted = "First Name: {}, Last Name: {}".format(first, last)
print(formatted)
# "First Name: nana, Last Name: lau"

print("######Converting Data Types######")
my_list = [1, 2, 3]
my_list_as_a_string = str(my_list)
print(type(my_list_as_a_string))
print(type(my_list))

num = 12
num = float(num)
print(num)