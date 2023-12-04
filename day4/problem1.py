from collections import defaultdict

file = open('./day4/input.txt')

def is_empty(str):
  return str != "" and str != " "

def count_points(line):
  _, card_info = line.split(":")
  [winning_cards, my_cards] = card_info.strip().split("|")
  winning_set = set(filter(is_empty, winning_cards.split(" ")))
  my_cards_set = set(filter(is_empty, my_cards.split(" ")))

  result = winning_set - my_cards_set
  return pow(2, len(winning_set) - len(result) - 1) if len(winning_set) != len(result) else 0

total = 0
for line in file:
  code = line.strip()
  total += count_points(code)

print(total)
