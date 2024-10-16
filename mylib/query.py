import os
from databricks import sql
from dotenv import load_dotenv


def query():
    load_dotenv(dotenv_path='../.env')
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                     http_path = os.getenv("HTTP_PATH"),
                     access_token = os.getenv("DATABRICKS_KEY")) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT
                        s1.ParentalSupport,
                        AVG(s1.ExtracurricularActivities) AS activity,
                        AVG(s1.PreviousGrade) AS previous_grade,
                        AVG(s1.FinalGrade) AS final_grade
                    FROM default.student_performance AS s1
                    JOIN default.student_performance AS s2
                        USING (Name)
                    GROUP BY s1.ParentalSupport
                    ORDER BY s1.ParentalSupport DESC;
                    """
            )
            cursor.close()
            connection.close()

    return "Query Success"


if __name__ == "__main__":
    query()