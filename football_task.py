from common_task import *

class Football:

    def __init__(self):
        self.football_data = data.data_extract("football.dat")
        self.team_goal_range=["",100,0]
        self.team = ""
        self.goal_diff = 0

    def goal_diff_return(self):
        self.team, self.goal_diff = difference.smallest_goal_diff(self.football_data,self.team_goal_range)
        print("Team is {}, Goals difference = {}".format(self.team, self.goal_diff))  

calc_min_goal_diff = Football()
calc_min_goal_diff.goal_diff_return()       