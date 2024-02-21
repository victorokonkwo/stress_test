import joblib

def predict(data):
    clf = joblib.load("xgb_model.sav")
    return clf.predict(data)
