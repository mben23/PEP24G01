# temperature = 10
#
# if temperature > 30:
#     print('Is a hot day')
# else:
#     print('Is not a hot day')


# - wile loop
# i = 1
# while i <= 20:
#     print(i)
#     i = i + 1
# print("Done")


# JOC SA GICIM NUMARUL

# secret_number = 9
# i = 0
# guess_limit = 3
# while i < 3:
#    guess =  int(input("Guess: "))
#    i += 1
#    if guess == secret_number:
#        print('You won: ')
#        break
# else:
#     print("sory you failed.")

# JOC 2 CU MASINA

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is alreadi started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already started.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start = to start the car
stop = to stop the car
quit = tp qit the game""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understend that.")

