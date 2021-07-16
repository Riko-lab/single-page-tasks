import sqlite3
from flask import Flask, g, request, session, render_template, redirect, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash

from helpers import show_tasks, show_single_task

# This is creating a flask application based on whatever file this line of code appears in, generally app.py
app = Flask(__name__)
# In order to use sessions you have to set a secret key, set the secret key.
app.secret_key = '/xa0/xd7"/xb5/xc4k/xc5///xac/xc7/x9cg/xa7/xbe/xcf/xf1/xba/xd6/x9a/xf9/xd8y/x12@'


DATABASE = 'db_users_tasks'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


'''HOME'''
@app.route('/', methods=['GET'])
def index():

    # check if user is currently logged in
    if 'user_id' not in session:
        return render_template('index.html')
    
    # doesn't let the user navigate away from the current page
    return ('', 204)


'''LOGIN'''
@app.route('/api/login', methods=["POST"])
def login():

    # get email and password
    data = (request.get_json())

    db = get_db()

    # get user
    row_user = db.execute("SELECT password, id FROM users WHERE email = :email",
            {'email': data['email']})
    row_user = row_user.fetchall()

    # Ensure username exists and password is correct
    if len(row_user) != 1 or not check_password_hash(row_user[0][0], data["password"]):
        db.close()
        return jsonify({'message': 'Invalid email or password'}), 403
    
    # get user tasks
    rows_tasks = db.execute("SELECT system_task_id, title FROM tasks  WHERE user_id == :user_id", {
        'user_id': row_user[0][1]
    })
    rows_tasks = rows_tasks.fetchall()
    db.close()

    # Remember which user has logged in
    session["user_id"] = row_user[0][1]

    # return list of tasks in html template
    template = show_tasks(rows_tasks)

    return jsonify({'template': template}), 200


'''GET SINGLE TASK'''
@app.route('/api/task', methods=["POST"])
def notes():

    # get task id
    task_id = (request.get_json())
    
    db = get_db()

    # get the task with the indicated id
    task = db.execute("SELECT title, note FROM tasks WHERE system_task_id == :note_id AND user_id == :user_id", {
                           'note_id': task_id,
                           'user_id': session["user_id"]
                       })
    task = task.fetchall()
    if len(task) == 0 :
        db.close()
        return 'Forbidden', 403
    db.close()

    task_title = task[0][0]
    task_note = task[0][1]

    template = show_single_task(task_id, task_title, task_note)
    return jsonify({'template': template}), 200


'''LOGOUT'''
@app.route('/logout')
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")