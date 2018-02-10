from flask import Flask

app = Flask(__name__, template_folder='templates')

@app.route('/index')
@app.route('/')
def index():
    return "Hello World"


def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()