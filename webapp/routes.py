from flask import Blueprint, Flask, render_template, request
from flask_mysqldb import MySQL

add_game = Blueprint('add_game', __name__)

app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)

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