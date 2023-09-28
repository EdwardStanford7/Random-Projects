import random


def yahtzee():
    print("Welcome to Yahtzee.")
    # print("Calb was here")
    scoring_options = ["01. ones", "02. twos", "03. threes", "04. fours", "05. fives", "06. sixes",
                       "07. three of a kind", "08. four of a kind", "09. full house", "10. small straight",
                       "11. large straight", "12. chance", "13. yahtzee"]

    upper_section = 0
    num_yahtzees = 0
    score = 0

    while len(scoring_options) > 0:
        choice = input("Press enter to roll the dice")
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)
        die4 = random.randint(1, 6)
        die5 = random.randint(1, 6)
        print(str(die1) + ", " + str(die2) + ", " + str(die3) + ", " + str(die4) + ", " + str(die5))
        count = 0
        while count < 2:
            choice = input("which dice are you keeping: ")
            choice = set(choice)
            if "1" not in choice:
                die1 = random.randint(1, 6)
            if "2" not in choice:
                die2 = random.randint(1, 6)
            if "3" not in choice:
                die3 = random.randint(1, 6)
            if "4" not in choice:
                die4 = random.randint(1, 6)
            if "5" not in choice:
                die5 = random.randint(1, 6)
            print(str(die1) + ", " + str(die2) + ", " + str(die3) + ", " + str(die4) + ", " + str(die5))
            count += 1
        print()

        for val in scoring_options:
            print(val)

        while True:
            choice = input("Pick a scoring option: ")
            if choice.isdigit():
                tf = False
                for i in range(0, len(scoring_options)):
                    if int(choice) == int(scoring_options[i][0:2]):
                        choice = scoring_options[i][4:100]
                        scoring_options.pop(i)
                        tf = True
                        break
                if tf:
                    break
                else:
                    print("Error")
            else:
                print("Error")

        dice = [die1, die2, die3, die4, die5]
        dice.sort()

        if choice == "ones":
            if die1 == 1:
                score += 1
                upper_section += 1
            if die2 == 1:
                score += 1
                upper_section += 1
            if die3 == 1:
                score += 1
                upper_section += 1
            if die4 == 1:
                score += 1
                upper_section += 1
            if die5 == 1:
                score += 1
                upper_section += 1
        elif choice == "twos":
            if die1 == 2:
                score += 2
                upper_section += 2
            if die2 == 2:
                score += 2
                upper_section += 2
            if die3 == 2:
                score += 2
                upper_section += 2
            if die4 == 2:
                score += 2
                upper_section += 2
            if die5 == 2:
                score += 2
                upper_section += 2
        elif choice == "threes":
            if die1 == 3:
                score += 3
                upper_section += 3
            if die2 == 3:
                score += 3
                upper_section += 3
            if die3 == 3:
                score += 3
                upper_section += 3
            if die4 == 3:
                score += 3
                upper_section += 3
            if die5 == 3:
                score += 3
                upper_section += 3
        elif choice == "fours":
            if die1 == 4:
                score += 4
                upper_section += 4
            if die2 == 4:
                score += 4
                upper_section += 4
            if die3 == 4:
                score += 4
                upper_section += 4
            if die4 == 4:
                score += 4
                upper_section += 4
            if die5 == 4:
                score += 4
                upper_section += 4
        elif choice == "fives":
            if die1 == 5:
                score += 5
                upper_section += 5
            if die2 == 5:
                score += 5
                upper_section += 5
            if die3 == 5:
                score += 5
                upper_section += 5
            if die4 == 5:
                score += 5
                upper_section += 5
            if die5 == 5:
                score += 5
                upper_section += 5
        elif choice == "sixes":
            if die1 == 6:
                score += 6
                upper_section += 6
            if die2 == 6:
                score += 6
                upper_section += 6
            if die3 == 6:
                score += 6
                upper_section += 6
            if die4 == 6:
                score += 6
                upper_section += 6
            if die5 == 6:
                score += 6
                upper_section += 6
        elif choice == "three of a kind":
            if dice[0] == dice[1] and dice[1] == dice[2]:
                score += sum(dice)
            elif dice[1] == dice[2] and dice[2] == dice[3]:
                score += sum(dice)
            elif dice[2] == dice[3] and dice[3] == dice[4]:
                score += sum(dice)
        elif choice == "four of a kind":
            if dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3]:
                score += sum(dice)
            elif dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]:
                score += sum(dice)
        elif choice == "full house":
            if dice[0] == dice[1] and dice[2] == dice[3] == dice[4]:
                score += 25
            elif dice[0] == dice[1] == dice[2] and dice[3] == dice[4]:
                score += 25
        elif choice == "small straight":
            dice = set(dice)
            dice = list(dice)
            if len(dice) >= 4:
                if dice[0] + 1 == dice[1] and dice[1] + 1 == dice[2] and dice[2] + 1 == dice[3]:
                    score += 30
                elif dice[1] == dice[2] and dice[2] == dice[3] + 1 and dice[3] == dice[4] + 1:
                    score += 30
        elif choice == "large straight":
            if dice[0] + 1 == dice[1] and dice[1] + 1 == dice[2] and dice[2] + 1 == dice[3] and dice[3] + 1 == dice[4]:
                score += 40
        elif choice == "chance":
            score += sum(dice)
        elif choice == "yahtzee":
            if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
                num_yahtzees += 1
                if num_yahtzees < 3:
                    scoring_options.append("13. yahtzee")
                if num_yahtzees == 1:
                    score += 50
                if num_yahtzees > 1:
                    score += 100

        print("You have " + str(score) + " points.")

    if upper_section >= 63:
        print("Your score for the upper section was more than 63!")
        print("You get the upper section bonus!")
        score += 35

    print()
    print("Your final score was: " + str(score) + " points!")


yahtzee()
