import pymysql
import pandas as pd

# Database connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="****",
    database="nlp"
)

class DataBase:
    def insert(self, name, email, password):
        # Check if email exists
        query = "SELECT email FROM emp WHERE email = %s"
        df = pd.read_sql(query, db,params=[email])
        
        if not df.empty:
            return 0  # Email already exists
        else:
            # Insert new record
            cr = db.cursor()
            insert_query = """
                INSERT INTO emp (name, email, password)
                VALUES (%s,%s,%s)
            """
            cr.execute(insert_query,(name,email,password))
            db.commit()
            return 1 
    
    def search(self, email, password):
        query = "SELECT email, password FROM emp WHERE email = %s AND password = %s"
        df = pd.read_sql(query, db, params=[email, password])
        
        if not df.empty:
            return 1  # Login successful
        else:
            return 0  # Login failed
        
