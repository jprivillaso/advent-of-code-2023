file = open('./input.txt')

def parse_line(code): 
  first_digit = None
  last_digit = None

  for i in code:
    if i.isdigit() and first_digit is None:
      first_digit = i
      last_digit = i
    elif i.isdigit():
      last_digit = i

  return int(f"{first_digit}{last_digit}")

sum = 0
for line in file:
    [code] = line.strip().split()
    sum += parse_line(code)

print(sum)