import pymongo
from pprint import pprint
from espnff import League
from collections import defaultdict

try:
    import simplejson as json
except:
    import json

# GLOBALS
# db stuff
db = pymongo.MongoClient().foosball
print("Connecting to DB: ",'\'',db.name,'\'')

# league info for api query
league_id = 262704
year = 2017
my_team_id = 8
this_week = 3

# END GLOBALS

# FUNCTIONS
def getmatch(week_matchups, team_id):
  for matchup in week_matchups:
    if matchup.home_team.team_id == team_id:
      match = matchup
      return match.data
    elif matchup.away_team.team_id == team_id:
      match = matchup
      return match.data
    else:
      match = "No Match Found"
  return match.data

# def getteams(teams_arr):
  # for team in teams_arr:
    # pprint(type(team))

# END FUNCTIONS

# SERIALIZABLE CLASSES
class TeamObj:
  def __init__(self, name, scores, wins, losses):
    self.name = name
    self.all_scores = scores
    self.wins = wins
    self.losses = losses

  def gettotal(self, scores):
    self.totalScore = 0
    for score in scores:
      self.totalScore += score
    return self.totalScore

# END SERIALIZABLE CLASSES

# get my team's overall data and write to disk
league = League(league_id, year)
teams = league.teams
my_team = next(team for team in teams if team.team_id == my_team_id)
team_obj = TeamObj(my_team.team_name, my_team.scores, my_team.wins, my_team.losses)
team_obj.gettotal(team_obj.all_scores)
with open('team.json', 'w') as f:
  json.dump(team_obj.__dict__, f)


# get my week's data and write to disk
week = league.scoreboard(week=this_week)
week_match = getmatch(week, my_team_id)
# print(type(week_match))
# for vars in week_match:
  # print(type(vars))
# for key, value in week_match.items():
  # print (key, type(value), value)
with open('week.json', 'w') as f:
  json.dump(week_match, f)
# print(week_match.items())
# pprint(week_match)
# print(vars(week_match))
# match_team = getteams(week_match)
# pprint(my_match)

