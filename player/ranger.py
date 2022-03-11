from player.player import Player
import constants.icons as icons

class Ranger(Player):
  def __init__(self, user_id: int, name: str):
    super().__init__(
      self,
      user_id=user_id,
      class_name='Ranger',
      name=name,
      health=20,
      stamina=25,
      armor=10
    )

    self.clas_icon = icons.RANGER
    self.class_icon_url = icons.RANGER_URL
    self.gear = '%s 1986 Metallica Shirt' % icons.BLUE
    self.weapon = '%s Homemade Slingshot' % icons.WHITE_LG 