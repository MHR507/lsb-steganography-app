from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

class StegoDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        from sklearn.metrics import accuracy_score, f1_score
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("F1-score:", f1_score(y_test, y_pred))

    def save(self, path='detector_model1.pkl'):
        joblib.dump(self.model, path)

    def load(self, path='detector_model1.pkl'):
        self.model = joblib.load(path)

    def predict(self, X):
        return self.model.predict(X)
