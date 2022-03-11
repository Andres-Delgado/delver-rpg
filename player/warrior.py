from player.player import Player
import constants.icons as icons

class Warrior(Player):
  def __init__(self, user_id: int, name: str):
    super().__init__(
      self,
      user_id=user_id,
      class_name='Warrior',
      name=name,
      health=20,
      stamina=20,
      armor=15
    )

    self.clas_icon = icons.WARRIOR
    self.class_icon_url = icons.WARRIOR_URL
    self.gear = '%s Wooden Shield' % icons.GREEN
    self.weapon = '%s Shovel' % icons.WHITE_LG
