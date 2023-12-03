from queue import Queue

file = open('./day3/input.txt')

def grab_number(matrix, visited, next_i, next_j):
  curr_digit = [matrix[next_i][next_j]]
  left_side = []
  right_side = []

  visited.add((next_i, next_j))

  # go left
  col_pointer = next_j - 1
  while col_pointer >= 0 and matrix[next_i][col_pointer].isdigit():
    if (next_i, col_pointer) in visited:
      break

    visited.add((next_i, col_pointer))
    left_side.append(matrix[next_i][col_pointer])
    col_pointer -= 1

  # go right
  col_pointer = next_j + 1
  while col_pointer < cols and matrix[next_i][col_pointer].isdigit():
    if (next_i, col_pointer) in visited:
      break

    visited.add((next_i, col_pointer))
    right_side.append(matrix[next_i][col_pointer])
    col_pointer += 1

  left_side.reverse()

  res = int("".join(left_side + curr_digit + right_side))

  return res

def visit_neighbor(matrix, visited, next_i, next_j):
  rows = len(matrix)
  cols = len(matrix[0])

  neighbor = []
  if next_i >= 0 and next_i < rows and next_j >= 0 and next_j < cols and matrix[next_i][next_j].isdigit():
    n = grab_number(matrix, visited, next_i, next_j)

    if n != "":
      neighbor.append(n)

  return neighbor

def find_valid_numbers(matrix, visited):
  q = Queue()

  # Find places where we have symbols to find the adjacent numbers
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      curr = matrix[i][j]

      if curr == "*" and not curr.isdigit():
        q.put((i, j))

  offsets = [
    (0, -1), # up
    (0, 1), # down
    (-1, 0), # left
    (1, 0), # right
    (-1, -1), # top left
    (1, -1), # top right
    (-1, 1), # down left
    (1, 1) # down right
  ]

  valid_numbers = []
  while not q.empty():
    (curr_i, curr_j) = q.get()

    adjacent_to_gear = []
    for (offset_i, offset_j) in offsets:
      next_i, next_j = (curr_i + offset_i, curr_j + offset_j)

      if (next_i, next_j) in visited:
        continue

      adjacent_to_gear += visit_neighbor(matrix, visited, next_i, next_j)

    if len(adjacent_to_gear) == 2:
      [num1, num2] = adjacent_to_gear
      valid_numbers += [num1 * num2]

  return valid_numbers

matrix = []
for line in file:
  code = line.strip()
  matrix.append(list(code))

rows = len(matrix)
cols = len(matrix[0])
visited = set()

print(sum(find_valid_numbers(matrix, visited)))
