from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Janaoltova.2019@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sjrkrnrvnrxzck:ce93741021f9ad77b5c9399a53cefe2e1b55ba38fb95fb77923102735d8d14ee@ec2-46-137-123-136.eu-west-1.compute.amazonaws.com:5432/d833dskppje99p'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False



db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))




@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
