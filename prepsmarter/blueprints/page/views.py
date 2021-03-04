from flask import Blueprint, render_template, request
from prepsmarter.extensions import conn


page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')



@page.route('/questions')
def questions():
    question_id = 30
    sql = "SELECT * FROM questions WHERE question_id = " + str(question_id)
    cursor = conn.cursor()
    cursor.execute(sql)
    question_data = cursor.fetchall()
    
    sql_2 = "SELECT * FROM answers WHERE question_id = " + str(question_id)
    cursor_2 = conn.cursor()
    cursor_2.execute(sql_2)
    answers_data = cursor_2.fetchall()
    return render_template("page/questions.html", question_data=question_data, answers_data = answers_data)


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


@page.route('/store_stats',methods = ['POST', 'GET'])
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