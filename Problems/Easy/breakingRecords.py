# HackerRank - Breaking Records

# Prompt

# Maria plays college basketball and wants to go pro. 
# Each season she maintains a record of her play. She tabulates the 
# number of times she breaks her season record for most points and 
# least points in a game. Points scored in the first game establish her 
# record for the season, and she begins counting from there.

class Solution:
    def breakingRecords(scores):
        # initiate min and max comparison variables
        minCount = maxCount = 0
        minScore = maxScore = scores[0]

        