def add_matrix(row = 5, col =4):
   matrix = []
   for _ in range(row):
      row_str = input(f'Ведите {col-1} элементов через пробел: ').split(' ')
      row = [int(i) for i in row_str]
      row.append(sum(row))
      matrix.append(row)
   return matrix

def show(mtrx):
   for row in mtrx:
      print(row)


if __name__ == '__main__':
   show(add_matrix())

