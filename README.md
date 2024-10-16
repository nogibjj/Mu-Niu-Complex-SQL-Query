# Mu-Niu-SQL-Database

[![CI/CD Run](https://github.com/nogibjj/Mu-Niu-Complex-SQL-Query/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Mu-Niu-Complex-SQL-Query/actions/workflows/hello.yml)

### Project Overview
This repository demonstrates how to work with complex SQL queries in Python, with a focus on connecting to Databricks SQL, transforming data, and building a pipeline for efficient data extraction, transformation, and querying. This project utilizes environment variables for secure access to the database, ensuring sensitive credentials are not exposed.

### SQL Query & Result

```python
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
```

| ParentalSupport | activity              | previous_grade      | final_grade         |
|-----------------|-----------------------|---------------------|---------------------|
| Medium          | 1.6666666666666667    | 81.33333333333333   | 83.33333333333333   |
| Low             | 0.6666666666666666    | 65                  | 67.33333333333333   |
| High            | 2                     | 85.5                | 87.5                |


### Code Explanation

1. Data Source: The query pulls data from the student_performance table in the default schema. The table is aliased as s1 and s2 to allow for a self-join.

2. Self-Join: The query is doing a self-join and it's not super meaningful for this case(just for the requirement).

3. Aggregation Using AVG(): The query calculates the average for three different fields:

* ExtracurricularActivities: Average number of extracurricular activities.
* PreviousGrade: Average of students' previous grades.
* FinalGrade: Average of students' final grades.

4. Grouping by ParentalSupport:

* The results are grouped by ParentalSupport, which categorizes the students based on the level of support they receive from their parents (e.g., High, Medium, Low).
* For each group (High, Medium, Low), the query computes the average of the activities, previous grades, and final grades.

5. Sorting the Results: The query orders the output by ParentalSupport in alphabetical descending order


###  Result Interpretation

This table suggests a positive correlation between parental support and both academic performance and extracurricular participation. Students with higher parental support tend to have:

* Higher grades (both previous and final grades).
* Greater involvement in extracurricular activities.