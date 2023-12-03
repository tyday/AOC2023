def file_helper(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip())
    if data[-1] == '':
        data.pop()
    return data