################################
# Pema lhendup
# 1 ICE
# 02230221
################################
# REFERENCES
# https://www.w3schools.com/python/
#https://www.youtube.com/watch?v=MMzXz7EDTZM&list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT&index=25
#https://www.youtube.com/watch?v=19PXDJCU3oc&t=406s
#https://www.codingal.com/coding-for-kids/blog/rock-paper-scissors-game-in-python/
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:50055
################################
#Define the function that needed to be read
def read_input(file_name):#read_input function is defined and it accepts a single parameter file_name indicating name of the file to be read.
    z = [] # z store data read from the file in the form of list as it allow duplicate data values and are changeable.
    with open(file_name, 'r') as file:# (r) represent reading a file
        line = file.readline()#file.readline() read the first line of the open opened file and stored it's content in the variable line.
        while line:#Iterate over each line in the file until empty line is encountered.
            opponent_choice, outcome = line.split()#After removing any preceding or following whitespace, it divide the line into opponent_choice and outcome depending on empty space.
            z.append((opponent_choice, outcome))#Add a tuple to the list z with opponent_choice and outcome.
            line = file.readline()# it read the next line of the opened file and stored it's content in the variable line
#Return the list z with the data read from the file.
    return z
#To calculate the score for each round, define calculate_score function
def calculate_score(rounds):
    total_score = 0#This line initializes the variable total_score to zero.
    for opponent_choice, outcome in rounds:
        if outcome == 'X':# if the outcome of the current round is 'X', we must accept the defeat
            #If opponent chooses A (Rock) we need to choose C (scissor) to fulfil the condition X(lost)
            if opponent_choice == 'A':
                total_score =total_score + 3 + 0 
            elif opponent_choice == 'B': #If opponent chooses B (Paper) we need to choose A (Rock) to fulfil the condition X(lost)
                total_score = total_score + 1 + 0
            else:#If opponent chooses C(scissor) we need to choose B(Paper) to fulfil the condition X(lost)
                total_score += 2 + 0
        if outcome == 'Y':# if the outcome of the current round is 'y', we need to draw the game
            #Choose the option same as the opponent to draw the game
            if opponent_choice == 'A': 
                total_score += 1 + 3
            elif opponent_choice == 'B':
                total_score += 2 + 3
            else:
                total_score += 3 + 3
        if outcome == 'Z': #if the outcome of the current round is 'Z', we will win the game
            if opponent_choice == 'A':#If opponent chooses A(Paper) we need to choose B(Paper) to fulfil the condition Z(Win)
                total_score += 2 + 6
            elif opponent_choice == 'B':#If opponent chooses B(Paper) we need to choose C(Scissor) to fulfil the condition Z(Win)
                total_score += 3 + 6
            else:#If opponent chooses C(Scissor) we need to choose A(Rock) to fulfil the condition Z(Win)
                total_score += 1 + 6
    print("The total score is:", total_score)

## Calculate the total score based on the rounds read from the valid input file "input_1_cap1.txt"
calculate_score(read_input("input_1_cap1.txt"))



