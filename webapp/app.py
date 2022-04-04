from flask import Flask, render_template, request
from flask_mysqldb import MySQL
# imports add_game blueprint from routes.py
from routes import add_game, home
# imports table blueprint from tables.py
from tables import table

# config for flask and mysql
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'dbsql'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL()
mysql.init_app(app)

# calls home blueprint from routes
app.register_blueprint(home)

# calls add_game blueprint from routes
app.register_blueprint(add_game)

# calls table blueprint from tables
app.register_blueprint(table)

# runs app on local host with debugging
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)



