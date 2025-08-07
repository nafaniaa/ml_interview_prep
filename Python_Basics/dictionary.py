# alien_0 = {
#     'color' : 'green', 
#     'points' : 5
#     }

# print(alien_0['color'])
# print(alien_0['points'])

# alien_0['x_position'] = 12
# alien_0['y_position'] = 36

# print(alien_0)

# del alien_0['color']
# print(alien_0)

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

# for key, value in user_0.items():
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')

# for key in user_0.keys():
#     print(key)

# for key in sorted(user_0.keys()):
#     print(key)

# languages = {'python', 'ruby', 'python', 'c'}

# for leng in set(languages):
#     print(leng)


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien.values())

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
