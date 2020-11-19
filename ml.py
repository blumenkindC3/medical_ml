#Imports:
from sklearn.linear_model import LinearRegression #Linear model
from sklearn.linear_model import LogisticRegression #Logistic regression
from sklearn.neighbors import KNeighborsClassifier #Classifier for K-nearest-neighbor
from sklearn.svm import SVC #Support vector machine

class model:
    def __init__ (self, modeltype = "knn"):

        if modeltype == "linear":
            self.model = LinearRegression()
        elif modeltype == "lg":  # for logistic regression
            self.model = LogisticRegression()
        elif modeltype == "knn":  # for k-neirest neighbor
            self.model = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
            # Default metric is minkowski, and with p=2 is equivalent to the standard Euclidean metric.
        elif modeltype == "svm":
            self.model = SVC(kernel='linear', C=1.0, random_state=1)
        else:
            print("This model was not implemented yet. Please choose another one.")

    def train_model(self):
        self.model.fit(x_train, y_train)







if __name__ == "__main__":
    print("Hello")