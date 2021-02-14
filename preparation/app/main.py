import pymysql
from flask import Flask, render_template, request, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Bonjour2021!',
    db = 'prepsmarter'
)

app = Flask(__name__)
app.secret_key = 'eeee'
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id = "",
    client_secret = "",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/hello')
def hello_world():
    email = dict(session)['profile']['email']
    print(dict(sessiongoo)['profile'])
    return f'Hello, you are logge in as {email}!'

@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/hello')

def execute_multiple(conn, statements, rollback_on_error=True):
    """
    Execute multiple SQL statements and returns the cursor from the last executed statement.

    :param conn: The connection to the database
    :type conn: Database connection

    :param statements: The statements to be executed
    :type statements: A list of strings

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type rollback_on_error: bool

    :returns cursor from the last statement executed
    :rtype cursor
    """

    try:
        cursor = conn.cursor()
        for statement in statements:
            cursor.execute(statement)
            if not rollback_on_error:
                conn.commit() # commit on each statement
    except Exception as e:
        if rollback_on_error:
            conn.rollback()
        raise
    else:
        if rollback_on_error:
            conn.commit() # then commit only after all statements have completed successfully
            

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/contributions')
def contributions():
    sql = "SELECT category_id, category_text FROM category"
    cursor = conn.cursor()
    cursor.execute(sql)    
    categories = cursor.fetchall()
    return render_template("contributions.html", categories=categories)


def question_already_answered(user_id, question_id):
    was_answered = False
    already_answered_sql = "SELECT * FROM responses WHERE user_id=(%s) and question_id=(%s)  LIMIT 1"
    cursor = conn.cursor()
    cursor.execute(already_answered_sql, (user_id, question_id))
    rows = cursor.fetchall()
    if rows:
        was_answered = True
    print(was_answered)
    return was_answered
    
@app.route('/store_stats',methods = ['POST', 'GET'])
def store_stats():
    if request.method == 'POST':
        answer_id = request.json['answer_id']
        question_id = request.json['question_id']    
        user_id = 1
        if not question_already_answered(user_id, question_id):
            sql = "INSERT INTO responses (question_id, user_id, answer_id) VALUES (%s, %s, %s)"
            cursor = conn.cursor()
            cursor.execute(sql, (question_id, user_id, answer_id))
            cursor.fetchall()
            conn.commit()
        return str("selected_answer")

@app.route('/stats')
def stats():
    return render_template("stats.html")

@app.route('/questions')
def questions():
    question_id = 29
    sql = "SELECT * FROM questions WHERE question_id = " + str(question_id)
    cursor = conn.cursor()
    cursor.execute(sql)
    question_data = cursor.fetchall()
    
    sql_2 = "SELECT * FROM answers WHERE question_id = " + str(question_id)
    cursor_2 = conn.cursor()
    cursor_2.execute(sql_2)
    answers_data = cursor_2.fetchall()
    return render_template("questions.html", question_data=question_data, answers_data = answers_data)


def insert_answers(question_id, answer_letter, answer_value, correct_answer):
    is_correct = 0
    if answer_letter == correct_answer:
        is_correct = 1
    sql_answer = "INSERT INTO answers (question_id, answer_letter, answer_value, is_correct) VALUES(%s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql_answer, (question_id, answer_letter, answer_value, is_correct))
    cursor.fetchall()
    conn.commit()
    

@app.route('/add_contributor',methods = ['POST', 'GET'])
def add_contributor():
    name = request.form.get('contrib_name')
    category = request.form.get('category_id')
    question = request.form.get('question')
    answer_a = request.form.get('answer_a')
    answer_b = request.form.get('answer_b')
    answer_c = request.form.get('answer_c')
    correct_answer = request.form.get('correct_answer')
    
    sql_1 = "INSERT INTO contributors (name) VALUES (%s)"
    sql_3 = "INSERT INTO questions (contributor_id, question_text, category_id) VALUES (%s, %s, %s)"
        
        
    cursor = conn.cursor()
    cursor.execute(sql_1, name)
    cursor.fetchall()
    contrib_id = cursor.lastrowid
    conn.commit()
    

    cursor_3 = conn.cursor()
    cursor_3.execute(sql_3, (contrib_id,question, category))    
    cursor_3.fetchall()
    question_id = cursor_3.lastrowid
    conn.commit()  
    
    insert_answers(question_id, "A", answer_a, correct_answer)
    insert_answers(question_id, "B", answer_b, correct_answer)
    insert_answers(question_id, "C", answer_c, correct_answer)
    

    return "e"

    

if __name__ == '__main__':
    app.run()



