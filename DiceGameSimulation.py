import random


def play_game_strategy1():
    score = 0
    num_rolls = 0
    while score < 20:
        num_rolls += 1
        dice_roll = random.randint(1, 6)
        if dice_roll == 1:
            return [0, num_rolls]
        else:
            score += dice_roll
    return [score, num_rolls]


def play_game_strategy2(num_rolls):
    score = 0
    for i in range(num_rolls):
        dice_roll = random.randint(1, 6)
        if dice_roll == 1:
            return 0
        else:
            score += dice_roll
    return score


def main():
    total_score = 0
    total_num_rolls = 0
    for i in range(1000000):
        total_score += play_game_strategy1()[0]
        total_num_rolls += play_game_strategy1()[1]

    print("For strategy number 1, the average score was " + str(
        total_score / 1000000) + ", and the average number of rolls was " + str(total_num_rolls / 1000000))

    total_score = 0
    for i in range(250000):
        total_score += play_game_strategy2(3)
    for i in range(750000):
        total_score += play_game_strategy2(4)

    print("For game strategy 2, using the average number of rolls from the previous round, the average score is " + str(
        total_score / 1000000))


main()
