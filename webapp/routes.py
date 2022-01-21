from flask import Blueprint, Flask, render_template, request
from flask_mysqldb import MySQL

home = Blueprint('home', __name__)
add_game = Blueprint('add_game', __name__)

app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

@home.route('/')
def index():
    return render_template("home.html")
@home.route('/home')
def homepage():
    return render_template("home.html")


@add_game.route('/add_games')
def games():
    return render_template("add_games.html")

 

#use add_games form to insert data to database
@add_game.route('/add_games_done', methods = ['POST', 'GET'])
def games_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        
        game_id = request.form['game_id']
        game_name = request.form['game_name']
        release_year = request.form['release_year']
        genre = request.form['genre']
        developer = request.form['dev']
        publisher = request.form['pub']
        platform = request.form['platform']
        own = request.form['own']
        wish = request.form['wish']
        play = request.form['play']
        completed = request.form['comp']

        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute(''' INSERT INTO Games VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id, game_name, release_year, genre, developer, publisher, platform))
        if own == "1":
            cursor.execute(''' INSERT INTO Games_Owned VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id, game_name, release_year, genre, developer, publisher, platform))
        if wish == "1":
            cursor.execute(''' INSERT INTO Games_Wishlist VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id, game_name, release_year, genre, developer, publisher, platform))
        if play == "1":
            cursor.execute(''' INSERT INTO Games_Playing VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id, game_name, release_year, genre, developer, publisher, platform))
        if completed == "1":
            cursor.execute(''' INSERT INTO Games_Completed VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id, game_name, release_year, genre, developer, publisher, platform))

        mysql.connection.commit()
        cursor.close()

        return render_template("done.html")

# route which moves selected data using game id from the wishlist table to the owned games table, it then deletes the record from wishlist table

@add_game.route('/move_game_done', methods = ['POST', 'GET'])
def move_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        
        game_id = request.form['game_id']

        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute('''INSERT INTO `Games_Owned`(`game_name`, `release_year`, `genre`, `developer`, `publisher`, `platform`) SELECT `game_name`, `release_year`, `genre`, `developer`, `publisher`, `platform` FROM `Games_Wishlist` WHERE game_id = %s;''',(game_id,))
        cursor.execute('''DELETE FROM `Games_Wishlist` WHERE game_id = %s;''',(game_id,))
        mysql.connection.commit()
        cursor.close()
            
        return render_template("wish_to_own.html")

# route which moves selected data using game id from the playing table to the completed games table, it then deletes the record from playing table

@add_game.route('/move_playing_game_done', methods = ['POST', 'GET'])
def move_playing_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        
        game_id = request.form['game_id']

        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute('''INSERT INTO `Games_Completed`(`game_name`, `release_year`, `genre`, `developer`, `publisher`, `platform`) SELECT `game_name`, `release_year`, `genre`, `developer`, `publisher`, `platform` FROM `Games_Playing` WHERE game_id = %s;''',(game_id,))
        cursor.execute('''DELETE FROM `Games_Playing` WHERE game_id = %s;''',(game_id,))
        mysql.connection.commit()
        cursor.close()
            
        return render_template("play_to_comp.html")

# route which adds selected data using game id from the owned table to the playing games table
@add_game.route('/add_owned_game_done', methods = ['POST', 'GET'])
def add_owned_game_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        
        game_id = request.form['game_id']

        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute('''INSERT INTO `Games_Playing`(`game_name`, `release_year`, `genre`, `developer`, `publisher`, `platform`) SELECT `game_name`, `release_year`, `genre`, `developer`, `publisher`, `platform` FROM `Games_Owned` WHERE game_id = %s;''',(game_id,))
        mysql.connection.commit()
        cursor.close()
            
        return render_template("own_to_play.html")

