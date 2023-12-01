#Day1 Problem1

import re

def find_first_last_digits(s):
    # Find the first integer
    match_first = re.search(r'\d', s)
    first_integer = match_first.group()
    first_digit = int(first_integer[0])

    # Find the last integer
    match_last = re.search(r'\d', s[::-1])
    last_integer = match_last.group()[::-1]
    last_digit = int(last_integer[-1])

    return first_digit, last_digit


#Day1 Problem2

import re
my_values = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
"enin":9,"thgie":8,"neves":7,"xis":6,"evif":5,"ruof":4,"eerht":3,"owt":2,"eno":1}            

def find_digit_or_name(s):
    # Find the first integer    
    try:
        match_first = re.search(r'\d', s)
        first_pos = match_first.start()
        first_integer = int(match_first.group()) 
    except AttributeError:
        first_pos = len(s)

    #Find the last integer
    try:
        match_last = re.search(r'\d', s[::-1])
        last_pos = match_last.start()
        last_integer = int(match_last.group()[::-1])  
    except AttributeError:
        last_pos = len(s)
  
    #Find first integer spelled out
    try:
        match_first_string = re.search(r'(one|two|three|four|five|six|seven|eight|nine)', s, re.IGNORECASE)
        first_pos_string = match_first_string.start()
        first_integer_string = my_values[match_first_string.group()]
    except AttributeError:
        first_pos_string = len(s)
      
    #Find last integer spelled out
    try:
        match_last_string = re.search(r'(enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)', s[::-1], re.IGNORECASE)
        last_pos_string = match_last_string.start()
        last_integer_string = my_values[match_last_string.group()]
    except AttributeError:
        last_pos_string = len(s)

    
    if first_pos < first_pos_string:
        first_digit = first_integer
    elif first_pos > first_pos_string:
        first_digit = first_integer_string

    if last_pos < last_pos_string:
        last_digit = last_integer
    elif last_pos > last_pos_string:
        last_digit = last_integer_string
    
    return first_digit, last_digit
