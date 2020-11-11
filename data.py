import csv
import pandas as pd

class data:
    # Automatically read column names from csv file into list.
    def read_column_names(self, url):
        csvfile = url  # file path to csv file with numbers and names.
        f = open(csvfile, 'r')  # opens file for reading
        reader = csv.reader(f)
        reader = list(reader)  # Form document into list
        columns = reader[0]
        return columns

    def load_data(self, path, filename):
        url = path + filename
        columns = self.read_column_names(url)
        data = pd.read_csv(url, names=columns) #load into pandas dataframe
        return data


