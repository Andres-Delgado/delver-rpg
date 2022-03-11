from player.player import Player
import constants.icons as icons

class Mage(Player):
  def __init__(self, user_id: int, name: str):
    super().__init__(
      self,
      user_id=user_id,
      class_name='mage',
      name=name,
      health=20,
      stamina=20,
      armor=10
    )

    self.clas_icon = icons.MAGE
    self.class_icon_url = icons.MAGE_URL
    self.gear = '%s Cloth Robe' % icons.WHITE_LG
    self.weapon = '%s Large Stick' % icons.WHITE_LG
