def escape(carpark):
    # Code here
    result = []

    # searching start position in carpark
    # 8. The start level may be any level of the car park.
    for i in range(len(carpark)):
        if 2 in carpark[i]:
            start = carpark[i].index(2)
            break

    D_num = 0

    # starting from the floor where start position was found... number 2
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