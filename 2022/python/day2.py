# Day 2

# scoring: paper: 1, rock: 2, scissors: 3
# + 3 for draw, 6 for win, 0 for loss

choices = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {'win': 6, 'draw': 3, 'loss': 0}
match = {'X': 'A', 'Y': 'B', 'Z': 'C'}

beats = {'Y': 'A', 'Z': 'B', 'X': 'C'}

def calc_winner(opponent, player):
    if match.get(player) == opponent:
        return 'draw'
    elif beats.get(player) == opponent:
        return 'win'
    else:
        return 'loss'
    
def game(file):
    total = 0
    with open(file, 'r') as f:
        for l in f:
            opponent_choice, player_choice = l.strip().split()
            choice_score = choices[player_choice]
            result = calc_winner(opponent_choice, player_choice)
            result_score = outcomes[result]
            game = choice_score + result_score
            # print("player choice: ", player_choice)
            # print("opponent choice: ", opponent_choice)
            # print("game score: ", game)
            total += game
    return total


file = '../inputs/d2.txt'
total_score = game(file)
print(f"Total Score: {total_score}")