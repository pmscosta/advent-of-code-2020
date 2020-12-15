from collections import OrderedDict


def loadInput(filename):
    file = open(filename)
    return [str(line.rstrip('\n')) for line in file]


def part_one(input):
    valid = 0
    for line in input:
        rule, pwd = str(line).split(':')
        pwd_range, char = rule.split(' ')
        low, high = [int(v) for v in pwd_range.split('-')]
        counter = 0
        for pchar in pwd:
            if pchar == char:
                counter += 1

        if counter >= low and counter <= high:
            valid += 1
    return valid


def part_two(input):
    valid = 0
    for line in input:
        rule, pwd = [str(s).strip() for s in (line).split(':')]
        pwd_range, char = rule.split(' ')
        low, high = [int(v) for v in pwd_range.split('-')]
        counter = 0
        for i in range(len(pwd)):
            if (i+1) == low or (i+1) == high:
                if pwd[i] == char:
                    counter += 1
            if counter > 1:
                break

        if counter == 1:
            valid += 1
    return valid


if __name__ == '__main__':
    input = loadInput('input.txt')
    print(part_two(input))
