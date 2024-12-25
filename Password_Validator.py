def validate_password(password):
    p_lower = False
    p_upper = False
    p_digit = False
    p_special = False
    valid_length = 6 <= len(password) <= 12

    for c in password():
        if c.islower():
            p_lower = True
        elif c.isupper():
            p_upper = True
        elif c.isdigit():
            p_digit = True
        elif c in '$#@':
            p_special = True

    if all([p_lower,p_upper,p_digit,p_special,valid_length]):
        return "Valid Password"
    else:
        return "Invalid Password"
        
password = input("Enter the password: ")
print(validate_password(password))
