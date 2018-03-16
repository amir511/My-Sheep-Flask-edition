from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')


######################################################
# Home, login, logout views                          #
######################################################
@app.route('/home')
@app.route('/')
def home():
    title = 'My Sheep|Home'
    return render_template('home.html',title=title)

@app.route('/login')
def login():
    title = 'My Sheep|Login'
    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    title = 'My Sheep|Logout'
    return render_template('logout.html', title=title)


######################################################    
# The add new 'stuff' views                          #
######################################################
@app.route('/new/stage')
def add_stage():
    title = 'My Sheep|new-stage'
    return render_template('add_edit_stage.html', title=title)

@app.route('/new/class')
def add_class():
    title  = 'My Sheep|new-class'
    return render_template('add_edit_class.html', title=title)
    
@app.route('/new/child')
def add_child():
    title  = 'My Sheep|new-child'
    return render_template('add_edit_child.html', title=title)

@app.route('/new/servant')
def add_servant():
    title  = 'My Sheep|new-servant'
    return render_template('add_edit_servant.html', title=title)

@app.route('/new/attendance/<class_id>')
def add_attendance():
    title  = 'My Sheep|new-attendance'
    return render_template('add_edit_attendance.html', title=title)

@app.route('/new/visit/<child_id>')
def add_visit():
    title  = 'My Sheep|new-visit'
    return render_template('add_edit_visit.html', title=title)


######################################################    
# The view 'stuff' views                             #
######################################################
@app.route('/view/stage/<stage_id>')
def view_stage():
    title  = 'My Sheep|view stage'
    return render_template('view_stage.html', title=title)

@app.route('/view/class/<class_id>')
def view_class():
    title  = 'My Sheep|view class'
    return render_template('view_class.html', title=title)

@app.route('/view/child/<child_id>')
def view_child():
    title  = 'My Sheep|view child'
    return render_template('view_child.html', title=title)

@app.route('/view/servant/<servant_id>')
def view_servant():
    title  = 'My Sheep|view servant'
    return render_template('view_servant.html', title=title)

@app.route('/view/attendance/<class_id>/<attendance_id>')
def view_attendance():
    title  = 'My Sheep|view attendance'
    return render_template('view_attendance.html', title=title)

@app.route('/view/visit/<child_id>/<visit_id>')
def view_visit():
    title  = 'My Sheep|view visit'
    return render_template('view_visit.html', title=title)

######################################################    
# The edit 'stuff' views                             #
######################################################
@app.route('/edit/stage/<stage_id>')
def edit_stage():
    title  = 'My Sheep|edit stage'
    return render_template('add_edit_stage.html', title=title)

@app.route('/edit/class/<class_id>')
def edit_class():
    title  = 'My Sheep|edit class'
    return render_template('add_edit_class.html', title=title)

@app.route('/edit/child/<child_id>')
def edit_child():
    title  = 'My Sheep|edit child'
    return render_template('add_edit_child.html', title=title)

@app.route('/edit/servant/<servant_id>')
def edit_servant():
    title  = 'My Sheep|edit servant'
    return render_template('add_edit_servant.html', title=title)

@app.route('/edit/attendance/<class_id>/<attendance_id>')
def edit_attendance():
    title  = 'My Sheep|edit attendance'
    return render_template('add_edit_attendance.html', title=title)

@app.route('/edit/visit/<child_id>/<visit_id>')
def edit_visit():
    title  = 'My Sheep|edit visit'
    return render_template('add_edit_visit.html', title=title)


######################################################    
# dashboard and site configuration views             #
######################################################
@app.route('/dashboard')
def dashboard():
    title  = 'My Sheep|my dashboard'
    return render_template('dashboard.html', title=title)

@app.route('/config')
def site_configuration():
    pass

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()