def next_gen(cells):
    # Uncomment next line for an example output
    #return cells

    live_neigh = 0

    for row in range(len(cells)):
        for col in range(len(cells[0])):
            for rowMod in range(-1,2):
                for colMod in range(-1,2):
                    if ro

#Create a grid with a Beacon pattern
def beacon():
  grid = []
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,1,1,0,0,0,0,0])
  grid.append([0,0,0,1,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,1,0,0,0])
  grid.append([0,0,0,0,0,1,1,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  return grid