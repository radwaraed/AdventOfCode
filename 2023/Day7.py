#Day7 Part1

from collections import defaultdict, Counter

items_list = problem_set.strip().splitlines()

hands = {item.split(" ")[0]:int(item.split(" ")[1]) for item in items_list}

strength_order = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2"
strength_order_list = strength_order.split(", ")[::-1]
strength_lookup = {item:idx for idx,item in enumerate(strength_order_list)}


def rank_hands_by_strength(list_of_hands):
    ordered_list = defaultdict(list)
    characters = {hand:[*hand] for hand in list_of_hands}
    characters_strength = defaultdict(list)
    for k,v in characters.items():
        for item in v:
            characters_strength[k].append(strength_lookup[item])
    sorted_characters = sorted(characters_strength, key=characters_strength.get,reverse=False)
    return(sorted_characters)


def rank_hands(list_of_hands):
    ranks = defaultdict(list)
    for hand in list_of_hands:
        unique_characters = set(hand)
        counts = set(Counter(hand).values())
        if len(unique_characters) == 1:
            ranks["7"].append(hand)
        elif len(unique_characters) == 2:
            if counts == {4, 1}: #four-of-a-kind
                ranks["6"].append(hand)
            elif counts == {3, 2}:
                ranks["5"].append(hand)               
        elif len(unique_characters) == 3:
            if counts == {3, 1, 1}: 
                ranks["4"].append(hand)
            elif counts == {2, 2, 1}: 
                ranks["3"].append(hand)               
        elif len(unique_characters) == 4:
            if counts == {2, 1, 1, 1}: 
                ranks["2"].append(hand)                 
        else:
            ranks["1"].append(hand) 
    return(ranks)
  
ranks = rank_hands(hands.keys())

ordered = {}
for rank in ["1","2","3","4","5","6","7"]:
    hands_to_evaluate = ranks[rank]
    ordered[rank] = rank_hands_by_strength(hands_to_evaluate)
  
final_count = 0
idx = 1
final_order = []
for rank in ["1","2","3","4","5","6","7"]:
    for item in ordered[rank]:
        final_order.append(item)
        final_count += (idx * hands[item])
        idx += 1
print(final_count) 

#Day7 Part2
from collections import defaultdict, Counter

items_list = problem_set.strip().splitlines()

hands = {item.split(" ")[0]:int(item.split(" ")[1]) for item in items_list}

strength_order = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J"
strength_order_list = strength_order.split(", ")[::-1]
strength_lookup = {item:idx for idx,item in enumerate(strength_order_list)}


def rank_hands_by_strength(list_of_hands):
    ordered_list = defaultdict(list)
    characters = {hand:[*hand] for hand in list_of_hands}
    characters_strength = defaultdict(list)
    for k,v in characters.items():
        for item in v:
            characters_strength[k].append(strength_lookup[item])
    sorted_characters = sorted(characters_strength, key=characters_strength.get,reverse=False)
    return(sorted_characters)

def rank_hands(list_of_hands):
    ranks = defaultdict(list)
    for hand in list_of_hands:
        unique_characters = set(hand)
        counts = set(Counter(hand).values())
        if "J" not in hand:
            if len(unique_characters) == 1:
                ranks["7"].append(hand)
            elif len(unique_characters) == 2:
                if counts == {4, 1}: #four-of-a-kind
                    ranks["6"].append(hand)
                elif counts == {3, 2}:
                    ranks["5"].append(hand)               
            elif len(unique_characters) == 3:
                if counts == {3, 1, 1}: 
                    ranks["4"].append(hand)
                elif counts == {2, 2, 1}: 
                    ranks["3"].append(hand)               
            elif len(unique_characters) == 4:
                if counts == {2, 1, 1, 1}: 
                    ranks["2"].append(hand)                 
            else:
                ranks["1"].append(hand) 
        elif "J" in hand:
            if len(unique_characters) == 1:
                ranks["7"].append(hand)  
                
            elif len(unique_characters) == 2:
                maximum = 0
                for key,value in Counter(hand).items():
                    if key != "J":
                        if value > maximum:
                            maximum = value
                for k,v in Counter(hand).items():
                    if v == maximum and k != "J":
                        hand_new = hand.replace("J",k)

                new_unique_characters = set(hand_new)
                new_counts = set(Counter(hand_new).values())
                if len(new_unique_characters) == 1:
                    ranks["7"].append(hand)
                    
            elif len(unique_characters) == 3:
                maximum = 0
                for key,value in Counter(hand).items():
                    if key != "J":
                        if value > maximum:
                            maximum = value
                for k,v in Counter(hand).items():
                    if v == maximum and k != "J":
                        hand_new = hand.replace("J",k)

                new_unique_characters = set(hand_new)
                new_counts = set(Counter(hand_new).values())

                if len(new_unique_characters) == 2:
                    if new_counts == {4, 1}: #four-of-a-kind
                        ranks["6"].append(hand)
                    elif new_counts == {3, 2}:
                        ranks["5"].append(hand)

            elif len(unique_characters) == 4:
                maximum = 0
                for key,value in Counter(hand).items():
                    if key != "J":
                        if value > maximum:
                            maximum = value
                for k,v in Counter(hand).items():
                    if v == maximum and k != "J":
                        hand_new = hand.replace("J",k)
                new_unique_characters = set(hand_new)
                new_counts = set(Counter(hand_new).values())

                if len(new_unique_characters) == 3:
                    
                    if new_counts == {3, 1, 1}: 
                        ranks["4"].append(hand)
                    elif new_counts == {3, 2}:
                        ranks["5"].append(hand) 
                    elif new_counts == {2, 2, 1}: 
                        ranks["3"].append(hand) 

            elif len(unique_characters) == 5:
                ranks["2"].append(hand) 
                
    return(ranks)
            
    
ranks = rank_hands(hands.keys())

ordered = {}
for rank in ["1","2","3","4","5","6","7"]:
    hands_to_evaluate = ranks[rank]
    ordered[rank] = rank_hands_by_strength(hands_to_evaluate)

final_count = 0
idx = 1
final_order = []
for rank in ["1","2","3","4","5","6","7"]:
    for item in ordered[rank]:
        final_order.append(item)
        final_count += (idx * hands[item])
        idx += 1
print(final_count)
