import pickle

def load_model():
    with open('rf_heart.pkl','rb') as f:
        model = pickle.load(f)
        return model

    