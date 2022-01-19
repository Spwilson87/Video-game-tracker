from flask import Blueprint, Flask, render_template, request
from flask_mysqldb import MySQL

table = Blueprint('table', __name__)

app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

@table.route('/owned_table')
def owned():
    cursor = mysql.connection.cursor()
    cursor.execute("USE database_games")
    cursor.execute(''' Select * From Games_Owned ''')
    owned = cursor.fetchall()
    return render_template('owned_table.html', title='Owned Games', owned=owned)