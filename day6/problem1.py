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
times = list(map(lambda x: int(x.strip()), list(filter(lambda x: x.strip(), time.split(" ")))))
distances = list(map(lambda x: int(x.strip()), list(filter(lambda x: x.strip(), distance.split(" ")))))

for i in range(len(times)):
  race_map[times[i]] = distances[i]

res = defaultdict()
for t, d in race_map.items():
  res[t] = parse_line(t, d)

print(reduce(lambda a, b: a*b, res.values()))
