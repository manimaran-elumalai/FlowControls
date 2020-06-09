# people = int(input("number of persons to pick up: "))

# if 4 < people <= 14:
#     print("you need a minibus")

# if people > 4 and people <= 14:
#     print("minibus")
# else:
#     print('taxi')

# asteroids = [9617, 9618, 9619, 9620, 9621, 13681]

# for asteroid in asteroids:
#     if asteroid == 9617:
#         print('A')
#     elif asteroid == 9618:
#         print("B")
#     elif asteroid == 9619:
#         print('C')
#         break
#     elif asteroid == 9620:
#         print('D')
#     elif asteroid == 9621:
#         print('D')
# else:
#     print('ABCD')

even = [1, 2, 3, 4, 5]
odd = [10, 9, 8, 7, 6]
numbers = even + odd
print(numbers)
numbers.sort()
# print(numbers)
numbers_in_order = sorted(numbers)
if numbers_in_order == numbers:
    print("equal")
else:
    print('not equal')

if numbers_in_order == sorted(numbers):
    print('YES')
else:
    print('NO')
