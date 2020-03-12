class DataExtracter:
    """For extracting data"""

    def data_extract(self, file):
        """For extracting and returning data"""

        file_data = [row.strip().split() for row in open('data/{}'.format(file)).readlines()]
        return file_data

class DataAnalyzer:
    """For analyzing data"""

    def __init__(self):
        """Initializing variables used in class"""

        data_extract=DataExtracter()
        self.data = tuple()

    def min_diff_return(self, data_useable):
        """For finding minimum difference
        rtype: tuple
        """

        min_diff = abs(data_useable[0][1] - data_useable[0][2])

        for data_row in data_useable:
            if abs(float(data_row[2]) - float(data_row[1])) < min_diff:
                min_diff = abs(float(data_row[2]) - float(data_row[1]))
                self.data = data_row

        return self.data
