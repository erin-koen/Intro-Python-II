from room import Room
from player import Player
from item import Item

# Declare all the rooms


rock = Item('quartz', 'it shiny')
sword = Item('excallibur', 'it sharp')
book = Item('tome', 'it dusty')
jacket = Item('duster', 'it warm')
boots = Item('hikers', 'they dry')


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword, rock]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [book]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [jacket]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [boots]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']




playing = True
new_player = Player('new', room['outside'])

while playing:
    print('Location: ', new_player.current_room.name)
    print('Location Description: ', new_player.current_room.description)
    items = [item.name for item in new_player.current_room.room_inventory]
    seperator = ', '
    print('Items Available: ', seperator.join(items) )

    # collect user input and set new_player.room to whatever the direction_to points to.
    direction = input(
        'Which way? (n/e/s/w) or press q to quit \n').lower().strip()

    if direction == 'q':
        print('laters')
        playing = False
    elif direction in ['n', 's', 'e', 'w']:
        new_player.attempt_move(direction)
    else:
        print("that isn't a valid direction you dope.")
