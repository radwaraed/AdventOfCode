#Day3 Problem1

items_list = problem_set.strip().splitlines()
#print(items_list)

symbols, digits = defaultdict(list), defaultdict(lambda:defaultdict(list))

for idx,item in enumerate(items_list):
    for match in re.finditer(r'[^\.]*', item): #look for anything that is not a dot
        if match.group() != "":
            if match.group().isdigit():
                digits[idx][match.group()].append(match.span())
            else:
                try:
                    to_add_by = match.span()[0]  

                    for match2 in re.finditer(r'\d+',match.group()): #look for anything
                        match2_span = list(x+to_add_by for x in match2.span())
                        digits[idx][match2.group()].append(match2_span)
                    for match3 in re.finditer(r'\D',match.group()): #look for anything that is not a digit
                        match3_span = list(x+to_add_by for x in match3.span())
                        if match3.group() == "*":
                            symbols[idx].append(match3_span[0])

                except AttributeError:
                    if match.group() == "*":
                        symbols[idx].append(match.span()[0])
                    
total_sum_engines = 0

for line,v in digits.items():
    for item,found_span in v.items():
        for find_span in found_span:
            #print(item)
            #print(find_span)
            before,after = find_span[0]-1,find_span[1]
            if before in symbols[line] or after in symbols[line]:
                #print('found1')
                total_sum_engines += int(item)
            else:
                for i in range(before,after+1):
                    if i in symbols[line-1]: #check above line
                        #print('found2')
                        total_sum_engines += int(item)
                    if i in symbols[line+1]: #check below line
                        #print('found3')
                        total_sum_engines += int(item)
                        
print(total_sum_engines)


#Day3 Problem2

items_list = problem_set.strip().splitlines()
#print(items_list)

symbols, digits = defaultdict(list), defaultdict(lambda:defaultdict(list))

for idx,item in enumerate(items_list):
    for match in re.finditer(r'[^\.]*', item): #look for anything that is not a dot
        if match.group() != "":
            if match.group().isdigit():
                digits[idx][match.group()].append(match.span())
            else:
                try:
                    to_add_by = match.span()[0]  

                    for match2 in re.finditer(r'\d+',match.group()): #look for anything
                        match2_span = list(x+to_add_by for x in match2.span())
                        digits[idx][match2.group()].append(match2_span)
                    for match3 in re.finditer(r'\D',match.group()): #look for anything that is not a digit
                        match3_span = list(x+to_add_by for x in match3.span())
                        symbols[idx].append(match3_span[0])

                except AttributeError:
                    symbols[idx].append(match.span()[0])
     
    
asterisk_hit = defaultdict(lambda:defaultdict(list))

for line,v in digits.items():
    for item,found_span in v.items():
        for find_span in found_span:
            #print(item)
            #print(find_span)
            before,after = find_span[0]-1,find_span[1]
            if before in symbols[line]:
                asterisk_hit[line][before].append(int(item))
            elif after in symbols[line]:
                asterisk_hit[line][after].append(int(item))
            else:
                for i in range(before,after+1):
                    if i in symbols[line-1]: #check above line
                        asterisk_hit[line-1][i].append(int(item))
                    if i in symbols[line+1]: #check below line
                        asterisk_hit[line+1][i].append(int(item))

total_sum = 0
for line,v in asterisk_hit.items():
    for location,numbers in v.items():
        if len(numbers) == 2:
            product = numbers[0] * numbers[1]
            total_sum += product
            
print(total_sum)
