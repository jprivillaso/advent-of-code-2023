file = open('./day13/input.txt')

def parse_horizontal(m):
  coords = []

  for i in range(len(m) - 1):
    if m[i] == m[i + 1]:
      coords.append((i, i + 1))

  if len(coords) == 0:
    return -1

  for coord in coords:
    (start, end) = coord

    valid = True
    while start >= 0 and end < len(m):
      if (m[start] != m[end]):
        valid = False
        break

      start -= 1
      end += 1

    if (valid):
      return coord[1]

  return -1

def parse_vertical(m):
  # transpose
  new_matrix = [*zip(*m)]
  return parse_horizontal(new_matrix)

data = []
curr_matrix = []

for line in file:
  code = line.strip().split()

  if len(code) > 0:
    curr_matrix.append(code[0])
  else:
    data.append(curr_matrix)
    curr_matrix = []

data.append(curr_matrix)

total = 0
for d in data:
  row = parse_horizontal(d)
  col = parse_vertical(d)

  if row != -1:
    total += row * 100

  if col != -1:
    total += col

print(total)
