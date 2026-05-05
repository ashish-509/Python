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



# Example usage:
X_train = [[1, 2], [3, 4], [5, 6]]
y_train = [0, 1, 0] 
X_test = [[2, 3], [4, 5]]

# Create model instances
lr_model = LinearRegression()
dt_model = DecisionTree()

# Train models
lr_model.train(X_train, y_train)
dt_model.train(X_train, y_train)

# Make predictions
lr_predictions = lr_model.predict(X_test)
dt_predictions = dt_model.predict(X_test)

print("Linear Regression Predictions:", lr_predictions)
print("Decision Tree Predictions:", dt_predictions)