from queue import Queue

file = open('./day16/input.txt')

matrix = []
for line in file:
  code = line.strip()
  matrix.append(list(code))

def valid(matrix, visited, o_i, o_j, next_i, next_j):
  return next_i >= 0 and next_i < len(matrix) and next_j >= 0 and next_j < len(matrix[0]) and (next_i, next_j, o_i, o_j) not in visited

def find_initial_direction(matrix):
  origin = matrix[0][0]

  if (origin == "."  or origin == "-" ):
    return (0, 1)
  elif (origin == "\\" or origin == "|"):
    return (1, 0)
  else:
    return (-1, 0)


def bfs(matrix, visited):
  # start moving right
  curr_direction = find_initial_direction(matrix)
  q = Queue()
  q.put(((0,0), curr_direction))
  visited.add((0, 0, curr_direction[0], curr_direction[1]))

  while not q.empty():
    (curr_pos, curr_direction) = q.get()

    curr_i, curr_j = curr_pos
    o_i, o_j = curr_direction
    next_i, next_j = curr_i + o_i, curr_j + o_j

    if valid(matrix, visited, o_i, o_j, next_i, next_j):
      # we marked this as visited but we don't append it to the queue
      visited.add((next_i, next_j, o_i, o_j))

      if (matrix[next_i][next_j] == "."):
        q.put(((next_i, next_j), curr_direction))

      # moving horizontally
      if (matrix[next_i][next_j] == "-" and o_j != 0):
        q.put(((next_i, next_j), curr_direction))

      # moving horizontally
      if (matrix[next_i][next_j] == "|" and o_j != 0):
        q.put(((next_i, next_j), (-1, 0)))
        q.put(((next_i, next_j), (1, 0)))

      # moving right
      if (matrix[next_i][next_j] == "\\" and o_j == 1):
        # go down
        q.put(((next_i, next_j), (1, 0)))

      # moving right
      if (matrix[next_i][next_j] == "/" and o_j == 1):
        # go up
        q.put(((next_i, next_j), (-1, 0)))

      # moving left
      if (matrix[next_i][next_j] == "\\" and o_j == -1):
        # go up
        q.put(((next_i, next_j), (-1, 0)))

      # moving left
      if (matrix[next_i][next_j] == "/" and o_j == -1):
        # go down
        q.put(((next_i, next_j), (1, 0)))

      # moving vertically
      if (matrix[next_i][next_j] == "-" and o_i != 0):
        q.put(((next_i, next_j), (0, -1)))
        q.put(((next_i, next_j), (0, 1)))

      # moving vertically
      if (matrix[next_i][next_j] == "|" and o_i != 0):
        q.put(((next_i, next_j), curr_direction))

      # moving up
      if (matrix[next_i][next_j] == "/" and o_i == -1):
        # go right
        q.put(((next_i, next_j), (0, 1)))

      # moving down
      if (matrix[next_i][next_j] == "/" and o_i == 1):
        # go left
        q.put(((next_i, next_j), (0, -1)))

      # moving up
      if (matrix[next_i][next_j] == "\\" and o_i == -1):
        # go left
        q.put(((next_i, next_j), (0, -1)))

      # moving down
      if (matrix[next_i][next_j] == "\\" and o_i == 1):
        # go right
        q.put(((next_i, next_j), (0, 1)))

visited = set()
bfs(matrix, visited)

vis = [[" " for _ in i] for i in matrix]

for (i, j, _, _) in visited:
  if i >= 0 and i < len(vis) and j >= 0 and j < len(vis[0]):
    vis[i][j] = "#"

total = 0
for row in vis:
  print(row)
  for col in row:
    if col == "#":
      total += 1

print(total)