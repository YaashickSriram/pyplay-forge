import pytest


#fixture
@pytest.fixture
def sample_user():
    """A reusable test user"""
    return {"name" :"Alcie",
            "email": "alice@test.com",
            "age" : 30
            }

@pytest.fixture
def user_list():
    """A list of users for parameterized test"""
    return [
        {"name" : "Alice", "age" : 30},
        {"name" : "Bob", "age" : 25},
        {"name" : "Charlie", "age" : 35}
    ]

#smoke tests

@pytest.mark.smoke
def test_user_has_required_fields(sample_user):
    assert "name" in sample_user
    assert "email" in sample_user
    assert sample_user["age"] > 0

@pytest.mark.smoke
def test_email_contains_at_symbol(sample_user):
    assert "@" in sample_user["email"]

#parameterisation

@pytest.mark.parametrize("age, is_adult", [
    (15, False),
    (17, False),
    (18, True),
    (25, True),
    (65, True)
])
def test_age_classification(age, is_adult):
    assert (age>= 18) == is_adult

#test fixtures with list of users

def test_all_users_have_names(user_list):
    for user in user_list:
        assert user["name"] != " "
        assert len(user["name"]) > 0   