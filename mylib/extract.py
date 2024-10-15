import os
import requests

def extract(
    url="""
    https://raw.githubusercontent.com/nogibjj/Mu-Niu-Pandas-Descriptive-Statistics-Script/main/student_performance.csv
    """,
    file_path="data/student_performance.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url, timeout=10) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path