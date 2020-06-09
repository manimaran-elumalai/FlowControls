for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 40)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("You're eligible for voting")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))
# (OR) - both returns the same results - Command + / to mark the line as a comment
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You're eligible for voting")
    print("Please put an X in the box")

