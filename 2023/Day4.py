#Day4 Part1

total_score = 0
items_list = problem_set.strip().splitlines()
for item in items_list:
    score = 0
    card_number = item.split(": ")[0]
    winning_numbers = item.split(": ")[1].split(" | ")[0].split(" ")
    drawn_numbers = filter(lambda x:x!= "",item.split(": ")[1].split(" | ")[1].split(" "))
    for number in drawn_numbers:
        if number in winning_numbers:
            if score == 0:
                score += 1
            else:
                score *= 2
                
    total_score += score

print(total_score)


#Day4 Part2
from collections import defaultdict

tally_of_cards = defaultdict(int)

items_list = problem_set.strip().splitlines()
for item in items_list:
    original_card_number = int(item.split(": ")[0].split(" ")[-1])
    tally_of_cards[original_card_number] += 1

for item in items_list:
    original_card_number = int(item.split(": ")[0].split(" ")[-1])
    winning_numbers = item.split(": ")[1].split(" | ")[0].split(" ")
    drawn_numbers = item.split(": ")[1].split(" | ")[1].split(" ")
    cleaned_drawn_numbers = []
    for number in drawn_numbers:
        if number != "":
            cleaned_drawn_numbers.append(number)
    for i in range(0,tally_of_cards[original_card_number]):
        card_number = original_card_number
        for number in cleaned_drawn_numbers:
            if number in winning_numbers:
                card_number += 1
                tally_of_cards[card_number] += 1
                

total_cards = 0
for k,v in tally_of_cards.items():
    total_cards += v
    
print(total_cards)
