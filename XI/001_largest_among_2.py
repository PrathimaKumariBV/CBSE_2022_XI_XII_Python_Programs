# Input two numbers and display the larger / smaller number.

print("Enter 2 numbers")
a = int(input("Enter First number"))
b = int(input("Enter Second number"))

if a > b:
    print(a, "is", "Largest number")
    print(b, "is", "Smallest number")
else:
    print("{} is Largest number".format(b))
    print("{} is Smallest number".format(a))
