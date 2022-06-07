MAX_ACTIONS = 3

class Survivor:
  def __init__(self, name: str):
    self.name = name
    self.wounds = 0
    self.actions = 0

  def is_alive(self) -> bool:
    return self.wounds < 2
  
  def actions_remaining(self) -> int:
    return MAX_ACTIONS - self.actions
