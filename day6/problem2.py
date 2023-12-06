from collections import defaultdict
from functools import reduce

file = open('./day6/input.txt')

def parse_line(time, distance):
  counter = 0

  for i in range(1, time):
    if i * (time - i) > distance:
      counter += 1

  return counter

[_, time] = next(file).split(":")
[_, distance] = next(file).split(":")

race_map = defaultdict()
times = list(map(lambda x: x.strip(), list(filter(lambda x: x.strip(), time.split(" ")))))
distances = list(map(lambda x: x.strip(), list(filter(lambda x: x.strip(), distance.split(" ")))))

time = int("".join(times))
distance = int("".join(distances))
print(parse_line(time, distance))
