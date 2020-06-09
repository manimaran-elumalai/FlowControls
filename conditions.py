age = int(input("How old are you? "))
# if age >= 16 and age <= 65 is the same as the following if condition.
if 16 <= age <= 65:
    # or if age in range(16, 66)
    print("Have a good day at work!")
else:
    print("Enjoy your free time")

print("-" * 40)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")