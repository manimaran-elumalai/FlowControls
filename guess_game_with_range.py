# import random
# highest = 10
# answer = random.randint(1, highest)
# print(answer)  # TODO: Remove after testing
#
# print("Please guess the number between 1 and {}: ".format(highest))
# guess = int(input())
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed")
#     else:
#         print("Sorry, you've not guessed correctly")

import random
highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
print("Please guess the number between 1 and {}: ".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done you guessed")
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
