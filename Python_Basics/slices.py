players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# print(players[2:])
# print(players[5:])

for player in players[:3]:
    print(player.title())

my_food = ['pizza', 'falafel', 'carrot cake']
friend_food = my_food[:]
friend_food.append('bubble tea')

print(my_food)
print(friend_food)
