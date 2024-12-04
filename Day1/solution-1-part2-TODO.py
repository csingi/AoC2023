########################################################################################################################
# Advent of Code 2023 - Dec - Day 1 - Part 2
#
# Challenge 2 of 25
#
# --- Day 1: Trebuchet?! ---
#
########################################################################################################################

# Parameter to use test data ("N") or load data from file to read the real data for the solution ("Y")
use_real_data = "Y"

# Returns list
if use_real_data == "Y":
    file = open("E:\Python programming\AoC2023\Day1\data.txt", "r")
    data = file.read()
    list = data.split("\n")
    file.close()
    # print(list)
else:
    list = ["two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"]
    # print(list)

valuedict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in list:
    
    for key, value in valuedict.items():
        check = line.find(value)
        print(check)
        # if check >= 0 :
        #     break

# example = "two1ninenine"
# for value in valuedict:
#     if value in example : 
#         print(valuedict[value])
#         print(value)