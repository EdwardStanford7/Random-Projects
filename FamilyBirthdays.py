import random


def three_months_missing():
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(22):
        day = random.randint(1, 365)
        if day < 32:
            months[0] += 1
        elif day < 60:
            months[1] += 1
        elif day < 91:
            months[2] += 1
        elif day < 121:
            months[3] += 1
        elif day < 152:
            months[4] += 1
        elif day < 182:
            months[5] += 1
        elif day < 213:
            months[6] += 1
        elif day < 244:
            months[7] += 1
        elif day < 274:
            months[8] += 1
        elif day < 305:
            months[9] += 1
        elif day < 335:
            months[10] += 1
        else:
            months[11] += 1

    num_months_missing = 0
    for i in months:
        if i == 0:
            num_months_missing += 1

    if num_months_missing >= 3:
        return True
    else:
        return False


def main():
    num_times_three_months_missing = 0

    i = 0

    while i < 1000000:
        if three_months_missing():
            num_times_three_months_missing += 1

        i += 1

    print("The chances of any 22 birthdays missing three or more months are: " + str(
        num_times_three_months_missing / i * 100) + "%")


main()
