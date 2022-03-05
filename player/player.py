class Player:

  def __init__(self, name: str, health: int, stamina: int, armor: int):
    self.name = name
    self.healthMax = health
    self.health = health
    self.staminaMax = stamina
    self.stamina = stamina
    self.armor = armor

    self.level = 1
    self.gold = 10
    self.experienceMax = 100
    self.experience = 0
