password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@$%^&*()-_=+[]{}|;',.<>?/"

for ch in password:
    if ch.islower():
        has_lower = True
    elif ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_characters:
        has_special = True

if has_upper and has_lower and has_digit and has_special:
    print("Password is valid and acceptable.")
else:
    print("Password is not valid.")
