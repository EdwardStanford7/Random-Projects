import random

file = open("test.txt", 'w')
for i in range(348):
    file.write(str(random.randint(1, 10)) + "\n")
file.close()


def do_one_group(f):
    string = ""

    for j in range(100):
        line = f.readline()
        if line == "":
            string = string[:-1]
            return string, True
        line = line[:-1]
        string += '"' + line + '",'

    string = string[:-1]
    return string, False


def main():
    f = open("test.txt", 'r')
    output = []
    while True:
        result, ended = do_one_group(f)
        output.append(result)

        if ended:
            break

    f.close()

    for j in output:
        print(j + "\n")


main()

print("The loch ness monster has eaten the code")
print("No more program :(")
