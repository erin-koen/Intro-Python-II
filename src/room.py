# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.room_inventory = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'A room named {self.name}.'
    
    def lose_item(self, item):
        self.room_inventory.remove(item)
        # return
    
    def gain_item(self, item):
        self.room_inventory.append(item)
        # return
    