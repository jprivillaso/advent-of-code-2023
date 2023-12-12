file = open('./day9/input2.txt')

def parse_line(line):
  line = list(map(lambda x: int(x), line))
  curr = line
  acc = [line]

  while set(curr) != {0}:
    temp = []
    for i in range(len(curr) - 1):
      temp.append(curr[i + 1] - curr[i])

    curr = temp
    acc.append(curr)

  p1 = 0
  for seq in acc[::-1]:
    p1 = seq[0] - p1

  return p1

total = 0
for line in file:
  total += parse_line(line.strip().split())

print(total)