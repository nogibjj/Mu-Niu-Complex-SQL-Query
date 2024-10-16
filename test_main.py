from mylib.extract import extract
from mylib.transform import load_database
from mylib.query import query


def test_extract():
    ext = extract()
    assert ext is not None


def test_load():
    load = load_database()
    assert load == "Load Success"


def test_query():
    q = query()
    assert q == "Query Success"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
