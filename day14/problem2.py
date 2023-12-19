from collections import defaultdict

file = open('./day14/input2.txt')

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

def to_str(grid):
  return "".join(["".join(grid[i]) for i in range(len(grid))])

numbers = [0, 1, 2, 3, 4]
matrix = []
for line in file:
  code = line.strip()
  matrix.append(list(code))

cache = defaultdict()

total = 0

for i in range(1000000000):
  matrix = point_north(matrix)
  matrix = point_west(matrix)
  matrix = point_south(matrix)
  matrix = point_east(matrix)

  if to_str(matrix) in cache:
    print('found something in cache', i)
    total += cache[to_str(matrix)]

  cache[to_str(matrix)] = curr
  curr = calculate_weight(matrix)
  total += curr

print(total)