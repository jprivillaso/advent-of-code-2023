from collections import defaultdict
from collections import Counter

file = open('./day7/input2.txt')

scores = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}

type_scores = {
  "five_of_a_kind": 7,
  "four_of_a_kind": 6,
  "full_house": 5,
  "three_of_a_kind": 4,
  "two_pair": 3,
  "one_pair": 2,
  "high_card": 1,
}

class Comparator(tuple):
  def __lt__(self, other):
    [curr_hand, curr_score] = self
    [next_hand, next_score] = other

    if curr_score < next_score:
      return True
    elif curr_score > next_score:
      return False

    lower = False

    for j in range(len(curr_hand)):
      curr_char_score = scores[curr_hand[j]]
      next_char_score = scores[next_hand[j]]

      if curr_char_score == next_char_score:
        continue

      if curr_char_score < next_char_score:
        lower = True
      else:
        lower = False

      break

    return lower

def categorize_hand(hand):
  global_max = None
  global_max_hand = None

  for i in hand:
    temp_hand = hand.replace('J', i)

    count_map = Counter(list(temp_hand))
    matches = list(count_map.values())
    matches.sort()

    score = None
    if matches == [5]:
      score = type_scores["five_of_a_kind"]
    elif (matches == [1, 4]):
      score = type_scores["four_of_a_kind"]
    elif (matches == [2, 3]):
      score = type_scores["full_house"]
    elif (matches == [1, 1, 3]):
      score = type_scores["three_of_a_kind"]
    elif (matches == [1, 2, 2]):
      score = type_scores["two_pair"]
    elif (matches == [1, 1, 1, 2]):
      score = type_scores["one_pair"]
    elif (matches == [1, 1, 1, 1, 1]):
      score = type_scores["high_card"]

    if global_max_hand is None or score > global_max:
      global_max = score
      global_max_hand = temp_hand

  return global_max

hand_to_bid = defaultdict()
for line in file:
  [hand, bid] = line.strip().split()
  hand_to_bid[hand] = int(bid)

hand_scores = {}
for [hand, bid] in hand_to_bid.items():
  hand_scores[hand] = categorize_hand(hand)

sorted_scores = dict(sorted(hand_scores.items(), key=Comparator))
sorted_keys = list(sorted_scores.keys())

total = 0
counter = 1
for hand in sorted_keys:
  total += counter * hand_to_bid[hand]
  counter += 1

print(total)
