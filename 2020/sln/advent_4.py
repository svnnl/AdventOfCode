import re

with open("../data/advent_4.txt") as f:
    data = [i.replace("\n", " ") for i in f.read().split("\n\n")]

passports = []
integer_fields = ["byr", "iyr", "eyr"]
string_fields = ["hgt", "hcl", "ecl", "pid"]
required_fields = integer_fields + string_fields

for i in data:
    passport = {}
    for field in i.split(" "):
        key, value = field.split(":")
        if key in integer_fields:
            value = int(value)
        else:
            value = str(value)
        passport[key] = value
    passports.append(passport)


def solve(validation):
    count = 0

    for passport in passports:
        error_log = []
        if not required_fields - passport.keys():
            if validation:
                if not 1920 <= passport["byr"] <= 2002:
                    error_log.append("Birth Year is not in between 1920 and 2002")

                if not 2010 <= passport["iyr"] <= 2020:
                    error_log.append("Issue Year is not in between 2010 and 2020")

                if not 2020 <= passport["eyr"] <= 2030:
                    error_log.append("Expiration year is not in between 2020 and 2030")

                unit = passport["hgt"][-2:]
                if unit not in ["cm", "in"]:
                    error_log.append("Height string does not contain cm or in")
                if (
                    unit == "cm"
                    and not 150 <= int(passport["hgt"].replace(unit, "")) <= 193
                ) or (
                    unit == "in"
                    and not 59 <= int(passport["hgt"].replace(unit, "")) <= 76
                ):
                    error_log.append("Height not within the boundaries")

                if not re.compile("^#[a-f0-9]{6}$").fullmatch(passport["hcl"]):
                    error_log.append("Hair color does not match Regex")

                if passport["ecl"] not in [
                    "amb",
                    "blu",
                    "brn",
                    "gry",
                    "grn",
                    "hzl",
                    "oth",
                ]:
                    error_log.append("Eye color not recognised")

                if not re.compile("^[0-9]{9}$").fullmatch(passport["pid"]):
                    error_log.append("PID not the correct size")

                if not error_log:
                    count += 1
                else:
                    print("Found some errors: \n {0}".format(error_log))

            else:
                count += 1

    return count


print("Answer to Part 1: {0}".format(solve(False)))
print("Answer to Part 2: {0}".format(solve(True)))
