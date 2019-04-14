def cut_fruits(fruits):
    # FRUIT_NAMES is preloded
    list = []
    for fruit in fruits:
      if fruit in FRUIT_NAMES:
        middle = len(fruit) // 2
        list.append(fruit[:len(fruit) - middle])
        list.append(fruit[len(fruit) - middle:])
      else:
        list.append(fruit)
    return list