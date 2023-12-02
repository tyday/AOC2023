import re

data = []
with open("data.txt") as f:
    for line in f:
        data.append(line)
red = 12
green = 13
blue = 14

part_one_total = 0

for game in data:
    game_data = game.split(":")
    game_number = game_data[0][4:].strip()
    values = re.split(r',|;', game_data[1])
    possible = True
    for value in values:
        value = value.strip()
        quantity = int(value.split(" ")[0])
        color = value.split(" ")[1]
        if color.strip() == 'red':
            if quantity > red:
                possible = False
                break
        if color.strip() == 'green':
            if quantity > green:
                possible = False
                break
        if color.strip() == 'blue':
            if quantity > blue:
                possible = False
                break
    if possible:
        part_one_total +=  int(game_number)

print("Part one total: " + str(part_one_total))

# Part Two
part_two_total = 0
for game in data:
    game_data = game.split(":")
    game_number = game_data[0][4:].strip()
    values = re.split(r',|;', game_data[1])

    max_red = 0
    max_green = 0
    max_blue = 0

    for value in values:
        value = value.strip()
        quantity = int(value.split(" ")[0])
        color = value.split(" ")[1]
        if color.strip() == 'red':
            if quantity > max_red:
                max_red = quantity
        elif color.strip() == 'green':
            if quantity > max_green:
                max_green = quantity

        elif color.strip() == 'blue':
            if quantity > max_blue:
                max_blue = quantity


    part_two_total += max_red * max_blue * max_green

print("Part two total = " + str(part_two_total))