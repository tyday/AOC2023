

def get_neighbors(self, digit, data):
    # Returns the values of neighboring cells in a grid
    # digit = (x,y) tuple
    # data = grid

    pos = digit.pos
    neighbors = []
    for x in range(-1,2):
        for y in range(-1,2):
            neighbor_pos = (pos[0] + y, pos[1] + x)
            if neighbor_pos[0] > -1 and neighbor_pos[0] < len(data[0]):
                if neighbor_pos[1] > -1 and neighbor_pos[1] < len(data):
                    neighbors.append(neighbor_pos)
    return neighbors

