from queue import Queue

file = open('./day10/input2.txt')

def parse_line(line):
  None

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

def next_char_is_valid(matrix, o_i, o_j, next_i, next_j):
  return matrix[next_i][next_j] in valid_positions[(o_i, o_j)]

def is_valid(matrix, visited, o_i, o_j, next_i, next_j):
  return next_i >= 0 and next_i < len(matrix) and next_j >= 0 and next_j < len(matrix[0]) and (next_i, next_j) not in visited and next_char_is_valid(matrix, o_i, o_j, next_i, next_j)

def traverse(matrix):
  q = Queue()
  q.put((i, j, 0))

  visited = set()
  visited.add((i, j))

  offsets = [
    (-1, 0), # up
    (1, 0),  # down
    (0, -1), # left
    (0, 1) # right
  ]

  max_so_far = 0

  while not q.empty():
    (curr_i, curr_j, curr_distance) = q.get()

    for (o_i, o_j) in offsets:
      next_i = curr_i + o_i
      next_j = curr_j + o_j

      valid_move = is_valid(matrix, visited, o_i, o_j, next_i, next_j)

      if (valid_move):
        q.put((next_i, next_j, curr_distance + 1))
        visited.add((next_i, next_j))
        max_so_far = max(max_so_far, curr_distance + 1)

  return max_so_far

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if (matrix[i][j] == "S"):
      print(traverse(matrix))
