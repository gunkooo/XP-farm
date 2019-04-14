def count_arara(n):
    # ...
    word = ''
    while n > 0:
      if n > 1 :
        word += ' adak'
        n -= 2
      else:
        word += ' anane'
        n -= 1
    return word[1:]
    pass