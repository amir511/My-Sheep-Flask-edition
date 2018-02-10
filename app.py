from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')

@app.route('/home')
@app.route('/')
def home():
    title = 'Home'
    return render_template('home.html',title=title)


def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()