from zombie_survivor.survivor import Survivor

class TestSurvivor:
  def setup(self):
    self.survivor = Survivor('Rob Zombie')
  
  def test_initial_setup(self):
    assert self.survivor.name == 'Rob Zombie'
    assert self.survivor.wounds == 0
    assert self.survivor.is_alive()
    assert self.survivor.actions_remaining == 3
  
  def test_setter(self):
    self.survivor.actions_remaining = 5
    assert self.survivor.actions_remaining == 5
