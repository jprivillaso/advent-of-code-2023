from queue import Queue

file = open('./day10/input2.txt')

matrix = []
for line in file:
  line = list(line.strip())
  matrix.append(line)

valid_positions = {
  (-1, 0): set(['|', 'F', '7']), # up
  (1, 0): set(['|', 'L', 'J']),  # down
  (0, -1): set(['-', 'L', 'F']), # left
  (0, 1): set(['-', 'J', '7']) # right
}

edges = {"J", "L", "F", "7"}
edge_direction = {"L": 1, "7": 1, "J": -1, "F": -1}

def is_valid(matrix, o_i, o_j, next_i, next_j):
  return next_i >= 0 and next_i < len(matrix) and next_j >= 0 and next_j < len(matrix[0]) and matrix[next_i][next_j] in valid_positions[(o_i, o_j)]

def shoelace(positions):
  x, y = zip(*positions)
  return 0.5 * abs(
    sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(positions)))
  )

def calculate_next_direction(row_offset, col_offset, pipe):
  mult = {"L": 1, "7": 1, "J": -1, "F": -1}
  return col_offset * edge_direction[pipe], row_offset * edge_direction[pipe]

def get_ordered_coords(matrix, i, j):
  offsets = [
    (-1, 0), # up
    (1, 0),  # down
    (0, -1), # left
    (0, 1) # right
  ]

  dir_row, dir_col = None, None

  for (o_i, o_j) in offsets:
    next_i = i + o_i
    next_j = j + o_j
    if is_valid(matrix, o_i, o_j, next_i, next_j):
      dir_row = o_i
      dir_col = o_j
      break

  loop = []
  start = (i, j)
  current = start

  while current != start or not loop:
    loop.append(current)
    row, col = current
    current = (row + dir_row, col + dir_col)
    curr_value = matrix[current[0]][current[1]]

    if curr_value in edges:
      dir_row, dir_col = dir_col * edge_direction[curr_value], dir_row * edge_direction[curr_value]

  return loop

def traverse(matrix, i, j):
  q = Queue()
  q.put((i, j))

  path = get_ordered_coords(matrix, i, j)
  return int(shoelace(path) - len(path) / 2 + 1)

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if (matrix[i][j] == "S"):
      print(traverse(matrix, i, j))