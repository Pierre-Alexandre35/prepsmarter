import pymysql

class Database:
    
    def __init__(self):
        self.con = pymysql.connect(host='localhost', 
                                    user='root',
                                    password='Bonjour2021!', 
                                    db='prepsmarter',
                                    cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
            
    
    def __disconnect__(self):
        self.con.close()
        
        


    
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