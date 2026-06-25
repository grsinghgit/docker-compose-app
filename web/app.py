import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        db = mysql.connector.connect(
            host="db",  # यह 'db' नाम Compose के अंदर Service का नाम है
            user="root",
            password=os.environ.get('MYSQL_PASSWORD', 'secret'),
            database="mydb"
        )
        cursor = db.cursor()
        cursor.execute("SELECT 'Hello from Database!'")
        result = cursor.fetchone()
        db.close()
        return f"✅ Web App is Running! <br> Database says: {result[0]}"
    except Exception as e:
        return f"❌ Could not connect to Database: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)