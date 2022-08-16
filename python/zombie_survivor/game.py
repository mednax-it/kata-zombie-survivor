from zombie_survivor.survivor import Survivor


class DuplicateNameError(Exception):
    pass


class Game:
    def __init__(self):
        self.survivors = []

    def add_survivor(self, survivor: Survivor):
        existing_names = map(lambda x: x.name, self.survivors)
        if survivor.name in existing_names:
            raise DuplicateNameError
        self.survivors.append(survivor)
