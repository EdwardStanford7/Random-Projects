def double_method():
    ranks = [0]
    for i in range(1, 53):
        if i % 2 == 0:
            lower = ranks[int(((i - 1) / 2) + .5)]
            upper = ranks[int(((i - 1) / 2.0) - .5)]
            ranks.append(i - 1 + lower + upper)
        else:
            lower = ranks[int((i - 1) / 2)]
            upper = ranks[int((i - 1) / 2)]
            ranks.append(i - 1 + lower + upper)

    for i in range(0, 53):
        print("Cards: " + str(i) + ", iterations: " + str(ranks[i]))


double_method()
