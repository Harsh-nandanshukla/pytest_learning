from db import Database
import pytest

@pytest.fixture
def db():
    """Provide a fresh indtance of Databse class and cleans up after the test."""
    database=Database()
    yield database #provide the fixture instance it's going to yorld the DB whemn it is needed and will run the code that comes after the yield keyword 
    # anything above yoedl wil run before test as setup operation and everything that comes after yield keyword wll run after the test as cleanup test or teardown step
    database.data.clear()# cleanup state (not needed for in-memory, but usefull for real dbs)

def test_add_user(db):
    db.add_user(1,"alice")
    assert db.get_user(1)=="alice"

def test_add_duplicate_user(db):
    db.add_user(1,"alice")
    with pytest.raises(ValueError,match="User already exists"):
        db.add_user(1,"Bob")

def test_delete_user(db):
    db.add_user(2,"bob")
    db.delete_user(2)
    assert db.get_user(2) is None


