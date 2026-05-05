# Implement inheritance:
    # Base class: Model
    # Derived classes: LinearRegression, DecisionTree
    # Add train() and predict() methods



class Model:
    def train(self, X, y):
        raise NotImplementedError("Subclasses must implement this method")

    def predict(self, X):
        raise NotImplementedError("Subclasses must implement this method")      

    
