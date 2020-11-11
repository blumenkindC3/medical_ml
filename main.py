from data import data

if __name__ == '__main__':


    mydata = data()  #Create instance of class data

    url = "data/X_data.csv" #filepath of input data

    x = mydata.load_data("data/", "X_data.csv") #Load input data

    print(x.head())

