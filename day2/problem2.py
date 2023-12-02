from functools import reduce

file = open('./input.txt')

limits = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def parse_line(code):
  [_, game_info] = code.split(":")
  game_sets = game_info.strip().split(";")

  max_values = {}
  for game_set in game_sets:
    pieces = game_set.strip().split(",")

    for piece in pieces:
      [n, color] = piece.strip().split(" ")

      curr = max_values.get(color, 0)

      if color not in max_values or int(n) > curr:
        max_values[color] = int(n)

  power_set = reduce((lambda x, y: x * y), max_values.values())

  return power_set

total = 0
for line in file:
  code = line.strip()
  total += parse_line(code)

print(total)
