# test file
from mylib.extract import extract
from mylib.transform import load_database
from mylib.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

import sqlite3


def test_extract():
    result = extract(
        url="https://raw.githubusercontent.com/nogibjj/Mu-Niu-Pandas-Descriptive-Statistics-Script/main/student_performance.csv",
        file_path="data/student_performance.csv",
    )
    assert result is not None


def test_load_database():
    data = load_database()
    if data:
        print("Database loading successful:")
        for row in data:
            print(row)
    else:
        print("Failed to load the database")


def test_create_CRUD():
    data = (11, "Luke", "male", 10, 23, 68, 4, "High", 100)

    create_CRUD("student_performance_DB.db", data)


def test_read_CRUD():
    database = "student_performance_DB.db"

    data = read_CRUD(database)

    if data:
        print("Data retrieval result:")
        for row in data:
            print(row)

        assert len(data) > 0, "Data is empty"
        print("Test read_CRUD passed successfully.")
    else:
        print("Failed to retrieve data")


def test_update_CRUD():
    db_file = "student_performance_DB.db"

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student_performance")
    all_records = cursor.fetchall()

    print("Database contents:")
    for row in all_records:
        print(row)

    new_data = ("Johnny", "Male", 80, 10, 70, 1, "Super High", 100)
    StudentID = 1  # ID of the record to update
    update_CRUD(db_file, StudentID, new_data)

    # Retrieve the updated data
    cursor.execute(
        "SELECT * FROM student_performance WHERE StudentID = ?", (StudentID,)
    )
    updated_result = cursor.fetchone()

    # Print the updated and expected results
    expected_data = (StudentID,) + new_data
    print("Updated result:", updated_result)
    print("Expected result:", expected_data)

    # Assert statement to compare the updated result with the expected result
    assert updated_result == expected_data, "Data update failed"


def test_delete_CRUD():
    db_file = "student_performance_DB.db"

    # ID of the record to delete
    StudentID = 11

    delete_CRUD(db_file, StudentID)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM student_performance WHERE StudentID = ?", (StudentID,)
    )
    deleted_result = cursor.fetchone()
    conn.close()

    assert deleted_result is None, "Data deletion failed"


if __name__ == "__main__":
    test_extract()
    test_load_database()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
