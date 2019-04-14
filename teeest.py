def escape(carpark):
    # Code here
    result = []
    for i in range(len(carpark)):
        if 2 in carpark[i]:
            start = carpark[i].index(2)
            break
#    start = carpark[0].index(2)
    D_num = 0
    for floor in carpark[i:]:
        if 1 in floor:
            D_index = floor.index(1)
            move = start - D_index
            if move > 0:
                result.append("L" + str(move))
                result.append("D1")
                start = D_index
            elif move < 0:
                result.append("R" + str(abs(move)))
                result.append("D1")
                start = D_index
            elif move == 0:
                result[-1] = "D" + str(int(result[-1][-1]) + 1)
        else:
            move = abs(start - (len(floor) - 1))
            if move > 0:
                result.append("R" + str(move))
            return result


carpark = [[0, 0, 0, 0, 1],
           [1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

print(escape(carpark))



