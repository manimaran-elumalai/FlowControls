day = "Saturday"
temperature = 30
raining = True

if (day == "Monday" and temperature > 27) or not raining:
    print('Go Swimming')
else:
    print("Learn Python")

print('**' * 12)

if 0:
    print('True')
else:
    print('False')

print('**' * 12)

name = input('Pls enter your name: ')
if name:
    print("Hello, {}".format(name))
else:
    print("are you the man withe no name?")

print('**' * 12)

name = input('Pls enter your name: ')
if name != '':
    print("Hello, {}".format(name))
else:
    print("are you the man withe no name?")