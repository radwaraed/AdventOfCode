#Day5 Part 1

from collections import defaultdict

to_collect = ["seeds","seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

items_list = problem_set.strip().splitlines()

master_dict = defaultdict(list)

for item in items_list:
    if item != " ":
        headers = item.rstrip("\n").split(": ")
        for header in headers:
            if header in to_collect:
                key = header
            else:
                if header != "":
                    master_dict[key].append(header)

seeds = master_dict['seeds'][0].split(" ")
locations = set()

for seed in seeds:
    seed = int(seed)
    done = 0
    for element in master_dict["seed-to-soil map:"]:
        destination,source,length = map(lambda x:int(x),element.split(" "))
        if seed in range(source,source+length):
            diff = seed - source
            newdestination = destination + diff
            done = 1
    if done == 0:
        newdestination = seed
                    
    for item in ["soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]:
        done = 0
        for element in master_dict[item]:
            source,destination,length = element.split(" ")
            for element in master_dict[item]:
                element_list = element.split(" ")
                destination,source,length = map(lambda x:int(x),element.split(" "))
                if newdestination in range(source,source+length):
                    diff = newdestination - source
                    newdestination = destination + diff
                    done = 1
                    break
            break
            
        if done == 0:
            newdestination = newdestination  
            
    locations.add(newdestination)
        
print(min(locations))



#Day5 Part2
#go from the other direction?

from collections import defaultdict

to_collect = ["seeds","seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

items_list = problem_set.strip().splitlines()

master_dict = defaultdict(list)

for item in items_list:
    if item != " ":
        headers = item.rstrip("\n").split(": ")
        for header in headers:
            if header in to_collect:
                key = header
            else:
                if header != "":
                    master_dict[key].append(header)
starts = {}
seeds = master_dict['seeds'][0].split(" ")
for i in range(0,len(seeds),2):
    start = int(seeds[i])
    length = int(seeds[i+1])
    starts[start] = length

minimum_destination = -1 #listed as zero in the dataset as a destination
x = ""

while x != "found":
    #print("trying ")
    minimum_destination += 1
    #print(minimum_destination)
    done = 0
    for element in master_dict["humidity-to-location map:"]:
        destination,source,length = map(lambda x:int(x),element.split(" "))
        if minimum_destination in range(destination,destination+length):
            diff = minimum_destination - destination
            newdestination = source + diff
            done = 1
            break
    if done == 0:
        newdestination = minimum_destination

    for item in ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:"][::-1]:
        #print(item)
        done = 0
        for element in master_dict[item]:
            destination,source,length = map(lambda x:int(x),element.split(" "))
            for element in master_dict[item]:
                element_list = element.split(" ")
                destination,source,length = map(lambda x:int(x),element.split(" "))
                if newdestination in range(destination,destination+length):
                    diff = newdestination - destination
                    newdestination = source + diff   
                    #print("newdestination " + str(newdestination))
                    done = 1
                    break
            break
        if done == 0:
            newdestination = newdestination
            #print("newdestination " + str(newdestination))

    #check if soil destination corresponds to an existing seed number 
    for start,length in starts.items():
        if newdestination in range(start,start+length):        
            print("found seed number: " + str(newdestination))
            print("lowest location: " + str(minimum_destination))
            x = "found"
