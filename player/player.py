import constants.icons as icons

class Player:
  def __init__(self, user_id: str, class_name: str, name: str, health: int, stamina: int, armor: int):
    self.user_id = user_id
    self.class_name = class_name
    self.name = name
    self.health_max = health
    self.health = health
    self.stamina_max = stamina
    self.stamina = stamina
    self.armor = armor

    self.level = 1
    self.gold = 10
    self.experience_max = 100
    self.experience = 0
    self.class_icon_url = None
