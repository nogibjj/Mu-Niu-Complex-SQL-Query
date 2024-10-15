import sqlite3

def create_CRUD(database, data):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO student_performance (StudentID,Name,Gender,AttendanceRate,StudyHoursPerWeek,PreviousGrade,ExtracurricularActivities,ParentalSupport,FinalGrade) VALUES (?, ?, ?, ?, ?,?,?,?,?)", 
        data
        )
    
    conn.commit()

    cursor.execute("SELECT * FROM student_performance")
    all_records = cursor.fetchall()
    print("Database content (create):")
    for record in all_records:
        print(record)

    conn.close()
        
    print("Records have been successfully created.")


def read_CRUD(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student_performance")
    results = cursor.fetchall()
        
    # Close the connection
    conn.close()

    print("Database content (read):")
    for record in results:
        print(record)

    print("Records have been successfully retrieved.")
    
    return results


def update_CRUD(database, StudentID, new_data):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Update data
    cursor.execute("UPDATE student_performance SET Name	= ?, Gender = ?, AttendanceRate = ?, StudyHoursPerWeek = ?, PreviousGrade = ?, ExtracurricularActivities = ?, ParentalSupport=?,FinalGrade=? WHERE StudentID=?",
    (*new_data, StudentID))

    conn.commit()

    cursor.execute("SELECT * FROM student_performance")
    all_records = cursor.fetchall()
    print("Database content (update):")
    for record in all_records:
        print(record)

    conn.close()

    print("Records have been successfully updated.")


def delete_CRUD(database, StudentID):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Delete data
    cursor.execute("DELETE FROM student_performance WHERE StudentID=?", (StudentID,))

    conn.commit()

    cursor.execute("SELECT * FROM student_performance")
    all_records = cursor.fetchall()
    print("Database content (delete):")
    for record in all_records:
        print(record)

    conn.close()

    print("Records have been successfully deleted.")