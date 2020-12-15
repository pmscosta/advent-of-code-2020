def loadInput(filename):
    file = open(filename)
    return [int(line.rstrip('\n')) for line in file]


def part_one(input, target):
    rem = set()
    for expense in input:
        dif = target - expense
        if dif in rem:
            return dif * expense
        rem.add(expense)
    return -1


def part_two(input, target):
    for i, expense in enumerate(input):
        mid = part_one(input[:i] + input[(i+1):], target-expense)
        if mid != -1:
            return mid * expense
    return -1


if __name__ == '__main__':
    input = loadInput('input.txt')
    print(part_one(input, 2020))
    print(part_two(input, 2020))
