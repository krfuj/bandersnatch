
playerName = input("Hello player what is your name: ")
print(f"Hello {playerName} this going to be one hell of a ride")
choice = input(" breakfast? music? work for tuckersoft?").lower()
if (choice == 'breakfast'):
    breakfastChoice = input("sugar? or frosties?").lower()
    if breakfastChoice == 'sugar':
        choice == 'music'
    elif breakfastChoice == 'frosties':
        choice == 'music'
    else:
        print("Invalid entry")
elif choice == 'music':
    musicChoice = input("Nov 2 or Thompson Twins")
    if musicChoice.lower() == 'Nov 2':
        choice == 'work for tuckersoft'
    elif musicChoice.lower() == 'Thompson Twins':
        choice == 'work for tuckersoft'
elif choice == 'work for tuckersoft':
    wftchoice.lower = input("yes / no: ")
    if wftchoice == 'yes':
        print("Game is terrible rate 0/5")
    elif wftchoice.lower == 'no':
        wftchoice1.lower == input("talk about mum at the doctor: yes / no? ")
        if wftchoice1 == 'yes':
            print("You are coming")