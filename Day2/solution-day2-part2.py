########################################################################################################################
# Advent of Code 2023 - Dec - Day 2 - Part 2
#
# Challenge 4 of 50
#
# --- Day 2: Cube Conundrum ---
#
########################################################################################################################

# Parameter to use test data ("N") or load data from file to read the real data for the solution ("Y")
use_real_data = "Y"

if use_real_data == "Y":
    file = open("E:\Python programming\AoC2023\Day2\data.txt", "r")
    data = file.read()
    games = data.split("\n")
    file.close()
    # print(games)
else:
    games = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
             "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
             "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
             "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
             "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
    # print(games)

cube_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}

multiple_of_cubes = 0

for game in games:
    # Split games and sets
    game_and_set = game.split(": ")
    # Determine game number
    game_number = game_and_set[0].lstrip("Game ")
    # print(game_number)
    #split games into different sets
    sets = game_and_set[1].split("; ")
    # print(sets)
    
    # set all values to a high value
    red = 0
    green = 0
    blue = 0
    # Determine the highest number of cubes in each set
    for set in sets:
        # print(game_number)
        one_set = set.split(", ")
        # print(one_set)

        for item in one_set:
            if "red" in item and red < int(item.split(" ")[0]) and int(item.split(" ")[0]) != 0 :
                red = int(item.split(" ")[0])
            if "green" in item and green < int(item.split(" ")[0]) and int(item.split(" ")[0]) != 0:
                green = int(item.split(" ")[0])
            if "blue" in item and blue < int(item.split(" ")[0]) and int(item.split(" ")[0]) != 0:
                blue = int(item.split(" ")[0])
    print("Game number: " + game_number)
    print(red)
    print(green)
    print(blue)
    multiple_of_cubes += red*green*blue
    print(multiple_of_cubes)
    #This was part of part 1 solution
    #                   12     20                     13        0                          14   2
    # if cube_dict.get("red") >= red and cube_dict.get("green") >= green and cube_dict.get("blue") >= blue :
    #     print(game_number)
    #     sum_of_ids += int(game_number) 
    #     print("Sum:")
    #     print(sum_of_ids)


