from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint, render_template, request, session, redirect, url_for, flash

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "HI"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
                
    
    return app

app = create_app()
db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    def __init__(self, username, password):
        self.username = username 
        self.password = password

@app.route("/")
def index():
    users=Users.query.all()
    return render_template("base.html", users= users)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username and password:
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            flash('You are logged in!!')
            db.session.commit()
    return render_template('signup.html')




with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)



