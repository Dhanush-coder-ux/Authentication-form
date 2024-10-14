from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = '123'  
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'       
app.config['MYSQL_PASSWORD'] = 'Dhanush@2005#'  
app.config['MYSQL_DB'] = 'sakila'  
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name'in request.form and 'password'in request.form and 'email' in request.form :
        
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!', 'error')
            return render_template('register.html')

        if len(password) < 6:
            flash('Password must be at least 6 characters!', 'error')
            return render_template('register.html')

       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))

        account = cursor.fetchone()
        
        if account:
            flash('Account already exists!', 'error')
        else:
           
            hashed_password = generate_password_hash(password)

            
            cursor.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
                           (name, email, hashed_password))
            mysql.connection.commit()
            flash('You have successfully registered!', 'success')
            return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and 'email'in request.form and 'password'in request.form :
        
        email = request.form['email']
        password = request.form['password']

       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        account = cursor.fetchone()

        if account and check_password_hash(account['password'], password):
            flash('Login successful!', 'success')
           
        else:
            flash('Invalid login credentials!', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
