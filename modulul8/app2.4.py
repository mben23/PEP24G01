from datetime import date

while True:
    input_date = input("Data nasterii in formatul YYYY-M-D [q pentru a iesi]: ")

    if input_date.lower() == 'q':
        break

    try:
        year, month, day = map(int, input_date.split('-'))
        user_birthdate = date(year, month, day)
    except ValueError:
        print("Formatul datelor este incorect. Te rog sa introduci data de nastere in formatul specificat.")
        continue

    current_date = date.today()
    next_birthday = date(current_date.year, user_birthdate.month, user_birthdate.day)

    if next_birthday < current_date:
        next_birthday = date(current_date.year + 1, user_birthdate.month, user_birthdate.day)

    days_alive = (current_date - user_birthdate).days
    days_until_birthday = (next_birthday - current_date).days

    print(f"Ai {days_alive} zile pe acest pamant.")

    if days_until_birthday < 30:
        print("Imediat va fi ziua ta! Mai", days_until_birthday, "zile.")
    else:
        print("Ziua ta va fi in", days_until_birthday, "zile.")
