import psycopg2
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
from player.player import Player

# TODO: TABLE FOR INITIAL VALUES (MAIN LINK TABLE)
# TODO: TABLE FOR USER CREATED VALUES, CURRENT HP, GOLD, XP, ITEMS ETC.
# TODO: HOW TO HANDLE METADATA?
# TODO: STORE ITEM DETAILS IN DB OR IN CODE??

class PlayerDb:
  def __init__(self):
    load_dotenv()
    self.db_name = getenv('DB_NAME')
    self.db_user = getenv('DB_USER')
    self.db_pass = getenv('DB_PASS')
    self.db_host = getenv('DB_HOST')

  def __execute(self, sql: str, data: tuple) -> bool:
    # TODO: try/catch
    conn = psycopg2.connect(
      database=self.db_name,
      user=self.db_user,
      password=self.db_pass,
      host=self.db_host)

    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()
    return True

  def create(self, player: Player) -> bool:
    """insert player to database"""

    # check table for unique name
    sql ='''
      INSERT INTO "Players" (
        user_id,
        name,
        class_name,
        health_max,
        stamina_max,
        level,
        created_date
      ) VALUES (
        %s, %s, %s, %s, %s, %s, %s)'''

    data = (
      player.user_id,
      player.name,
      player.class_name,
      player.health_max,
      player.stamina_max,
      player.level,
      datetime.now()
    )
    return self.__execute(sql, data)

  def read(self, user_id: int, name: str) -> bool:
    """select player from database"""

    sql = '''
      SELECT
        user_id,
        name,
        class_name,
        health_max,
        stamina_max,
        level
      FROM "Players"
      WHERE
        user_id = %s
        AND name = %s'''

    data = (user_id, name)
    return self.__execute(sql, data)

  def update_level_up(self, player: Player) -> bool:
    """update a leveled up player in database"""

    sql = '''
      UPDATE "Players"
      SET
        health_max = %s,
        stamina_max = %s,
        level = %s
      WHERE
        user_id = %s
        AND name = %s'''

    data = (
      player.health_max,
      player.stamina_max,
      player.level,
      player.user_id,
      player.name
    )
    return self.__execute(sql, data)

  def delete(self, player: Player) -> bool:
    """delete player from database"""

    sql = '''
      DELETE FROM "Players"
      WHERE
        user_id = %s
        AND name = %s
    '''

    data = (player.user_id, player.name)
    return self.__execute(sql, data)
