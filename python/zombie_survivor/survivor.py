class Survivor:
    def __init__(self, name):
        self.name = name
        self.wounds = 0
        self.actions_remaining = 3

    def is_alive(self):
        return self.wounds < 2
