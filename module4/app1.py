[8:42 PM] Emanuel Aurel Craciun
    if len(passwd) < 7:
        print("Parola cu lungime gresita")
        condition_not_ok = True
    for character in requires_chars:
        if character in passwd:
            break
    else:
        print("Parola trebuie sa contina : ! @ %")
        condition_not_ok = True
    for character in range(10):
        if str(character) in passwd:
            break
    else:
        print("Parola trebuie sa contina : number")
        condition_not_ok = True
    if condition_not_ok:
        check_passwd()
check_passwd()