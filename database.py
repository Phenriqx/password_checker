import sqlite3

connection = sqlite3.connect('password.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS password (
                password text)""")

def insert_into_database(password):
    with connection:
        cursor.execute("INSERT INTO password VALUES (:password)", {'password': password})
    print('data inserted successfully')
    
def select_from_database():
    print('')
    with connection:
        cursor.execute("SELECT * FROM password")
        for password in cursor.fetchall():
            print(f'-> {password[0]}')
    print('')