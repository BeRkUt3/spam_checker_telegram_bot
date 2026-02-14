from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import roc_auc_score, f1_score
from sklearn.model_selection import GridSearchCV, train_test_split
import numpy as np
import pandas as pd
import joblib

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

RANDOM_STATE = 42
TEST_SIZE = 0.2

def train():
    data = pd.read_csv('data/emails.csv')
    data = data.drop_duplicates(subset='text').reset_index(drop=True)

    vectorizer = CountVectorizer(lowercase=True, stop_words='english')

    X = data['text']
    y = data['spam']

    X = vectorizer.fit_transform(X)
    log_reg = LogisticRegression(C=np.float64(0.615848211066026))
    log_reg.fit(X, y)

    """
    test_data = pd.read_csv('data/test.csv')
    Xtest = test_data['text']
    ytest = test_data['label_num']
    Xtest = vectorizer.transform(Xtest)
    print(roc_auc_score(ytest, log_reg.predict_proba(Xtest)[:,1]))
    print(f1_score(ytest, log_reg.predict(Xtest)))
    """

    joblib.dump((log_reg, vectorizer), 'model.pkl')
if __name__ == "__main__":
    train()