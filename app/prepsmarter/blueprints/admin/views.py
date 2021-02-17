from flask import Blueprint, render_template, request
import pymysql


admin = Blueprint('admin', __name__, template_folder='templates')

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Bonjour2021!',
    db = 'prepsmarter'
)


@admin.route('/users', methods=['GET'])
def get_users():
    return render_template('admin/new-question.html')



def insert_answers(question_id, answer_letter, answer_value, correct_answer):
    is_correct = 0
    if answer_letter == correct_answer:
        is_correct = 1
    sql_answer = "INSERT INTO answers (question_id, answer_letter, answer_value, is_correct) VALUES(%s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql_answer, (question_id, answer_letter, answer_value, is_correct))
    cursor.fetchall()
    conn.commit()
    
    

@admin.route('/add_contributor',methods = ['POST'])
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