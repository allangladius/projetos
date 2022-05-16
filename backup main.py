from flask import Flask, flash, redirect,url_for, render_template,request,session
from functools import wraps
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='24090110'
app.config['MYSQL_DB']='Login'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)
'''connection = mysql.connector.connect(
                                    host='localhost',
                                    user='root',
                                    password='24090110',
                                    database='Login')'''
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
        status = True
        '''if request.method == 'POST' and 'username' in request.form and 'password' in request.form:'''
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                cursor = mysql.connection.cursor()
                cursor.execute('SELECT * FROM Login WHERE username=%s AND password=%s',(username, password))
                account = cursor.fetchone()

                if account:
                    session['logged_in'] = True
                    session['username'] = account['username']
                    flash("Login Successfully", 'success')
                    return render_template('index.html')
                else:
                    flash("Invalid Login. Try Again", 'danger')

                """if username == 'admin' and password == 'admin123':
                        return render_template('index.html')
                else:
                        msg= "Incorrect username / password!"""    
        return render_template('login.html')

if __name__ == "__main__":
    app.secret_key= os.urandom(12)
    app.run(debug=True, host='0.0.0.0',port=5000)