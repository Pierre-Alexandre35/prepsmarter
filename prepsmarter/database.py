import pymysql

class Database:
    instance = None 
    
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self. password = password
        self.db = db 


    def connect(self):
        try: 
            conn = pymysql.connect(
                host = self.host,
                user = self.user,
                passwd = self.password,
                db = self.db
            )
            return conn
        except Exception as e:
            print(e)
        
