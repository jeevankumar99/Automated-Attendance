# Marks attendance and updates the database
import time
import mysql.connector

def initialize_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="jeevan",
            password="jeevan1234",
            database="Attendance_IPP"
        )
        mycursor = mydb.cursor()

    # if database does not exist
    except mysql.connector.errors.ProgrammingError:
        mydb = mysql.connector.connect(
            host="localhost",
            user="jeevan",
            password="jeevan1234",
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE Attendance_IPP")
        mycursor.execute("USE Attendance_IPP")

    mycursor.execute("SHOW TABLES")
    return mycursor


def mark_present(mycursor, students):
    tables = mycursor.execute("SHOW TABLES")
    for student in students:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        if student not in tables:
            query = f"CREATE TABLE {student} (classes_attended DATETIME, classes_absent DATETIME)"
            mycursor.execute(query)
        mycursor.execute(f"INSERT INTO {student} (classes_attened, classes_absent) VALUES ({now}, NULL")


    
