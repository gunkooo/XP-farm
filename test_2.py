def escape(carpark):
    # Code here
    result = []
    start = carpark[0].index(2)
    D_num = 0
    for floor in carpark:
        if 1 in floor:
            D_index = floor.index(1)
            move = start - D_index
            if (D_num > 0) and move != 0:
                result.append("D" + str(D_num))
                D_num = 0
            if move > 0:
                result.append("L" + str(move))
                start = D_index
            elif move < 0:
                result.append("R" + str(abs(move)))
                start = D_index
            elif move == 0:
                D_num += 1
        else:
            move = abs(start - (len(floor) - 1))
            if move > 0:
                result.append("R" + str(move))
            return result



carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

print(escape(carpark))