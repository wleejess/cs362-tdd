def check_pwd(pwd):
    letters = "abcdefghijklmnopqrstuvwxyz"
    upperLetters = letters.upper()
    numDigits = "0123456789"
    lowercase = False
    uppercase = False
    digits = False

    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    for char in pwd:
        if char in letters:
            lowercase = True
        if char in upperLetters:
            uppercase = True
    
    if lowercase == True and uppercase == True and digits == True:
        return True
    else:
        return False

    return True