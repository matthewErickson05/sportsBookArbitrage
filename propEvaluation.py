import pandas as pd
import numpy as np

##Goal of this file is to have all the data and evaluate the props against the sportsbook


##First method will take in a line from prizepicks and an over under price from the sportsbook.
##Problem: it will value a two yard difference in passing yards the same as a 2 point kicking difference
def EvaluateLine(ppline, sbline, overPrice, underPrice) :
    ##Gameplan: Find if the over or under on the sportsBook if favored
    ##          if one is favored find if the line for ppline is different
    lineDiff = ppline - sbline
    if (abs(lineDiff) < 1) :
        lineDiff = 0
    if (overPrice < underPrice) :
        ##Over is favorited, 
        if (lineDiff > 0) :
            #The bet is looking good
            powerRanking = lineDiff * abs(overPrice)
        elif (lineDiff < 0) :
            #The bet is looking bad
            powerRanking = 0
        elif (lineDiff == 0) :
            #The bet is favored as much as the sportsbook says
            powerRanking = abs(overPrice)
    elif (overPrice > underPrice) :
        #Under if favored
        if (lineDiff < 0) :
            powerRanking = lineDiff * abs(underPrice)
        elif (lineDiff > 0) :
            #Bet is looking bad
            powerRanking = 0
        elif (lineDiff == 0) :
            powerRanking = underPrice
    else :
        ##line is even, see if there is a discrepency in pp vs. book
        if (lineDiff > 0) :
            powerRanking = lineDiff * 100
        elif (lineDiff < 0) :
            powerRanking = lineDiff * 100
        else :
            powerRanking = 0
    return powerRanking

print(EvaluateLine(225.5, 227.5, -110, -100))