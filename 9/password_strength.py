from collections import Counter


MIN_LENGTH = 8

def check_password_strength(password):
    
    has_lower = any(c.islower() for c in password)
    if not has_lower:
        print("The password must contain a lower case letter!")
        return False
    
    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        print("The password must contain an upper case letter!")
        return False
    
    special_chars = "!@#$%^&*(),.?\":{}|<>"
    has_special = any(c in special_chars for c in password)
    if not has_special:
        print("The password must contain a special char!")
        return False
    
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        print("The password must contain a digit!")
        return False
    
    if len(password) < MIN_LENGTH:
        print("The password must contain at least 8 chars!")
        return False
    
    char_count = Counter(password)
    if any(count > 2 for count in char_count.values()):
        print("The password cannot be repeated more then twice!")
        return False
    
    for i in range(len(password) - 2):   # ord: brings char to ASCII
        if (ord(password[i+1]) == ord(password[i]) + 1 and 
            ord(password[i+2]) == ord(password[i]) + 2):
            print("The password cannot contain a sequence of 3 consecutives chars!")
            return False
        
    return True


# Test cases
valid_passwords = [
    "Ab3!xYz9"
]

invalid_passwords = [
    "098765@A",    # no lowercase
    "098765@a",    # no uppercase
    "gtejfAd1",    # no special char
    "gtejfAd@",    # no digit
    "We1@",        # too short
    "Abc123!!!",   # repeated chars
    "Abcd123!"     # sequence of chars
]

def test_passwords(passwords, expected_result: bool):
    for pwd in passwords:
        result = check_password_strength(pwd)
        status = "passed!" if result == expected_result else "failed!"
        print(f"Password {pwd}: {status}")

print("Testing invalid passwords")
test_passwords(invalid_passwords, expected_result=False)

print("\nTesting valid passwords")
test_passwords(valid_passwords, expected_result=True)
