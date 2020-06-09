shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for item in shopping_list:
    if item == 'spam':
        continue
    print('buy {}'.format(item))

print('**' * 25)

for item in shopping_list:
    if item != 'spam':
        print('buy ' + item)
print('**' * 25)

for item in shopping_list:
    if item == 'spam':
        break
    print('buy ' + item)