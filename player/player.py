import constants.icons as icons

class Player:

  def __init__(self, user_id: str, class_name: str, name: str, health: int, stamina: int, armor: int):
    # self.id
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
    self.url = None

    # TODO: CREATE INDIVUAL PLAYER CLASSES
    if class_name == 'WARRIOR':
      self.clas_icon = icons.WARRIOR
      self.class_icon_url = icons.WARRIOR_URL
      self.gear = '%s Wooden Shield' % icons.GREEN
      self.weapon = '%s Shovel' % icons.WHITE_LG
    elif class_name == 'MAGE':
      self.clas_icon = icons.MAGE
      self.class_icon_url = icons.MAGE_URL
      self.gear = '%s Cloth Robe' % icons.WHITE_LG
      self.weapon = '%s Large Stick' % icons.WHITE_LG
    elif class_name == 'ROGUE':
      self.clas_icon = icons.ROGUE
      self.class_icon_url = icons.ROGUE_URL
      self.gear = '%s Stinky Shirt' % icons.WHITE_LG
      self.weapon = '%s Simple Dagger' % icons.GREEN
    elif class_name == 'RANGER':
      self.clas_icon = icons.RANGER
      self.class_icon_url = icons.RANGER_URL
      self.gear = '%s 1986 Metallica Shirt' % icons.BLUE
      self.weapon = '%s Homemade Slingshot' % icons.WHITE_LG 
