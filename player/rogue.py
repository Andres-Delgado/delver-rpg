from player.player import Player
import constants.icons as icons

class Rogue(Player):
  def __init__(self, user_id: int, name: str):
    super().__init__(
      self,
      user_id=user_id,
      class_name='Rogue',
      name=name,
      health=20,
      stamina=20,
      armor=10
    )

    self.clas_icon = icons.ROGUE
    self.class_icon_url = icons.ROGUE_URL
    self.gear = '%s Stinky Shirt' % icons.WHITE_LG
    self.weapon = '%s Simple Dagger' % icons.GREEN