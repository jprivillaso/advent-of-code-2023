from collections import defaultdict

file = open('./day8/input.txt')

def find_z_target(desert_map, directions):
  curr = 'AAA'
  pointer = 0
  length = len(directions)
  counter = 0

  while curr != 'ZZZ':
    counter += 1
    curr = desert_map[curr][int(directions[pointer % length])]
    pointer += 1

  return counter

directions_str = next(file).strip()
directions_str = directions_str.replace("L", '0')
directions_str = directions_str.replace("R", '1')
directions = list(directions_str)
next(file) # empty line

desert_map = defaultdict()
for line in file:
  [origin, target] = line.strip().split("=")
  [target1, target2] = target.replace("(", "").replace(")", "").strip().split(",")
  target1 = target1.strip()
  target2 = target2.strip()
  desert_map[origin.strip()] = [target1, target2]

print(find_z_target(desert_map, directions))
