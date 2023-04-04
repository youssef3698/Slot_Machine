from slot_machine import SlotMachine

name = input("Welcome to the Terminal Casino! What's your name? ")

wants_to_play = input(f"It's wonderful to host you this evening {name}. We're quite full tonight and our only free game is the Slot Machine. Would you like to play? Y/N ")

if wants_to_play.upper() != "Y":
    print("I understand! I hope to see you soon when the house is less crowded. Have a wonderful evening!")
    quit()
else:
    while True:
        try:
            deposit = float(input(f"That's great! How much would you like to deposit {name}? "))
            if deposit <= 0:
                print("Please deposit a positive number!")
                continue
            else:
                break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
    
balance = deposit

still_playing = True
machine = SlotMachine()

while still_playing:
    while True:
        while True:
            try:
                bet_price = float(input(f"Your balance is {balance}. How much would you like to bet? Remember that each line is a different bet. "))
                break
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
        while True:
            try:
                bet_lines = int(input("How many lines would you like to bet on? "))
                if bet_lines > 3:
                    print("You can only choose up to 3 line to bet on.")
                    continue
                else:
                    break
            except ValueError:
                print("Oops! That was not a valid number. Try again...")
        if (bet_price * bet_lines) < balance:
            break
        else:
            print("I am sorry, your bet is unacceptable. Try again with a valid bet.")
    
    balance -= bet_price * bet_lines
    
    machine.roll()
    
    total = machine.check_wins(bet_lines, bet_price)
    
    if total == 0:
        print("Hard luck. You didn't win anything this round. Better luck next time.")
    else:
        print(f"Congrats! You have won {total} this round!")
    
    balance += total
    
    if balance > 0:
        play_again = input(f"Your remaining balance is {balance}. Would you like to continue playing? Y/N ")
        machine.__init__()
    else:
        play_again = input("Your balance is insufficient to play again. Would you like to deposit a new amount? Y/N ")
        if play_again.upper() != "Y":
            print(f"Thank you for playing. Have a great evening {name}!")
            break
        else:
            while True:
                try:
                    deposit = float(input(f"How much would you like to deposit {name}? "))
                    if deposit <= 0:
                        print("Please deposit a positive number!")
                        continue
                    else:
                        break
                except ValueError:
                    print("Oops! That was not a valid number. Try again...")

    if play_again.upper() != "Y":
        print(f"Thank you for playing! Hope to see you again soon {name}")
        still_playing = False