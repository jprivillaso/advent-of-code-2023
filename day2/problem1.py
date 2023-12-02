file = open('./input.txt')

limits = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def parse_line(code, valid_games):
  [game_name, game_info] = code.split(":")
  game_id = int(game_name.split(" ")[1].strip())
  game_sets = game_info.strip().split(";")

  valid_games.add(game_id)

  for game_set in game_sets:
    pieces = game_set.strip().split(",")

    valid = True
    for piece in pieces:
      [n, color] = piece.strip().split(" ")

      if (color in limits and int(n) > limits[color]):
        valid = False
        break

    if not valid:
      valid_games.remove(game_id)
      break

valid_games = set()

for line in file:
    code = line.strip()
    parse_line(code, valid_games)

print(sum(valid_games))
