from data import data, data_ml


if __name__ == '__main__':

    mydata = data("data/")  # Create instance of class data
    x = mydata.load_data("X_data.csv")  # Load input data
    y = mydata.load_data("y_data.csv")
    print(x.head())
    print(y.head())

    mymldata = data_ml(x,y,0.2,0.2)

    x_train, x_validation, x_test, y_train, y_validation, y_test = mymldata.prepare_data_for_ml()

    print(x_validation.head())
    print(y_validation.head())

