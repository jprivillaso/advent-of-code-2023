from collections import defaultdict
from functools import reduce
import math

file = open('./day8/input.txt')

def find_origins(desert_map):
  origins = []

  for k in desert_map.keys():
    if k[-1] == "A":
      origins.append(k)

  return origins

def find_z_target(desert_map, start, directions):
  curr = start
  pointer = 0
  length = len(directions)
  counter = 0

  while curr[-1] != 'Z':
    counter += 1
    curr = desert_map[curr][int(directions[pointer % length])]
    pointer += 1

  return counter

from functools import reduce

def lcm(arr):
  l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
  return l

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

origins = find_origins(desert_map)

times_to_z = []
for o in origins:
  times_to_z.append(find_z_target(desert_map, o, directions))

print(lcm(times_to_z))