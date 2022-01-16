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

@app.route('/add_developer')
def developer():
    return render_template("add_developer.html")

@app.route('/add_completed')
def completed():
    return render_template("add_completed.html")

@app.route('/add_games')
def games():
    return render_template("add_games.html")

@app.route('/add_genre')
def genre():
    return render_template("add_genre.html")

@app.route('/add_platform')
def platform():
    return render_template("add_platform.html")
 
@app.route('/add_publisher')
def publisher():
    return render_template("add_publisher.html")
#use add_games form to insert data to database
@app.route('/add_games_done', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        game_id = request.form['game_id']
        game_name = request.form['game_name']
        release_year = request.form['release_year']
        pub_id = request.form['pub_id']
        dev_id = request.form['dev_id']
        platform_id = request.form['platform_id']
        genre_id = request.form['genre_id']
        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute(''' INSERT INTO games VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id,game_name, release_year, pub_id, dev_id, platform_id, genre_id))
        mysql.connection.commit()
        cursor.close()
        return render_template("done.html")
# use add_genre form to insert data to database
# @app.route('/add_genre_done', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "error"
     
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         age = request.form['age']
#         cursor = mysql.connection.cursor()
#         cursor.execute("USE database_games")
#         cursor.execute(''' INSERT INTO people VALUES(%s,%s,%s)''',(first_name, last_name, age))
#         mysql.connection.commit()
#         cursor.close()
#         return render_template("done.html")


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)






