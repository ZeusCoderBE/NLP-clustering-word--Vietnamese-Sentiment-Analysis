import pyodbc
def check_login(username, password):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute("EXEC CheckLogin @Username=?, @Password=?", (username, password))
    login_success = cursor.fetchone()[0]  
    conn.close()
    return login_success
def get_full_name(comment):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute(f"select full_name From users join comments on comments.user_id=users.id where comment = N'{comment}'")
    user_row = cursor.fetchone()
    conn.close()
    return user_row[0] if user_row else None
def get_user_id(username):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM users WHERE username = '{username}'")
    user_row = cursor.fetchone()
    conn.close()
    return user_row[0] if user_row else None
def get_comment_by_user():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute("SELECT comment FROM comments")
    comments = cursor.fetchall()
    return comments
def insert_comment(username, comment):
    user_id = get_user_id(username) 
    if user_id:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comments (user_id, comment) VALUES (?, ?)",(user_id,comment))
        conn.commit()  
        print("Comment inserted successfully.")
        conn.close()
    else:
        print("User not found.")




    