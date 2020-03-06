from common_task import *

class Weather:

    def __init__(self):
        self.weather_data = data.data_extract("weather.dat")
        self.day_temp_range = [0,100,0]
        self.day = 0
        self.max_temp = 0
        self.min_temp = 0

    def smallest_temperatue_spread(self):
        self.day, self.max_temp, self.min_temp = difference.smallest_temp_spread(self.weather_data, self.day_temp_range)
        print("Day is {}, Max temp = {}, Min Temp = {}".format(self.day, self.max_temp, self.min_temp))

calc_weather_temp_spread = Weather()
calc_weather_temp_spread.smallest_temperatue_spread()




