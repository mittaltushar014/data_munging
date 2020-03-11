from common import *

class WeatherAnalyzer(DataExtracter, DataAnalyzer):
    """For weather operations"""

    def __init__(self):
        """Initializing variables used in class"""

        self.weather_data = self.data_extract("weather.dat")
        self.useable_data = list()
        self.day_and_temp = tuple()


    def smallest_temperatue_spread(self):
        """For printing day and the smallest temperature spread"""

        for data_row in self.weather_data[2:]:

            if data_row[1][-1] == '*':
                data_row[1] = data_row[1][:-1]

            if data_row[2][-1] == '*':
                data_row[2] = data_row[2][:-1]

            self.useable_data.append((data_row[0], float(data_row[1]), float(data_row[2])))

        self.day_and_temp = self.min_diff_return(self.useable_data)
        print("Day is {}, Max temp = {}, Min Temp = {}".format(self.day_and_temp[0], self.day_and_temp[1], self.day_and_temp[2]))

weather_temp_spread = WeatherAnalyzer()
weather_temp_spread.smallest_temperatue_spread()
