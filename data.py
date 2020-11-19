import csv
import pandas as pd
from sklearn.model_selection import train_test_split #Train test split

class data:

    def __init__(self, path):
        self.path = path

    # Automatically read column names from csv file into list.
    def read_column_names(self,url):
        csvfile = url  # file path to csv file with numbers and names.
        f = open(csvfile, 'r')  # opens file for reading
        reader = csv.reader(f)
        reader = list(reader)  # Form document into list
        columns = reader[0]
        return columns

    def load_data(self, filename):
        url = self.path + filename
        columns = self.read_column_names(url)
        data = pd.read_csv(url, names=columns) #load into pandas dataframe
        return data




class data_ml(data):

    def __init__(self, x, y, test_split=0, validation_split=0):
        self.x=x
        self.y=y
        self.test_split = test_split
        self.validation_split = validation_split

    def prepare_data_for_ml(self):
        x_train, x_validation, x_test, y_train, y_validation, y_test = self.split_data()

        return x_train, x_validation, x_test, y_train, y_validation, y_test

    def split_data(self):

        # Split the dataset in a training and test set:
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, train_size=1-self.test_split)

        #Split the remaining data in a training and validation set:
        train_size = 1 - (self.test_split * 100)* (self.validation_split* 100)/1000
        #Multiply floats by 100 to transform float to int and avoid floating point error at multiplication.

        
        x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, train_size=train_size)

        return x_train, x_validation, x_test, y_train, y_validation, y_test


if __name__ == "__main__":
    mydata = data("data/")  #Create instance of class data
    x = mydata.load_data("X_data.csv") #Load input data
    y = mydata.load_data("y_data.csv")
    print(x.head())
    print(y.head())
