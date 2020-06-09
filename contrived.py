numbers = [5, 7, 9, 24, 35, 76]

for i in numbers:
    if i % 13 == 0:
        print("The number is not acceptable")
        break
else:
    print("The numbers are ok")