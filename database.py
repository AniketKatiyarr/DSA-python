import mysql.connector
example_database = mysql.connector.connect(
    host = "hostname",
    user = "username",
    passw = "12333",
    databse = "testing database"
)

cursor_object = example_database.cursor()
book_info = """create tabke book(
    title varchar 
    author name not nill
    code int
    )"""
