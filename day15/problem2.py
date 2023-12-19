from collections import defaultdict

file = open('./day15/input2.txt')

def hash_code(code, boxes, positions_map):
  data = None
  sign = None

  if code.find("=") != -1:
    data = code.split("=")
    sign = "="
  else:
    sign = "-"
    data = code.split("-")

  label = data[0]

  box_index = 0
  for c in label:
    ascii_code = ord(c)
    box_index += ascii_code
    box_index = (box_index * 17) % 256

  if sign == "-":
    if label in positions_map:
      label_index_in_boxes = positions_map[label]
      del boxes[box_index][label_index_in_boxes]
      del positions_map[label]

      # recompute positions for that box
      for i in range(len(boxes[box_index])):
        positions_map[boxes[box_index][i][0]] = i
  else:
    focal_len = data[1]

    if label not in positions_map:
      boxes[box_index].append((label, focal_len))
      positions_map[label] = len(boxes[box_index]) - 1
    else:
      label_index_in_boxes = positions_map[label]
      boxes[box_index][label_index_in_boxes] = ((label, focal_len))

boxes = [[] for _ in range(256)]
positions_map = defaultdict()

for line in file:
  codes = line.strip().split(",")

  for code in codes:
    hash_code(code, boxes, positions_map)

total = 0
for i in range(len(boxes)):
  box = boxes[i]

  for j in range(len(box)):
    total += (i+1) * (j+1) * int(box[j][1])

print(total)