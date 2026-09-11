from password_checker import is_valid_password 

def test_valid_password():
    assert is_valid_password('abc12345') == True

def test_password_too_short():
    assert is_valid_password('abc123') == False

def test_password_without_number():
    assert is_valid_password('abcdefgh') == False



