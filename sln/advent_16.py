import re


def check_ticket(ticket):
    invalid = []
    numbers = [int(i) for i in ticket.split(',')]
    for number in numbers:
        if not any(lower <= number <= upper for (lower, upper) in rules):
            invalid.append(number)
    return invalid


with open('../data/advent_16.txt') as f:
    data = f.read()

rules = []
for i in data.split('\n\n')[0].splitlines():
    found = re.findall(r"(([0-9]+)-([0-9]+))", i)
    rules.extend([(int(i), int(j)) for i, j in [range[0].split('-') for range in found]])

my_ticket = data.split('\n\n')[1].replace('your ticket:\n', '')

nearby_tickets = []
for i in data.split('\n\n')[2].splitlines():
    if 'tickets' not in i:
        nearby_tickets.append(i)

invalid_numbers = []
for ticket in nearby_tickets:
    invalid_values = check_ticket(ticket)
    if not len(invalid_values) == 0:
        nearby_tickets.remove(ticket)
    invalid_numbers.extend(invalid_values)

print(f'Answer to Part 1: {sum(invalid_numbers)}')

# Part 2
