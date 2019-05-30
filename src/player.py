# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.player_inventory = []
   
    def __str__(self):
        return f'A player named {self.name}.'
     # function to pick up items and store them in inventory
    def get_item(self, item):
        self.player_inventory.append(item)
        # return

    def drop_item(self, item):
        self.player_inventory.remove(item)
        return

    # function if no move is available
    def bad_move(self):
        print("There's no room in that direction.")
        return

    # function to move a player from one room to the next

    def attempt_move(self, direction):

        # turn direction into the movement attribute
        attribute = direction + "_to"

        # check player's current room for movement attribute
        if getattr(self.current_room, attribute):
            next_room = getattr(self.current_room, attribute)
            # set attribute value to current value
            self.current_room = next_room
            return
        # let em know if it doesn't exist
        else:
            self.bad_move()

