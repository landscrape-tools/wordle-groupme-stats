#
# wordle-groupme-stats.py
#
# Provide group and individual statistics on Wordle games posted to a GroupMe group
#
# steps:
# 1. open web GroupMe where you track Wordle games
# 2. scroll up as far back in time as you want staistics for
# 3. click and drag selection all the way back down to most recent
# 4. copy and paste selection into file 'wordle-groupme-history.txt'
# 5. edit the list of GroupMe usernames in wordle-groupme-stats.py:
playerNames = ['GroupMeUser1','GroupMeUser2','GroupMeUser3','GroupMeUser4','GroupMeUser5','GroupMeUser5_alt','GroupMeUser6']
# 6. if any players have multiple GroupMe accounts whose stats should be merged, edit this list in wordle-groupme-stats.py:
mergePlayers = [('GroupMeUser5_alt','GroupMeUser5')] # merge first player stats into second player
# 7. python wordle-groupme-stats.py
# 8. copy and paste stats back into GroupMe
#
# todo: 
# 1. auto crawl Groupme for steps 1-6
# 2. auto collect and submit stats daily at 12 am
#
from datetime import datetime
import operator

class Player:
    def __init__(self, name):
        self.name = name
        self.gameNumsPlayed = []
        self.gameScores = []
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.totalScore = 0
        self.currWinStreak = 0
        self.maxWinStreak = 0
        self.winPercentage = 0.0
        self.avgScore = 0.0

def collectStats(playerDict):
    currentPlayer = ''
    firstGameDate = ''
    currentGameDate = ''
    with open('wordle-groupme-history.txt') as txtFile:
        for line in txtFile:
            # get player name
            for playerName in playerDict.keys():
                if playerName in line:
                    currentPlayer = playerName
                    for mergePlayerFirst, mergePlayerSecond in mergePlayers:
                        if currentPlayer == mergePlayerFirst:
                            currentPlayer = mergePlayerSecond
                        break
                    break

            # get game date
            if ' AM' in line or ' PM' in line:
                gameDateTime = line.split(',')
                if len(gameDateTime) >= 2:
                    gameDate = gameDateTime[0]
                    if not firstGameDate:
                        firstGameDate = gameDate + ' 2022'
                    if gameDate != currentGameDate:
                        currentGameDate = gameDate

            # get game # and game score
            if 'Wordle' in line and '/6' in line:
                player = playerDict[currentPlayer]
                gameNum = int(line.strip().split('Wordle ')[1].split(' ')[0])

                if gameNum not in player.gameNumsPlayed:
                    #print ('%s played game %d' % (currentPlayer, gameNum))
                    player.gameNumsPlayed.append(gameNum)
                    player.gamesPlayed += 1
                    scoreText = line.strip().split('/6')[0][-1]
                    if scoreText.isdigit():
                        player.gamesWon += 1
                        player.totalScore += int(scoreText)
                        player.currWinStreak += 1
                        if player.currWinStreak > player.maxWinStreak:
                            player.maxWinStreak = player.currWinStreak
                        player.gameScores.append(scoreText)
                    else:
                        player.currWinStreak = 0
                        player.gameScores.append('X')
                    playerDict[currentPlayer] = player # todo: necessary?

    for mergePlayerFirst, mergePlayerSecond in mergePlayers:
        del playerDict[mergePlayerFirst]

    return firstGameDate

def calcStats(allPlayers, playerDict):
    for playerName in playerDict.keys():
        player = playerDict[playerName]
        if player.gamesPlayed > 0:
            player.winPercentage = float(player.gamesWon)/float(player.gamesPlayed)*100.0
        else:
            player.winPercentage = 0.0

        if player.gamesWon > 0:
            player.avgScore = float(player.totalScore)/float(player.gamesWon)
        else:
            player.avgScore = 7.0

        playerDict[playerName] = player # todo: necessary?

        allPlayers.gamesPlayed += player.gamesPlayed
        allPlayers.gamesWon += player.gamesWon
        allPlayers.totalScore += player.totalScore

    allPlayers.winPercentage = float(allPlayers.gamesWon)/float(allPlayers.gamesPlayed)*100.0
    allPlayers.avgScore = float(allPlayers.totalScore)/float(allPlayers.gamesWon)

def leaderboard(playerDict, description, formatStr, attributeStr, descendingOrder=True):
    indentSpaces = ''
    print (indentSpaces+description)
    rank = 1
    for player in (sorted(playerDict.values(), key=operator.attrgetter(attributeStr), reverse=descendingOrder)):
        #print(getattr(player, attributeStr), type(getattr(player, attributeStr)))
        print(str(indentSpaces+'%d. '+formatStr) % (rank, player.name, getattr(player, attributeStr)))
        rank += 1
    print

def outputStats(allPlayers, playerDict, firstGameDate):
    print ('\n---  WordleStatsBot version 12 April 2023 ---') 
    firstGameDateTime = datetime.strptime(firstGameDate, '%b %d %Y')

    print ('%d games played since %s (%d days)\n%d (%.0f%%) games won with %.2f average score' % \
        (allPlayers.gamesPlayed, firstGameDate, (datetime.today() - firstGameDateTime).days, allPlayers.gamesWon, allPlayers.winPercentage, allPlayers.avgScore))

    print
    leaderboard(playerDict, '\nAverage score:',        '%s (%.2f)',   'avgScore', descendingOrder=False)
    leaderboard(playerDict, '\nWin percentage:',       '%s (%.2f%%)', 'winPercentage')
    leaderboard(playerDict, '\nAll-time win streak:',  '%s (%d)',     'maxWinStreak')
    leaderboard(playerDict, '\nCurrent win streak:',   '%s (%d)',     'currWinStreak')
    leaderboard(playerDict, '\nGames won:',            '%s (%d)',     'gamesWon')
    leaderboard(playerDict, '\nGames played:',         '%s (%d)',     'gamesPlayed')

    # dump it all
    # for key in playerDict.keys():
    #     print key,
    #     attrs = vars(playerDict[key])
    #     print(', '.join("%s: %s" % item for item in attrs.items()))


########################################################################################################################

playerDict = {}
for playerName in playerNames:
    playerDict[playerName]=Player(playerName)
allPlayers = Player('All Players')

firstGameDate = collectStats(playerDict)
calcStats(allPlayers, playerDict)
outputStats(allPlayers, playerDict, firstGameDate)
