from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')

@app.route('/home')
@app.route('/')
def home():
    title = 'Home'
    return render_template('home.html',title=title)

@app.route('/login')
def login():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/new_stage')
def add_stage():
    pass

@app.route('/new_class')
def add_class():
    pass
    
@app.route('/new_child')
def add_child():
    pass

@app.route('/new_servant')
def add_servant():
    pass

@app.route('/new_attendance')
def add_attendance():
    pass

@app.route('/new_visit/<child_name>')
def add_visit():
    pass

@app.route('/dashboard')
def dashboard():
    pass

@app.route('/config')
def site_configuration():
    pass

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()