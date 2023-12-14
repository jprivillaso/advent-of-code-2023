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

def expand_matrix(matrix, special_rows, special_cols):
  new_matrix = []

  for i in range(len(matrix)):
    if i in special_rows:
      row = []
      for j in range(len(matrix[0])):
        row.append(".")

        if j in special_cols:
          row.append(".")

      new_matrix.append(row)
      new_matrix.append(row)
    else:
      row = []
      for j in range(len(matrix[0])):
        row.append(matrix[i][j])

        if j in special_cols:
          row.append(".")

      new_matrix.append(row)

  return new_matrix

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

def find_min_paths(origin, target):
  (origin_i, origin_j) = origin
  (target_i, target_j) = target

  return abs(target_j - origin_j) + abs(target_i - origin_i)

matrix = []
for line in file:
  line = list(line.strip())
  matrix.append(line)

empty_rows = traverse_rows(matrix)
empty_cols = traverse_cols(matrix)
expanded_matrix = expand_matrix(matrix, empty_rows, empty_cols)
galaxies = find_galaxies(expanded_matrix)
print("Galaxies")
print(len(galaxies))
pairs = find_pairs(galaxies)
print("Pairs")
print(len(pairs))

total = 0
for p in pairs:
  (origin, target) = p
  min_distance = find_min_paths(origin, target)
  total += min_distance
  print(f"distance between {origin} and {target} is {min_distance}. New Total: {total}")

print(total)