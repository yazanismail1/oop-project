import pytest
from oop_project.classes import SaveKeeper

@pytest.fixture
def user_instance():
    user = SaveKeeper()
    return user

# -------- TESTS SECTION -------- #

@pytest.mark.skip("todo")
def test_savekeeper_str(user_instance):
    message = '''
    ---------------------------------------------------------
    ################### Welcome to SeaBed ###################
    ---------------------------------------------------------
    A place where you never need to reset a password again...

    User Guide --> 
    
    - Type (1) to view all the your accounts passwords.
    - Type (2) to view a specific account.
    - Type (3) to add account details.
    - Type (4) to edit the account details.
    - Type (5) to delete the account.
    - Type (6) to exit the program.
    ---------------------------------------------------------
    '''
    assert user_instance.__str__() == message

@pytest.mark.skip("todo")
def test_view_accounts(user_instance):
    expected_output = [{'socialMedia': 'Facebook', 'userName': 'Test', 'password': 12345, 'id': 2}]
    assert user_instance.view_accounts() == expected_output

@pytest.mark.skip("todo")
def test_view_account(user_instance):
    social_media_input = "Facebook"
    expected_output = '''Facebook --> User Name: Test, Password: 12345'''
    assert user_instance.view_account(social_media=social_media_input) == expected_output

@pytest.mark.skip("todo")
def test_add_account(user_instance):
    social_media_input = "Instagram"
    user_name_input = "Test 2"
    password_input = "123456"
    expected_output = f"{social_media_input} has been added to your collection successfully"
    assert user_instance.add_account(social_media=social_media_input, user_name=user_name_input, password=password_input) == expected_output

# @pytest.mark.skip("todo")
def test_edit_account(user_instance):
    social_media_input = "Instagram"
    user_name_input = "Test 2"
    password_input = "654321"
    expected_output = {'sheet1': {'socialMedia': 'Instagram', 'userName': 'Test 2', 'password': '654321', 'id': 3}}
    assert user_instance.edit_account(social_media=social_media_input, user_name=user_name_input, password=password_input) == expected_output

# @pytest.mark.skip("todo")
def test_delete_account(user_instance):
    social_media_input = "Instagram"
    user_instance.delete_account(social_media_input)
    expected_output = [{'socialMedia': 'Facebook', 'userName': 'Test', 'password': 12345, 'id': 2}]
    expected_output2 = f"You deleted {social_media_input} from your collection."
    assert user_instance.view_accounts() == expected_output
    assert user_instance.delete_account(social_media_input) == expected_output2

@pytest.mark.skip("todo")
def test_exit_program(user_instance):
    assert user_instance.exit_program() == "Thanks for using SeaBed, hope to see you soon."















