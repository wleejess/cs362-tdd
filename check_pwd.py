def check_pwd(pwd):
    letters = "abcdefghijklmnopqrstuvwxyz"

    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    for char in pwd:
        if char in letters:
            return True
        else:
            return False

    return True
