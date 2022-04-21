import psycopg2
import pandas as pd

df = pd.read_csv('btc_5m.csv')
df.rename(columns = {'not':'num'}, inplace = True)
df.drop(columns="ignore", inplace=True)
df = df.iloc[:1000]

conn = psycopg2.connect(
  #jdbc:postgresql://database-1.c8qyfxb7l3rj.ap-northeast-2.rds.amazonaws.com
  host="myfirstdbinstance.c8qyfxb7l3rj.ap-northeast-2.rds.amazonaws.com",
  database="firstdb",
  user="postgres123",
  password="rkdahdmlelql",
  port=5432
)

cur = conn.cursor()

# q1 = """
# CREATE TABLE IF NOT EXISTS t1 (
#     id SERIAL PRIMARY KEY,
#     a VARCHAR(50) NOT NULL,
#     b VARCHAR(50) NOT NULL,
#     c VARCHAR(50) NOT NULL
# )
# """

q1="""
CREATE TABLE IF NOT EXISTS btc_ustd_5m (
  open_time BIGINT PRIMARY KEY,
  open float,
  high float,
  low float,
  close float,
  volume float,
  close_time BIGINT,
  qav float,
  num integer,
  tbbav float,
  tbqav float
  );
  """
dq = 'DROP table IF EXISTS btc_ustd_5m;'
cur.execute(dq)
conn.commit()
cur.execute(q1)
conn.commit()


def execute_many(conn, df, table):
    """
    Using cursor.executemany() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % (table, cols)
    cursor = conn.cursor()
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_many() done")
    cursor.close()





execute_many(conn, df, 'btc_ustd_5m')
cur = conn.cursor()
cur.execute("SELECT * FROM btc_ustd_5m LIMIT 100")
rere = cur.fetchall()
for re in rere:
  print(re)