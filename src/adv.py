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
    room_items = [item.name for item in new_player.current_room.room_inventory]
    player_items = [item.name for item in new_player.player_inventory]
    seperator = ', '
    print('Items available in this room: ', seperator.join(room_items))
    print('Items you are carrying: ', seperator.join(player_items))

    # collect user input and set new_player.room to whatever the direction_to points to.
    command = input(
        ' *** Which way? (n/e/s/w) or press q to quit \n \n ** * Show your inventory by pressing "i"\n\n ** * You can pick up an item by typing "Get itemName"\n \n ** * You can drop an item by typing "Drop itemName" \n\n ** * press q to quit \n \n ').lower().strip()
    command_list = command.split(' ')
    if len(command_list) < 2:
        # if the command is a single word, interpret and proceed as needed
        if command == 'q':
            print('laters')
            playing = False
        elif command in ['n', 's', 'e', 'w']:
            new_player.attempt_move(command)
        elif command == 'i':
            print('Items you are carrying: ', seperator.join(player_items))
        else:
            print("that isn't a valid command you dope.")
    else:
        # if the command is more than one word, evaluate first word for 'get' or 'drop' and the second one for the item name
        if command_list[0] == 'get' and command_list[1] in room_items:

            # identify the item object by name
            item_in_question = [
                item for item in new_player.current_room.room_inventory if item.name == command_list[1]][0]

            # call the player get command on the item
            new_player.get_item(item_in_question)

            # call the item on_take command to print the message
            item_in_question.on_take()

            # call the room lose_item command on the item to finalize the transfer
            new_player.current_room.lose_item((item_in_question))

        elif command_list[0] == 'drop' and command_list[1] in player_items:

            # identify the item object by name
            # (need to handle what happens if more than one item has the same name, come back to that)
            item_in_question = [
                item for item in new_player.player_inventory if item.name == command_list[1]][0]
            print(item_in_question.name)
            # call the player get command on the item
            new_player.drop_item(item_in_question)

            # call the item on_take command to print the message
            item_in_question.on_drop()

            # call the room lose_item command on the item to finalize the transfer
            new_player.current_room.gain_item(item_in_question)
