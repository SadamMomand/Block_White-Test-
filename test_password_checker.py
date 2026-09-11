from passwort_checker import in_valid_password 

def test_valid_password():
    assert in_valid_password('abc12345') == True

def test_password_too_short():
    assert in_valid_password('abc123') == False

def test_password_without_number():
    assert in_valid_password('abcdefgh') == False

