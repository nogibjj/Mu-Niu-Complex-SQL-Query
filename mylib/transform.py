import sqlite3
import csv


# load
def load_database(dataset="data/student_performance.csv", encoding="utf-8"):
    data = csv.reader(open(dataset, newline="", encoding=encoding), delimiter=",")
    next(data)
    conn = sqlite3.connect("student_performance_DB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS student_performance")
    c.execute(
        """
        CREATE TABLE student_performance (
            StudentID INTEGER,
            Name TEXT,
            Gender TEXT,
            AttendanceRate INTEGER,
            StudyHoursPerWeek INTEGER,
            PreviousGrade INTEGER,
            ExtracurricularActivities INTEGER,
            ParentalSupport TEXT,
            FinalGrade INTEGER
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO student_performance (
        StudentID,Name,Gender,AttendanceRate,StudyHoursPerWeek,PreviousGrade,ExtracurricularActivities,ParentalSupport,FinalGrade)
        VALUES (?, ?, ?, ?, ?,?,?,?,?)""",
        data,
    )
    conn.commit()
    conn.close()
    return "student_performance_DB.db"