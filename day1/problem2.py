from collections import defaultdict
import re

file = open('./input.txt')

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
translate = {'one': '1','two': '2','three': '3','four': '4','five': '5', 'six': '6', 'seven': '7', 'eight': '8','nine': '9'}

def parse_line(code):
  pos_map = defaultdict(list)

  for n in numbers:
    indexes = [x.start() for x in re.finditer(n, code)]

    if len(indexes) == 0:
      continue

    if n in translate:
      pos_map[translate[n]] = pos_map[translate[n]] + indexes
    else:
      pos_map[n] = pos_map[n] + indexes

  global_min = None
  global_min_key = None
  global_max = None
  global_max_key = None

  for [n, indexes] in pos_map.items():
    local_min = min(indexes)
    local_max = max(indexes)

    if global_min is None or local_min < global_min:
      global_min = local_min
      global_min_key = n

    if global_max is None or local_max > global_max:
      global_max = local_max
      global_max_key = n

  return int(f"{global_min_key}{global_max_key}")

sum = 0
for line in file:
    [code] = line.strip().split()
    sum += parse_line(code)

print(sum)
