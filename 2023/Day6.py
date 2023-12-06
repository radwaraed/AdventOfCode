#Day6 Part1
items_list = problem_set.strip().splitlines()

times_list,distances_list = items_list
times = map(lambda x:int(x),times_list.split(":        ")[-1].split("     "))
distances = distances_list.split(":   ")[-1].split("   ")

successful_attempts_list = []

time_distance_dictionary = {}
for i,time in enumerate(times):
    successful_attempts = 0
    record_distance = int(distances[i])
    for test_run in range(0,time):
        speed = test_run
        time_remaining = time - test_run
        distance_travelled = speed*time_remaining
        if distance_travelled > record_distance:
            successful_attempts += 1
    successful_attempts_list.append(successful_attempts)
         
result = 1
for element in successful_attempts_list:
    result *= element
print(result)


#Day6 Part2
items_list = problem_set.strip().splitlines()

times_list,distances_list = items_list
times = int(times_list.split(":        ")[-1].strip().replace(" ",""))
distances = int(distances_list.split(":   ")[-1].strip().replace(" ",""))

successful_attempts_list = []

time_distance_dictionary = {}
    
successful_attempts = 0
record_distance = distances
for test_run in range(0,times):
    speed = test_run
    time_remaining = times - test_run
    distance_travelled = speed*time_remaining
    if distance_travelled > record_distance:
        successful_attempts += 1
successful_attempts_list.append(successful_attempts)

result = 1
for element in successful_attempts_list:
    result *= element
print(result)
