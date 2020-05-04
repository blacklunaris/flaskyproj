from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app= Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/appdb'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db= SQLAlchemy(app)



@app.route('/')
def profile():
    return render_template('profile.html')

if __name__== "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)