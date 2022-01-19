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
    return render_template('owned_table.html', owned=owned)

@table.route('/wishlist_table')
def wishlist():
    cursor = mysql.connection.cursor()
    cursor.execute("USE database_games")
    cursor.execute(''' Select * From Games_Wishlist ''')
    wish = cursor.fetchall()
    return render_template('wishlist_table.html', wish=wish)

@table.route('/playing_table')
def playing():
    cursor = mysql.connection.cursor()
    cursor.execute("USE database_games")
    cursor.execute(''' Select * From Games_Playing ''')
    play = cursor.fetchall()
    return render_template('playing_table.html', play=play)

@table.route('/completed_table')
def completed():
    cursor = mysql.connection.cursor()
    cursor.execute("USE database_games")
    cursor.execute(''' Select * From Games_Completed ''')
    comp = cursor.fetchall()
    return render_template('completed_table.html', comp=comp)