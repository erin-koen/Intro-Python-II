class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'An item named {self.name}'
    
    def on_take(self):
        return 'You have picked up {self.name}.'
    
    def on_drop(self):
        return f'You have dropped {self.name}'
    