# By: Tim Tarver
# Example Content Management System

# Import all modules needed for this project

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Create the Base Directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Instantiate the application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, data.db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)


# Create class for Content Management System

class ContentManagementSystem(database.Model):
    identification = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    content = database.Column(database.Text, nullable=False)


# Networking: Web Application component to call index.HTML file

@app.route('/')
def index():
    articles = ContentManagementSystem.query.all()
    return render_template('index.html', articles=articles)


# Networking: GET Method: Web Application component to call different pages

@app.route('/article/<int:article_id>')
def article(article_id):
    article1 = ContentManagementSystem.query.get(article_id)
    return render_template('article.html', article=article1)


# Driver Code: Run the app

if __name__ == '__main__':
    app.run(debug=True)
