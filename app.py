from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema22091'
mysql.init_app(app)

@app.route("/")
def func():
    #GUARDAR AL DIEGO EN LA BASE A DE DATOS
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Diego', 'eldiego@gmail.com', 'fotola.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('empleados/index.html')

@app.route("/juanca")
def func1():
    return render_template('empleados/juancarlos.html')


if __name__ == '__main__':
    app.run(debug=True)