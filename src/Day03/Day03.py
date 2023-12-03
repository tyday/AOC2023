from helper.FileHelper import file_helper
from Numbers import Number


def parse_line(line, y, number_list):
    parsing_digit = False
    x = 0
    number = Number()
    while x < len(line):
        if parsing_digit:
            if line[x].isnumeric():
                number.add(line[x], x, y)
            else: # line[x] == '.':
                parsing_digit = False
                number.finalize()
                number_list.append(number)
                number = Number()
            # else:
            #     pass
        elif not parsing_digit:
            if line[x].isnumeric():
                number.add(line[x], x, y)
                parsing_digit = True
        x += 1
    if parsing_digit:
        number.finalize()
        number_list.append(number)



def main(filename):
    data = file_helper(filename)
    # print(data)
    number_list = []
    y = 0
    for line in data:
        parse_line(line, y, number_list)
        y = y + 1

    # print(number_list)
    total = 0
    for number in number_list:
        # print(number.textual_value + str(number.get_neighbor_symbols(data)))
        if len(number.get_neighbor_symbols(data)) > 0:
            print(number.textual_value)
            total += number.value
        # else:
            # print(number.textual_value + " no value")
    print (f"total for part one: {total}")

    numbers_with_gears = {}
    for number in number_list:
        if len(number.gears) == 1:
            pos = number.gears.pop()
            if pos in numbers_with_gears:
                numbers_with_gears[pos].append(number.value)
            else:
                numbers_with_gears[pos] = [number.value]
        elif len(number.gears) > 1:
            Exception("Too many gears")
        else:
            pass

    total = 0
    for k,v in numbers_with_gears.items():
        if len(v) > 1:
            total += v[0] * v[1]
    print(f"Part two total: {total}")



if __name__  == "__main__":
    main("data.txt")