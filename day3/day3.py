def loadInput(filename):
    file = open(filename)
    return [str(line.rstrip('\n')) for line in file]


def part_one(input, slope):
    x, y = [s for s in slope]
    i = j = 0
    max_x = len(input[0])
    max_y = len(input)
    trees = 0
    while j < max_y - y:
        i = (i + x) % max_x
        j = j + y
        if input[j][i] == '#':
            trees += 1
    return trees


def part_two(input, slopes):
    counter = 1
    for slope in slopes:
        counter *= part_one(input, slope)
    return counter


if __name__ == '__main__':
    input = loadInput('input.txt')
    print(part_one(input, [3, 1]))
    print(part_two(input, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))
