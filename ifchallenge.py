name = input('pls enter your name: ')
age = int(input("what's your age? "))

if 18 <= age < 31:
    print("Welcome to club 18-30 holidays, {0}".format(name))
else:
    print("I'm sorry, our holidays are not suited for you")