from common import *

class FootballAnalyzer(DataExtracter, DataAnalyzer):
    """For football operations"""

    def __init__(self):
        """Initializing variables used in class"""

        self.football_data = self.data_extract("football.dat")
        self.useable_data = list()
        self.team_and_goal_diff = tuple()

    
    def smallest_goal_difference(self):
        """For printing team and the minimum goal difference"""

        for data_row in self.football_data[1:]:
            if len(data_row) != 1:
                self.useable_data.append((data_row[1], float(data_row[6]), float(data_row[8])))

        self.team_and_goal_diff = self.min_diff_return(self.useable_data)
        print("Team is {}, Goals difference = {}".format(self.team_and_goal_diff[0], abs(self.team_and_goal_diff[1]-self.team_and_goal_diff[2]))) 

min_goal_diff = FootballAnalyzer()
min_goal_diff.smallest_goal_difference()
