# Day 2

# scoring: paper: 1, rock: 2, scissors: 3
# + 3 for draw, 6 for win, 0 for loss

# part 2:
# X = lose, Y = draw, Z = win

# ex
# opp chooses Rock, needs to end in Y, or a draw. If Y, match opponent A = X
# if ends X = loss, pick what opponent beats (player chooses B paper, pick X rock)
# if ends Z = win, pick what Z wins => player chooses C scissors, pick X paper

choices = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {'win': 6, 'draw': 3, 'loss': 0}
match = {'X': 'A', 'Y': 'B', 'Z': 'C'}

beats = {'Y': 'A', 'Z': 'B', 'X': 'C'}

# Part 2
opp_wins = {'A': 'Z', 'B': 'X', 'C': 'Y'}
opp_loses = {'A': 'Y', 'B': 'Z', 'C': 'X'}
opp_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def calc_choice(opponent, outcome):
    if outcome == 'Y': # Draw
        player_choice = opp_draw.get(opponent)
        return player_choice
    elif outcome == 'X': # Lose
        player_choice = opp_wins.get(opponent)
        return opp_wins.get(opponent)
    elif outcome == 'Z': # Win
        player_choice = opp_loses.get(opponent)
        return player_choice

def calc_winner(opponent, player):
    if match.get(player) == opponent:
        return 'draw'
    elif beats.get(player) == opponent:
        return 'win'
    else:
        return 'loss'
    
# Part 1
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

# Part 2
def game2(file):
    total = 0
    with open(file, 'r') as f:
        for l in f:
            opponent_choice, outcome = l.strip().split()
            player_choice = calc_choice(opponent_choice, outcome)
            choice_score = choices[player_choice]
            result = calc_winner(opponent_choice, player_choice)
            result_score = outcomes[result]
            game = choice_score + result_score
            total += game
    return total

file = '../inputs/d2.txt'
game1_total_score = game(file)
game2_total_score = game2(file)
print(f"Game 1 Total Score: {game1_total_score}")
print(f"Game 2 Total Score: {game2_total_score}")
