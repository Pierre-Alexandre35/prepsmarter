import pymysql
from flask import Flask, render_template, request


conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Bonjour2021!',
    db = 'test_prep_db'
)

app = Flask(__name__)


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
    return render_template("contributions.html")


@app.route('/questions')
def questions():
    sql = "SELECT * FROM questions WHERE question_id = 9"
    cursor = conn.cursor()
    cursor.execute(sql)
    question_data = cursor.fetchall()
    print(question_data)
    return render_template("questions.html", data=question_data)

@app.route('/add_contributor',methods = ['POST', 'GET'])
def add_contributor():
    name = request.form.get('contrib_name')
    category = request.form.get('category')
    question = request.form.get('question')
    answer_a = request.form.get('answer_a')
    answer_b = request.form.get('answer_b')
    answer_c = request.form.get('answer_c')
    correct_answer = request.form.get('correct_answer')
    
    sql_1 = "INSERT INTO contributors (name) VALUES (%s)"
    sql_3 = "INSERT INTO questions (contributor_id, question_text, category) VALUES (%s, %s, %s)"
    
    sql_4 = "INSERT INTO answers (question_id, answer_a, answer_b, answer_c, correct_answer) VALUES(%s, %s, %s, %s, %s)"
        
        
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
    
    cursor_4 = conn.cursor()
    cursor_4.execute(sql_4, (question_id,answer_a, answer_b, answer_c, correct_answer))    
    cursor_4.fetchall()
    conn.commit() 
    

    
    return "e"



if __name__ == '__main__':
    app.run()
