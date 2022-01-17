from email.mime import message
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'dbsql'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/add_games')
def games():
    return render_template("add_games.html")

#use add_games form to insert data to database
@app.route('/add_games_done', methods = ['POST', 'GET'])
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


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)






