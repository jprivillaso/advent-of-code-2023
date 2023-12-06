from collections import defaultdict

file = open('./day5/input2.txt')

seed_ids = list(map(lambda n: n.replace("\n", ""), next(file).split(" ")[1:]))

def parse_input(file):
  current_map_id = None
  input_map = defaultdict(list)

  for line in file:
    code = line.strip()
    if (code == ""): continue

    if (code.find("map") != -1):
      map_id = code.split(" ")[0]
      current_map_id = map_id
    else:
      input_map[current_map_id].append(code.split(" "))

  return input_map

def create_ranges_map(input_map):
  ranges_map = defaultdict(defaultdict)

  for [k, v] in input_map.items():
    for [destination, origin, length] in v:
      ranges_map[k][(int(origin), int(origin) + int(length))] = int(destination)

  return ranges_map

def get_locations(ranges_map, seed_ids):
  maps_to_iterate = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
  locations = defaultdict()

  for seed in seed_ids:
    current_value = seed
    for m in maps_to_iterate:
      for [(origin_a, origin_b), destination] in ranges_map[m].items():
        if int(current_value) >= origin_a and int(current_value) <= origin_b:
          delta = int(current_value) - origin_a + destination
          current_value = delta
          break

    locations[seed] = current_value

  return locations

input_map = parse_input(file)
ranges_map = create_ranges_map(input_map)
locations = get_locations(ranges_map, seed_ids)
print(min(locations.values()))


