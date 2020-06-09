shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
item_to_find = 'rice'
found_at = None
# for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# print('Item found at position {}'.format(found_at))

print("**" * 25)

# item_to_find1 = 'spam'
# found_at1 = None
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find1:
#         found_at1 = index
#         break
# if found_at1 is not None:
#     print('Item found at position {}'.format(found_at1))
# else:
#     print("{} not found".format(item_to_find1))

print("**" * 25)

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print('Item found at position {} '.format(found_at))
else:
    print('{} not found'.format(item_to_find))
