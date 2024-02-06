
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# def type(string):
#   for c
#  in string:
#     if 

def priorities(alphabet, start):
  scores = dict()
  for char in alphabet:
    scores[char] = start
    start += 1
  return scores
  
def rucksack(path, dict):
  priority_dict = dict
  score = 0
  with open(path, 'r') as f:
    for line in f:
      pack = line.strip()
      pouch1 = pack[0:(int(len(pack) / 2))]
      pouch2 = pack[(int(len(pack) / 2)):int(len(pack))]
      intersection = ''.join(set(pouch1).intersection(pouch2))
      line_score = priority_dict.get(intersection)
      score += line_score
  return score

def main():
  path = "../inputs/d3.txt"
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabet_caps = alphabet.upper()

  dict1 = priorities(alphabet, 1)
  dict2 = priorities(alphabet_caps, 27)
  merge = dict1 | dict2
  score = rucksack(path, merge)
  print(score)
  # priority = sorted(merge.items(), key=lambda item: item[1])
  # print(priority)
  # score = rucksack(path, priority)
  # print(score)




if __name__ == "__main__":
  main()





# intersection = ''.join(set(pouch1).intersection(pouch2))