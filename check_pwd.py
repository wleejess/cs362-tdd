def check_pwd(pwd):
    letters = "abcdefghijklmnopqrstuvwxyz"
    upperLetters = letters.upper()
    numDigits = "0123456789"
    specialChars = "~`!@#$%^&*()_+-="
    lowercase = False
    uppercase = False
    digits = False
    special = False

    if len(pwd) < 8 or len(pwd) > 20:
        return False
    else:
        for char in pwd:
            if char in letters:
                lowercase = True
            if char in upperLetters:
                uppercase = True
            if char in numDigits:
                digits = True
            if char in specialChars:
                special = True
        
        if lowercase == True and uppercase == True and digits == True and special == True:
            return True
        else:
            return False
