file = open('./day14/input.txt')

def point_north(matrix):
  for i in range(len(matrix)):
    # either a wall or an empty space
    empty_spaces = []

    for j in range(len(matrix[0])):
      if matrix[j][i] == "#":
        empty_spaces.clear()
        continue

      if matrix[j][i] == ".":
        empty_spaces.append((i, j))
        continue

      if matrix[j][i] == "O" and len(empty_spaces) > 0:
        [prev_i, prev_j] = empty_spaces.pop(0)
        matrix[j][i] = "."
        matrix[prev_j][prev_i] = "O"
        empty_spaces.append((i, j))

  return matrix

def point_west(matrix):
  for i in range(len(matrix)):
    # either a wall or an empty space
    empty_spaces = []

    for j in range(len(matrix[0])):
      if matrix[i][j] == "#":
        empty_spaces.clear()
        continue

      if matrix[i][j] == ".":
        empty_spaces.append((i, j))
        continue

      if matrix[i][j] == "O" and len(empty_spaces) > 0:
        [prev_i, prev_j] = empty_spaces.pop(0)
        matrix[i][j] = "."
        matrix[prev_i][prev_j] = "O"
        empty_spaces.append((i, j))

  return matrix

def point_south(matrix):
  row_length = len(matrix) - 1

  for i in range(len(matrix)):
    # either a wall or an empty space
    empty_spaces = []

    for j in range(row_length, -1, -1):
      if matrix[j][i] == "#":
        empty_spaces.clear()
        continue

      if matrix[j][i] == ".":
        empty_spaces.append((j, i))
        continue

      if matrix[j][i] == "O" and len(empty_spaces) > 0:
        [prev_i, prev_j] = empty_spaces.pop(0)
        matrix[j][i] = "."
        matrix[prev_i][prev_j] = "O"
        empty_spaces.append((j, i))

  return matrix

def point_east(matrix):
  col_length = len(matrix[0]) - 1

  for i in range(len(matrix)):
    # either a wall or an empty space
    empty_spaces = []

    for j in range(col_length, -1, -1):
      if matrix[i][j] == "#":
        empty_spaces.clear()
        continue

      if matrix[i][j] == ".":
        empty_spaces.append((i, j))
        continue

      if matrix[i][j] == "O" and len(empty_spaces) > 0:
        [prev_i, prev_j] = empty_spaces.pop(0)
        matrix[i][j] = "."
        matrix[prev_i][prev_j] = "O"
        empty_spaces.append((i, j))

  return matrix

def calculate_weight(matrix):
  transposed_matrix = [*zip(*matrix)]

  row_length = len(matrix[0])
  total = 0

  for row in transposed_matrix:
    weight = 0
    counter = 0
    for i in range(row_length):
      if row[i] == "O":
        weight += row_length - counter
      counter += 1

    total += weight

  return total

def my_add(a, b):
  result = a + b
  print(a, b)
  return result

numbers = [0, 1, 2, 3, 4]
matrix = []
for line in file:
  code = line.strip()
  matrix.append(list(code))

matrix = point_north(matrix)
print(calculate_weight(matrix))