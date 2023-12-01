from flask import Flask, render_template

app = Flask("_name_")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')