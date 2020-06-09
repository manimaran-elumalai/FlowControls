activity = input("what would you like to do today? ")
#  casefold() - converts the string to lower case

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
else:
    print('Great, I will c you at the theatres :-)')