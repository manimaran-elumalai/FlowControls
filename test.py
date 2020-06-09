for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
print('It is over')
print("***" * 20)

for i in range(1, 20):
    if i % 3 != 0 and i % 5 != 0:
        print("i is now {} ".format(i))

print('It is over')
print("***" * 20)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print("i is now {} ".format(i))
print("***" * 20)
for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)