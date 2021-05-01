# Tournament Winner

# Prompt 

# Solution

# function should take two parameters, competition and results
def tournamentWinner(competition, results):
    # create initial variable set as empty string
    currentBest = ""

    # create variable to represent scores, set to 0
    scores = {currentBest: 0}

    # initiate a for loop
    for i, competiton in enumerate(competitions):
        # create a result variable set to the i'th element in (results) input
        result = results[i]
        homeTeam, awayTeam = competition

        # create a variable to represent the winning team
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        # aspirational code, helper method to take care of updating scores
            # 3 parameters:
                # Team
                # points
                # scores
        updateScores(winningTeam, 3, scores)

        # if the scores for the winningTeam is greater than the currentBest
        # then set the currentBest to the winningTeam

        if scores[winningTeam] > scores[currentBest]:
            currentBest = winningTeam
    
    # return the currentBest
    return currentBest

# create helper function below
def updateScores(team, points, scores):
    # if (team) isn't in (scores), then create a key:value pair
    # of (team) in (scores) set to 0
    if team not in scores:
        scores[team] = 0
    
    # if there are (teams) in scores, then increment by (points)
    scores[team] += points

