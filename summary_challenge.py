# print("Please choose from the following options: ")
# print("1:\tLearn Python")
# print("2:\tLearn Rust")
# print("3:\tGo for dinner")
# print("4:\tGo to sleep")
# print("0:\tExit")
choice = "-"
while choice != "0":
    if choice in "1234":
        print("You chose {}".format(choice))
    else:
        print("Please choose from the following options: ")
        print("1:\tLearn Python")
        print("2:\tLearn Rust")
        print("3:\tGo for dinner")
        print("4:\tGo to sleep")
        print("0:\tExit")
    choice = input()

# while True:
#     if choice == "0":
#         break
#     elif choice in "1234":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose from the following options: ")
#         print("1:\tLearn Python")
#         print("2:\tLearn Rust")
#         print("3:\tGo for dinner")
#         print("4:\tGo to sleep")
#         print("0:\tExit")
#     choice = input()
