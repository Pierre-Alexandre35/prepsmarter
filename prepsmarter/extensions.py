from prepsmarter.database import Database
import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USERNAME')
pwd = os.getenv('DB_PASSWORD')
db = os.getenv('DB_DATABASE')

conn = Database(host, user, pwd, db).connect()


