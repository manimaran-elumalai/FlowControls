available_exits = ['north', 'south', 'east', 'west']

chosen_exit = ''

while chosen_exit not in available_exits:
    chosen_exit = input('Pls choose a direction: ')
    if chosen_exit.casefold() == 'quit':  # converts the str to lowercase
        print('Game Over')
        break
print("Are'nt you glad you got out of there")