import joblib

def predict(data, model):
    clf = joblib.load("xgb_model.sav")
    clf = joblib.load(model)
    return clf.predict(data)
