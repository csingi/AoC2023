########################################################################################################################
# Advent of Code 2023 - Dec - Day 1 - Part 1
#
# Challenge 1 of 50
#
# --- Day 1: Trebuchet?! ---
#
########################################################################################################################

# Parameter to use test data ("N") or load data from file to read the real data for the solution ("Y")
use_real_data = "Y"

if use_real_data == "Y":
    file = open("E:\Python programming\AoC2023\Day1\data.txt", "r")
    data = file.read()
    list = data.split("\n")
    file.close()
    # print(list)
else:
    list = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    # print(list)

# Instantiate required variables
# Store digit * 10 in the list
first_digit_10 = []
# Store last digit in the list
last_digit = []
# Store result in this variable
resultsum = 0

# Iterate through each word in the input list
for word in list:
    # Iterate through each letter in order for each word
    for letter in word:
        # If the character is a digit append the value to the first_digit_10 list and mulpiply it by 10
        if letter.isdigit():
            letter = int(letter) * 10
            first_digit_10.append(letter)
            # print(result)
            break
    # Iterate through each letter in backwards order for each word
    for last_letter in reversed(word):
        # If the character is a digit append the value to the last_digit list
        if last_letter.isdigit():
            last_digit.append(int(last_letter))
            # print(result)
            break

# Iterate through both lists to add their values then add the results into resultsum variable
for i in range(0, len(first_digit_10)):
    num1 = first_digit_10[i]
    num2 = last_digit[i]
    # print(num1 + num2)
    summ = num1+num2
    resultsum += summ
    # print(resultsum)

# Print the final result
print(resultsum)

########################################################################################################################
# 
# Improvement ideas: Merge last for loop into the first loop
#
########################################################################################################################