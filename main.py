from mylib.extract import extract
from mylib.transform import load_database
from mylib.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

db_file_path = "student_performance_DB.db"  # SQLite DB file path
new_data = ("Johnny", "Male", 80, 10, 70, 1, "Super High", 100)
data = (11, "Luke", "male", 10, 23, 68, 4, "High", 100)


if __name__ == "__main__":
    extract()
    load_database()
    create_CRUD("student_performance_DB.db", data)
    read_CRUD(db_file_path)
    update_CRUD("student_performance_DB.db", 1, new_data)
    delete_CRUD(db_file_path, 11)
