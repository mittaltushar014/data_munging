
class DataExtracter:

    def data_extract(self,file):
        file_data = [row.strip().split() for row in open('{}'.format(file)).readlines()]
        return file_data

class DataAnalyzer:

    def smallest_temp_spread(self, extracted_data_file, day_temp_range):
        for row in extracted_data_file[2:]:
             
            if row[1][-1] == '*':
                row[1] = row[1][:-1]
             
            if row[2][-1] == '*':
                row[2] = row[2][:-1]
             
            if (float(row[1])-float(row[2]))<(day_temp_range[1]-day_temp_range[2]):
                day_temp_range[0] = int(row[0])
                day_temp_range[1] = float(row[1])
                day_temp_range[2] = float(row[2])
 
        return(day_temp_range[0], day_temp_range[1], day_temp_range[2])


    def smallest_goal_diff(self, extracted_data_file, team_goal_range):
        for data_row in extracted_data_file[2:]:
            if len(data_row)!=1:
                if abs((int(data_row[6])-int(data_row[8])))<abs((team_goal_range[1]-team_goal_range[2])):
                    team_goal_range[0]=data_row[1]
                    team_goal_range[1]=int(data_row[6])
                    team_goal_range[2]=int(data_row[8])

        return(team_goal_range[0], abs(team_goal_range[1] - team_goal_range[2]))
            
    


data = DataExtracter()
difference = DataAnalyzer()
 









#def diff_return(self, extracted_data_file, range, arg1, arg2):
#        return_row=list()
#        for data_row in extracted_data_file[1:]:
#            if len(data_row)!=1:
#                if abs(int(data_row[arg1])-int(data_row[arg2]))<abs(range[arg1]-range[arg2]):
#                    return_row=data_row[:]
#
#        return return_row