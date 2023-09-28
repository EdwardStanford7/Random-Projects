def sum_digits(n):
    number = str(n)
    digits = []
    for i in range(0, len(number)):
        digits.append(int(number[i]))
    return sum(digits)


result = 0
for a in range(1, 100):
    for b in range(1, 100):
        if sum_digits(a ** b) > result:
            result = sum_digits(a ** b)
print(result)
