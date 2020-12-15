import re


def loadInput(filename):
    input = []
    passport = ""
    with open(filename) as f:
        line = None
        previous = next(f, None)
        for line in f:
            if previous in ['\n', '\r\n']:
                input.append(passport.strip())
                passport = ""
            else:
                passport += previous.strip() + " "
            previous = line
        if previous is not None:
            passport += previous.strip()
            input.append(passport.strip())

    return input


def part_one(input):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    invalid = 0
    for passport in input:
        for req in required:
            if passport.find(req) == -1:
                invalid += 1
                break
    return len(input) - invalid


def part_two(input):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    invalid = 0
    for passport in input:
        skip = False
        for req in required:
            if passport.find(req) == -1:
                invalid += 1
                skip = True
                break

        if not skip and not check_passport(passport):
            invalid += 1

    return len(input) - invalid


def check_passport(ppt):
    keys = {}
    for kv in ppt.split():
        kv = kv.split(':')
        key = kv[0]
        val = kv[1]
        keys[key] = val

    byr = keys['byr']
    if not check_range(byr, 1920, 2002):
        return False

    iyr = keys['iyr']
    if not check_range(iyr, 2010, 2020):
        return False

    eyr = keys['eyr']
    if not check_range(eyr, 2020, 2030):
        return False

    hgt = keys['hgt']
    if not check_hgt(hgt):
        return False

    hcl = keys['hcl']
    if not check_hcl(hcl):
        return False

    ecl = keys['ecl']
    if not check_ecl(ecl):
        return False

    pid = keys['pid']
    if not check_pid(pid):
        return False

    return True


def check_range(val, low, high):
    try:
        val = int(val)
    except:
        return False
    return low <= val <= high


def check_hgt(hgt):
    if str(hgt).find('in') != -1:
        return check_range(hgt.split('in')[0], 59, 76)
    elif str(hgt).find('cm') != -1:
        return check_range(hgt.split('cm')[0], 150, 193)
    return False


def check_hcl(hcl):
    return re.match(r"^#([0-9]|[a-f]){6}$", hcl)

def check_ecl(hcl):
    return re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", hcl)

def check_pid(pid):
    return re.match(r"^[0-9]{9}$", pid)


if __name__ == '__main__':
    input = loadInput('input.txt')
    print(part_one(input))
    print(part_two(input))
