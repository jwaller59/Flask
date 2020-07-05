from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')

@app.route('/main')
def main():
    return 'Goodbye World'

@app.route('/pack')
def pack():
    return render_template('Pack.html', title='Jarvis - Pack')

@app.route('/pick')
def pick():
    return render_template('Pick.html', title='Jarvis - Pick')

@app.route('/stow')
def stow():
    return render_template('Stow.html', title='Jarvis - Stow')

@app.route('/receive')
def receive():
    return render_template('Receive.html', title='Jarvis - Receive')

