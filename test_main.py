# from main import get_weather
# from main import add, divide
from  main import UserManager
import pytest

# def test_get_weather():
#     assert get_weather(21)=="hot"

# def test_add():
#     assert add(2,3)==5, "2+3 should be 5"
#     assert add(0,0)==0," 0+0 should be 0"
#     assert add(-1,1)==0,"-1+1 should be zero"

# def test_divide():
#     with pytest.raises(ValueError,match="can't divide by zero"):
#      divide(2,0)
#     assert divide(10,2)==5

           
@pytest.fixture # to use fresh instance of the class each time for different functions defines below 
def user_manager():
    """Creates fresh instance of user Manager before each test"""
    return UserManager()
# user_manager=UserManager()
def test_add_user(user_manager):
    assert user_manager.add_user("john doe","john@example.com")==True
    assert user_manager.get_user("john doe")=="john@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john doe","john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john doe","another@example.com")
