# wordle-groupme-stats
Provide group and individual statistics on Wordle games posted to a GroupMe group

## steps:
1. open web GroupMe where you track Wordle games
2. scroll up as far back in time as you want staistics for
3. click and drag selection all the way back down to most recent
4. copy and paste selection into file 'wordle-groupme-history.txt'
5. edit the list of GroupMe usernames in wordle-groupme-stats.py:
`playerNames = ['GroupMeUser1','GroupMeUser2','GroupMeUser3','GroupMeUser4','GroupMeUser5','GroupMeUser5_alt','GroupMeUser6']`
# 6. if any players have multiple GroupMe accounts whose stats should be merged, edit this list in wordle-groupme-stats.py:
`mergePlayers = [('GroupMeUser5_alt','GroupMeUser5')] # merge first player stats into second player`
7. python wordle-groupme-stats.py
8. copy and paste stats back into GroupMe

## todo:
1. automate all steps above
2. collect and output stats to GroupMe weekly at 12 am

## sample output:
```
---  WordleStatsBot version 12 April 2023 ---
221 games played since Feb 17 2022 (420 days)
209 (95%) games won with 4.37 average score

Average score:
1. GroupMeUser1 (4.24)
2. GroupMeUser5 (4.24)
3. GroupMeUser6 (4.38)
4. GroupMeUser3 (4.41)
5. GroupMeUser2 (4.62)
6. GroupMeUser4 (5.00)

Win percentage:
1. GroupMeUser4 (100.00%)
2. GroupMeUser5 (100.00%)
3. GroupMeUser3 (96.43%)
4. GroupMeUser1 (95.83%)
5. GroupMeUser2 (93.02%)
6. GroupMeUser6 (88.89%)

All-time win streak:
1. GroupMeUser5 (46)
2. GroupMeUser1 (24)
3. GroupMeUser2 (24)
4. GroupMeUser3 (23)
5. GroupMeUser6 (21)
6. GroupMeUser4 (2)

Current win streak:
1. GroupMeUser5 (46)
2. GroupMeUser1 (15)
3. GroupMeUser3 (4)
4. GroupMeUser2 (2)
5. GroupMeUser4 (2)
6. GroupMeUser6 (1)

Games won:
1. GroupMeUser6 (48)
2. GroupMeUser1 (46)
3. GroupMeUser5 (46)
4. GroupMeUser2 (40)
5. GroupMeUser3 (27)
6. GroupMeUser4 (2)

Games played:
1. GroupMeUser6 (54)
2. GroupMeUser1 (48)
3. GroupMeUser5 (46)
4. GroupMeUser2 (43)
5. GroupMeUser3 (28)
6. GroupMeUser4 (2)
```
