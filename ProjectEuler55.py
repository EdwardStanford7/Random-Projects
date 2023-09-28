def is_lychrel(n):
    n = str(n)
    for j in range(1, 50):
        n1 = reverse_number(n)
        if is_palindrome(str(int(n) + int(n1))):
            return False
        n = str(int(n) + int(n1))
    return True


def reverse_number(n):
    str_n = str(n)
    str1n = ""
    length = len(str(n))
    for j in range(0, length):
        str1n += str_n[length - 1 - j]
    return str1n


def is_palindrome(n):
    for j in range(0, len(n)):
        if n[j] != n[-(j + 1)]:
            return False
    return True


result = 0
for i in range(1, 10001):
    if is_lychrel(i):
        result += 1

print(result)
