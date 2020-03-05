#import commontask

class Football:
    
    def __init__(self):
        self.football_data=[line.strip().split() for line in open('football.dat').readlines()]
        self.team_goal_range=["",100,0]
    
    
    def smallest_goal_diff(self):
        for data_row in self.football_data[1:]:
            if len(data_row)!=1:
                if abs((int(data_row[6])-int(data_row[8])))<abs((self.team_goal_range[1]-self.team_goal_range[2])):
                    self.team_goal_range[0]=data_row[1]
                    self.team_goal_range[1]=int(data_row[6])
                    self.team_goal_range[2]=int(data_row[8])

        print("Team is {}, Goals difference = {}".format(self.team_goal_range[0], abs(self.team_goal_range[1] - self.team_goal_range[2])))         

        
team_goal_diff=Football()
team_goal_diff.smallest_goal_diff()