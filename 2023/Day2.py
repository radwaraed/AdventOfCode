#Day2 Problem1

input_in_bag = {"red": 12, "green": 13, "blue":14}

items_list = problem_set.strip().splitlines()

total_games = len(items_list)
impossible_games = set()
possible_games_sum = 0

for item in items_list:
    game, draws = item.split(": ")
    game_number = int(game.split(" ")[1])
    draws_list = draws.split("; ")
    for draw in draws_list:
        individual_draws_list = draw.split(", ")
        for individual_draw in individual_draws_list:
            ball_count,ball_color = individual_draw.split(" ")
            ball_count = int(ball_count)
            if ball_count > input_in_bag[ball_color]:
                impossible_games.add(game_number)
                break
                
for i in range(1,total_games+1):
    if i not in impossible_games:
        possible_games_sum += i
    
print(possible_games_sum)



#Day2 Problem2

from collections import defaultdict

items_list = problem_set.strip().splitlines()
            
#create a dictionary where min_input_in_bag is zero per color               
min_input_in_bag = defaultdict(lambda:defaultdict(lambda:0))

#overwrite the dictionary with the minimum count per game
for item in items_list:
    game, draws = item.split(": ")
    game_number = int(game.split(" ")[1])
    draws_list = draws.split("; ")
    for draw in draws_list:
        individual_draws_list = draw.split(", ")
        for individual_draw in individual_draws_list:
            ball_count,ball_color = individual_draw.split(" ")
            ball_count = int(ball_count)
            if ball_count > min_input_in_bag[game_number][ball_color]:
                min_input_in_bag[game_number][ball_color] = ball_count

games_total = 0

for game,stats in min_input_in_bag.items():
    game_value = 1      
    for color,count in stats.items():
        game_value *= count
    games_total += game_value  
    
print(games_total)
