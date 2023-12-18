file = open('./day13/input2.txt')

def check_smudge(a, b):
  coords = []

  for i in range(len(a)):
    if a[i] != b[i]:
      coords.append(i)

  if len(coords) > 1:
    return (False, -1)

  if a[coords[0]] == "#":
    a = a[:coords[0]] + "." + a[coords[0] + 1:]
    return (a == b, coords[0])
  elif a[coords[0]] == ".":
    a = a[:coords[0]] + "#" + a[coords[0] + 1:]
    return (a == b, coords[0])

def parse_vertical(m, flag):
  # transpose
  new_matrix = [*zip(*m)]
  new_matrix = list(map(lambda x: "".join(x), new_matrix))
  return parse_horizontal(new_matrix, flag)

def parse_horizontal(m, prev_use_smudge):
  coords = []
  local_smudge_use = False

  for i in range(len(m) - 1):
    if m[i] == m[i + 1]:
      coords.append((i, i + 1))
    else:
      (is_smudge, smudge_idx) = (False, -1) if prev_use_smudge or local_smudge_use else check_smudge(m[i], m[i+1])

      if (is_smudge):
        m[i] = m[i+1][:smudge_idx] + m[i+1][smudge_idx] + m[i+1][smudge_idx+1:]
        coords.append((i, i + 1))
        local_smudge_use = True

  if len(coords) == 0:
    return (-1, local_smudge_use or prev_use_smudge)

  final_res = None

  for coord in coords:
    (start, end) = coord

    valid = True

    while start >= 0 and end < len(m):
      if (m[start] != m[end]):
        (valid_with_smudge, smudge_idx) = (False, -1) if prev_use_smudge or local_smudge_use else check_smudge(m[start], m[end])

        if (valid_with_smudge):
          local_smudge_use = True
          m[start] = m[end][:smudge_idx] + m[end][smudge_idx] + m[end][smudge_idx+1:]
          start -= 1
          end += 1
          continue

        valid = False
        break

      start -= 1
      end += 1

    if (valid):
      return (coord[1], local_smudge_use or prev_use_smudge)

  if final_res is not None:
    return final_res

  return (-1, local_smudge_use or prev_use_smudge)

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
rows = 0
cols = 0
counter = 0
for d in data:
  (row, row_flag) = parse_horizontal(d, False)
  (col, col_flag) = parse_vertical(d, row_flag)

  print(f"i {counter} row {row} col {-1 if row != -1 else col}")
  counter += 1

  if row != -1:
    total += row * 100
    rows += row * 100

  if row == -1 and col != -1:
    total += col
    cols += col

print(total)
