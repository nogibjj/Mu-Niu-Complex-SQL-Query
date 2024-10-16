import os
import csv
from databricks import sql
from dotenv import load_dotenv


def query(dataset="data/student_performance.csv"):
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    load_dotenv()
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                     http_path = os.getenv("HTTP_PATH"),
                     access_token = os.getenv("DATABRICKS_KEY")) as connection:
        c = connection.cursor()
        c.execute(
            """
                SELECT
                    s1.ParentalSupport,
                    AVG(s1.ExtracurricularActivities) AS activity,
                    AVG(s1.PreviousGrade) AS previous_grade,
                    AVG(s1.FinalGrade) AS final_grade
                FROM student_performance AS s1
                JOIN student_performance AS s2
                    USING (Name)
                GROUP BY s1.ParentalSupport
                ORDER BY s1.ParentalSupport DESC
                """
        )
        c.fetchall()
        c.close()
    return "Query Success"


if __name__ == "__main__":
    query()