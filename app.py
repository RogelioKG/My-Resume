from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_of_life')
def game_of_life():
    return render_template('game_of_life.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('index.html', username = username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)