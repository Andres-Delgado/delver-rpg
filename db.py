from wsgiref.handlers import IISCGIHandler
import psycopg2

DB_NAME = 'mdhkissn'
DB_USER = 'mdhkissn'
DB_PASS = 'b_KE2vU2xfkvwVQ090hff5GHOrz2tPMd'
DB_HOST = 'jelani.db.elephantsql.com'
DB_PORT = '5432'


conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

cur = conn.cursor()

cur.execute("INSERT INTO Players (id, name, class) VALUES (%s, %s, %s)", (1, 'BussyBoy', 'Ranger'))


conn.commit()
cur.close()
conn.close()


  