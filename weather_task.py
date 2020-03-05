class Weather:
    
    def __init__(self):
        self.weather_data=[row.strip().split() for row in open('weather.dat').readlines()]
        self.day_temp_range=[0,100,0]
    
    
    def smallest_temp_spread(self):
        for row in self.weather_data[2:]:
            
            if row[1][-1]=='*':
                row[1]=row[1][:2]
            
            if row[2][-1]=='*':
                row[2]=row[2][:2]
            
            if (float(row[1])-float(row[2]))<(self.day_temp_range[1]-self.day_temp_range[2]):
                self.day_temp_range[0]=int(row[0])
                self.day_temp_range[1]=float(row[1])
                self.day_temp_range[2]=float(row[2])

        print("Day is {}, Max temp = {}, Min Temp = {}".format(self.day_temp_range[0], self.day_temp_range[1], self.day_temp_range[2]))            

        
day_temp_spread=Weather()
day_temp_spread.smallest_temp_spread()        