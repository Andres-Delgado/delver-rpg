import psycopg2
from dotenv import load_dotenv
from os import getenv
from player.player import Player

class DbProvider:

  def __init__(self):
    load_dotenv()
    self.db_name = getenv('DB_NAME')
    self.db_user = getenv('DB_USER')
    self.db_pass = getenv('DB_PASS')
    self.db_host = getenv('DB_HOST')


  def check_unique_name(self):
    conn = psycopg2.connect(database=self.db_name, user=self.db_user, password=self.db_pass, host=self.db_host)
    cur = conn.cursor()

    cur.execute('INSERT INTO "Players" (name, class) VALUES (%s, %s)', ("ayye", "Ranger"))


    conn.commit()
    cur.close()
    conn.close()

  def create_player(self, player: Player):
    # check unique name
    # users can only have 1 of each class

    return 'hey'
