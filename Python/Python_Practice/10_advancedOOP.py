# Implement inheritance:
    # Base class: Model
    # Derived classes: LinearRegression, DecisionTree
    # Add train() and predict() methods



class Model:
    def train(self, X, y):
        raise NotImplementedError("Subclasses must implement this method")

    def predict(self, X):
        raise NotImplementedError("Subclasses must implement this method")      

    
class LinearRegression(Model):
    def train(self, X, y):
        print("Training Linear Regression model with data:", X, y)

    def predict(self, X):
        print("Predicting with Linear Regression model for data:", X)
        return [0] * len(X)  # Dummy prediction


class DecisionTree(Model):
    def train(self, X, y):
        print("Training Decision Tree model with data:", X, y)

    def predict(self, X):
        print("Predicting with Decision Tree model for data:", X)
        return [1] * len(X)  # Dummy prediction



