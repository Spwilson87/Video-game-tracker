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
def games_done():
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
        cursor.execute(''' INSERT INTO games VALUES(%s,%s,%s,%s,%s,%s,%s)''',(game_id, game_name, release_year, pub_id, dev_id, platform_id, genre_id))
        mysql.connection.commit()
        cursor.close()
        
        return render_template("done.html")

# use add_genre form to insert data to database
@app.route('/add_genre_done', methods = ['POST', 'GET'])
def genre_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        genre_id = request.form['genre_id']
        genre = request.form['genre']
        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute(''' INSERT INTO genre VALUES(%s,%s)''',(genre_id, genre))
        mysql.connection.commit()
        cursor.close()
        return render_template("done.html")

# use add_developer form to insert data to database
@app.route('/add_developer_done', methods = ['POST', 'GET'])
def developer_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        dev_id = request.form['dev_id']
        developer = request.form['developer']
        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute(''' INSERT INTO developer VALUES(%s,%s)''',(dev_id, developer))
        mysql.connection.commit()
        cursor.close()
        return render_template("done.html")

# use add_platform form to insert data to database
@app.route('/add_platform_done', methods = ['POST', 'GET'])
def platform_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        platform_id = request.form['platform_id']
        platform = request.form['platform']
        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute(''' INSERT INTO platform VALUES(%s,%s)''',(platform_id, platform))
        mysql.connection.commit()
        cursor.close()
        return render_template("done.html")

# use add_publisher form to insert data to database
@app.route('/add_publisher_done', methods = ['POST', 'GET'])
def publisher_done():
    if request.method == 'GET':
        return "error"
     
    if request.method == 'POST':
        pub_id = request.form['pub_id']
        publisher = request.form['publisher']
        cursor = mysql.connection.cursor()
        cursor.execute("USE database_games")
        cursor.execute(''' INSERT INTO publisher VALUES(%s,%s)''',(pub_id, publisher))
        mysql.connection.commit()
        cursor.close()
        return render_template("done.html")


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)






