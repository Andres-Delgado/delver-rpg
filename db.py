import psycopg2
from dotenv import load_dotenv
from os import getenv
from player.player import Player



def create_player(player: Player):
  # check unique name
  # users can only have 1 of each class
  
  return 'hey'  
  


load_dotenv()

dbName = getenv('DB_NAME')
dbUser = getenv('DB_USER')
dbPass = getenv('DB_PASS')
dbHost = getenv('DB_HOST')
conn = psycopg2.connect(database=dbName, user=dbUser, password=dbPass, host=dbHost)

cur = conn.cursor()

# "" - string wrapped in double quotes is case sensative
# '' - single quotes in case insensitive

cur.execute('INSERT INTO "Players" (name, class) VALUES (%s, %s)', ("ayye", "Ranger"))


conn.commit()
cur.close()
conn.close()


  