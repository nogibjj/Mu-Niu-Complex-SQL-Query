import csv
import os
from dotenv import load_dotenv
from databricks import sql

# load
def load_database(dataset="data/student_performance.csv", encoding="utf-8"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)

    load_dotenv()
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                     http_path = os.getenv("HTTP_PATH"),
                     access_token = os.getenv("DATABRICKS_KEY")) as connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS student_performance")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS student_performance (
                    StudentID int,
                    Name string,
                    Gender string,
                    AttendanceRate int,
                    StudyHoursPerWeek int,
                    PreviousGrade int,
                    ExtracurricularActivities int,
                    ParentalSupport string,
                    FinalGrade int
                )
            """
            )
        c.executemany("INSERT INTO student_performance VALUES (?,?,?,?,?,?,?,?,?)", 
                      payload)
        c.close()
    return "Load Success"



if __name__ == '__main__':
    load_database()