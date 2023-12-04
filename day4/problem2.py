from collections import defaultdict

file = open('./day4/input.txt')

def is_empty(str):
  return str != "" and str != " "

def count_points(line, card_map):
  card_title, card_info = line.split(":")
  card_name = card_title.split(" ").pop()
  [winning_cards, my_cards] = card_info.strip().split("|")
  winning_set = set(filter(is_empty, winning_cards.split(" ")))
  my_cards_set = set(filter(is_empty, my_cards.split(" ")))

  result = winning_set - my_cards_set
  matching_numbers = len(winning_set) - len(result) if len(winning_set) != len(result) else 0

  card_id = int(card_name)
  card_map[card_id] += 1

  if matching_numbers == 0:
    return 0

  for i in range(card_id + 1, card_id + matching_numbers + 1):
    card_map[i] += card_map[card_id]

card_map = defaultdict(int)

for line in file:
  code = line.strip()
  count_points(code, card_map)

print(sum(card_map.values()))
