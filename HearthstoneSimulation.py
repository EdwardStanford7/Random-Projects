import random


def best_outcome():
    stupid_hacky_solution = 1
    targets = ["mine", "his", "me", "him", "mine"]
    for i in range(3):
        target = random.randint(0, len(targets) - 1 - stupid_hacky_solution)
        if targets[target] == "his":
            targets.remove("his")
        elif targets[target] == "mine":
            targets.remove("mine")
            stupid_hacky_solution = 0

    if "mine" in targets:
        if "his" not in targets:
            return True
    else:
        return False


def mad_bomber_simulation():
    num_best_outcomes = 0
    for i in range(1000000):
        if best_outcome():
            num_best_outcomes += 1

    print("The percentage of the time that his minion dies and your minion does not is %" + str(
        num_best_outcomes / 10000))


def player_one_wins():
    win_lose = [
        [1, 2, 1],
        [2, 1, 2],
        [1, 2, 1]]

    player_1_options = [0, 1, 2]
    player_2_options = [0, 1, 2]
    player_1_wins = 0
    player_2_wins = 0

    while player_1_wins < 3 and player_2_wins < 3:
        player_1_choice = player_1_options[random.randint(0, len(player_1_options) - 1)]
        player_2_choice = player_2_options[random.randint(0, len(player_2_options) - 1)]

        # print("Player one choice: " + str(player_1_choice) + " player 2 choice: " + str(player_2_choice))

        # print(player_1_options)
        # print(player_2_options)

        winner = win_lose[player_1_choice][player_2_choice]

        if winner == 1:
            # print("Player one won")
            player_1_wins += 1
            player_1_options.remove(player_1_choice)
        else:
            # print("Player two won")
            player_2_wins += 1
            player_2_options.remove(player_2_choice)

        # print("player one wins: " + str(player_1_wins))
        # print("player two wins: " + str(player_2_wins))

    if player_1_wins > player_2_wins:
        return True
    else:
        return False


def tournament_simulation():
    num_player_one_wins = 0

    for i in range(1000000):
        if player_one_wins():
            num_player_one_wins += 1

    print("The percentage of the time that player 1 wins is " + str((num_player_one_wins / 1000000) * 100) + "%")


mad_bomber_simulation()
tournament_simulation()
