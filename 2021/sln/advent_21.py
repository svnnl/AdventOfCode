with open("../data/advent_21.txt") as f:
    positions = [int(i.split(":")[1]) for i in f.read().splitlines()]

player_scores = [0, 0]

values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def roll_dice(index, score, position, dice):
    dice_values = [dice, dice + 1, dice + 2]
    for i, value in enumerate(dice_values):
        if value > 100:
            dice_values[i] = value % 100
    print(dice_values)
    position = (position + sum(dice_values)) % 10
    score += values[position]
    dice = dice_values[-1] + 1
    print(
        "Player {0} rolls {1} and moves to space {2} for a total score of {3}".format(
            index, dice_values, position, score
        )
    )

    return [score, position, dice]


dice = 1
throws = 0
turns = 1
finished = False

while not finished:
    print("--------------------Turn {0}-------------------".format(turns))
    for index, score in enumerate(player_scores):
        player_scores[index], positions[index], dice = roll_dice(
            index + 1, score, positions[index], dice
        )

        throws += 3

        if any(score >= 1000 for score in player_scores):
            finished = True
            break

    turns += 1

print("Answer to Part 1 is: {0}".format(throws * min(player_scores)))
