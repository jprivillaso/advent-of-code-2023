from queue import Queue

file = open('./day11/input2.txt')

def traverse_cols(matrix):
  empty_cols = set()

  for i in range(len(matrix)):
    empty = True

    for j in range(len(matrix[0])):
      if matrix[j][i] == "#":
        empty = False
        break

    if (empty):
      empty_cols.add(i)

  return empty_cols

def traverse_rows(matrix):
  empty_rows = set()

  for i in range(len(matrix)):
    is_empty = len(list(filter(lambda x: x == "#", matrix[i]))) == 0
    if is_empty:
      empty_rows.add(i)

  return empty_rows

def find_galaxies(matrix):
  galaxies = []

  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if (matrix[i][j] == "#"):
        galaxies.append((i, j))

  return galaxies

def find_pairs(galaxies):
  pairs = []

  for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
      pairs.append((galaxies[i], galaxies[j]))

  return pairs

def find_min_paths(origin, target, empty_rows, empty_cols):
  (origin_i, origin_j) = origin
  (target_i, target_j) = target

  min_i, min_j = min([origin_i, target_i]), min([origin_j, target_j])
  max_i, max_j = max([origin_i, target_i]), max([origin_j, target_j])

  crossed_rows = list(filter(lambda x: x >= min_i and x <= max_i, empty_rows))
  crossed_cols = list(filter(lambda x: x >= min_j and x <= max_j, empty_cols))
  multiplier = 1000000 - 1

  return abs(target_j - origin_j) + abs(target_i - origin_i) + multiplier * len(crossed_rows) + multiplier * len(crossed_cols)

matrix = []
for line in file:
  line = list(line.strip())
  matrix.append(line)

empty_rows = traverse_rows(matrix)
empty_cols = traverse_cols(matrix)
galaxies = find_galaxies(matrix)
pairs = find_pairs(galaxies)

print("empty rows", empty_rows)
print("empty cols", empty_cols)

total = 0
for p in pairs:
  (origin, target) = p
  min_distance = find_min_paths(origin, target, empty_rows, empty_cols)
  total += min_distance
  print(f"distance between {origin} and {target} is {min_distance}. New Total: {total}")

print(total)