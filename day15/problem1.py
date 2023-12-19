file = open('./day15/input.txt')

def hash_code(code):
  total = 0

  for c in code:
    ascii_code = ord(c)
    total += ascii_code
    total = (total * 17) % 256

  return total

total = 0
for line in file:
  codes = line.strip().split(",")

  for code in codes:
    total += hash_code(code)

print(total)
