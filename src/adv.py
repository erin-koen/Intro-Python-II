from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allwed.
#
# If the user enters "q", quit the game.

new_player = Player('new', room['outside'])

#function if no move is available
def bad_move():
    print("There's no room in that direction.")
    return

# function to move a player from one room to the next
def attempt_move(player, direction):
    # turn direction into the movement attribute
    attribute = direction + "_to"
    print("this is the", attribute)
    # check player's current room for movement attribute
    if hasattr(player.room, attribute):
        next_room = getattr(player.room, attribute)
        # set attribute value to current value
        player.room = next_room
        return
    else:
        bad_move()

playing = True

while playing:
    print('Location: ', new_player.room.name)
    print('Location Description: ', new_player.room.description)
    #collect user input and set new_player.room to whatever the direction_to points to. 
    direction = input('Which way? (n/e/s/w) or press q to quit \n').lower().strip()
    if direction == 'q':
        print('laters')
        playing = False
    else:
        attempt_move(new_player, direction)