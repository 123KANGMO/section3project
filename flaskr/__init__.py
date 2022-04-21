import os

from flask import Flask
from flask import current_app, g
import psycopg2




def create_app(test_config=None):
    # create and configure the app
    print(f"__mame__ : {__name__}")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    conn = psycopg2.connect(
        #jdbc:postgresql://database-1.c8qyfxb7l3rj.ap-northeast-2.rds.amazonaws.com
      host="myfirstdbinstance.c8qyfxb7l3rj.ap-northeast-2.rds.amazonaws.com",
      database="firstdb",
      user="postgres123",
      password="rkdahdmlelql",
      port=5432)
      
    cur = conn.cursor()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/create')
    def create():
        try:
            sql_file = open(os.path.join(app.instance_path, '../flaskr/schema.sql'),'r')
            x=cur.execute(sql_file.read())
            conn.commit()
            print(x)
        except Exception as e :
            return str(e)
        return 'employees, tt table created'

    @app.route('/insert_tt')
    def insert_into_tt():
        try:
            instr = "INSERT INTO tt(id,name) VALUES(%s, %s);"
            cur.execute(instr,(1, 'jamess') )
            conn.commit()
        except Exception as e :
            return str(e)

        return 'add james into TABLE tt'

    @app.route('/select_tt')
    def getsome():
        try:
            instr = "select * from tt limit 1"
            cur.execute(instr)
            tt_records = cur.fetchone()
            answer = ''
            for r in tt_records:
                answer += f"{r}\n"

            
        except Exception as e :
            return str(e)

        return f'{answer} is what i got'

    

    
    # from . import db
    # db.init_app(app)
    # print('db done')

    return app