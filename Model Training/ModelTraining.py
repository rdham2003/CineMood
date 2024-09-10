import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, hamming_loss, jaccard_score, confusion_matrix
import warnings
import pickle

df = pd.read_csv("VIP Files\movieWeatherTimeData2.csv")
df.head()

df1 = df.drop(columns=["Movie Title"],axis=1)
df1.head()

#feature variables
X = df1[["Weather", "Time"]]
print(X.head())
#label variables
Y = df1.drop(columns=["Weather", "Time"])
print(Y.head())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

multiLabelRandomForest = MultiOutputClassifier(RandomForestClassifier(n_estimators=1200, max_depth=6, random_state=1))
multiLabelRandomForest.fit(X_train, Y_train)

Y_pred = multiLabelRandomForest.predict(X_test)

precision = precision_score(Y_test, Y_pred, average='macro', zero_division=1)
recall = recall_score(Y_test, Y_pred, average='macro', zero_division=1)
f1 = f1_score(Y_test, Y_pred, average='macro', zero_division=1)
classReport = classification_report(Y_test, Y_pred)
hammingLoss = hamming_loss(Y_test, Y_pred)
jaccard = jaccard_score(Y_test, Y_pred, average='macro')


#Precision: How many predictioms that were predicted positive were actually positive: True Pos/True Pos + False Pos. Desired Value: ≈ 1
#Recall: How many positives were identified by the classifier: True Pos/True Pos + False Neg. Desired Value: ≈ 1
#F1 Score: Average of Precision and Recall. Desired Value: ≈ 1
#Classification Report: Breakdown of Precision, Recall and F1 Score
#Hamming Loss: Fraction of incorrect labels to total labels. Desired value: ≈ 0
#Jaccord Score: Takes the predicted and true label sets and divies their intersection by their union. Desired Value: ≈ 1

print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print(f'Classification Report: \n{classReport}')
print(f'Hamming Loss: {hammingLoss}')
print(f'Jaccard Score: {jaccard}')

# Precision: 0.9831983475437605
# Recall: 0.9839030825919184
# F1 Score: 0.9832769498335231
# Classification Report:
#               precision    recall  f1-score   support

#            0       0.98      1.00      0.99       479
#            1       0.99      1.00      0.99       756
#            2       0.99      1.00      0.99       756
#            3       0.99      1.00      0.99       756
#            4       0.97      1.00      0.99       355
#            5       0.99      0.99      0.99       995
#            6       0.99      0.94      0.96       707
#            7       1.00      1.00      1.00       438
#            8       0.98      1.00      0.99      1124
#            9       0.94      1.00      0.97       704
#           10       1.00      1.00      1.00        76
#           11       0.98      1.00      0.99       451
#           12       0.98      0.92      0.95       712
#           13       0.98      0.92      0.95       712
#           14       0.98      0.97      0.98       122
#           15       1.00      0.98      0.99       223
#           16       0.98      1.00      0.99       586
#           17       0.98      1.00      0.99       596

#    micro avg       0.98      0.98      0.98     10548
#    macro avg       0.98      0.98      0.98     10548
# weighted avg       0.98      0.98      0.98     10548
#  samples avg       0.87      0.86      0.86     10548

# Hamming Loss: 0.010444444444444444
# Jaccard Score: 0.9675386606377953

def confusionMatrix(Y, Y_pred, genre):
    conmat = confusion_matrix(Y, Y_pred)
    
    # plt.figure(figsize=(15,8))
    # sns.heatmap(conmat, annot=True, cmap="RdBu")
    # plt.xlabel('Predicted')
    # plt.ylabel('Actual')
    # plt.title(f'Confusion Matrix for {genre}')
    # plt.show()
    
def plot_confusion_matrices(Y_test, Y_pred, genres):
    for i, genre in enumerate(genres):
        confusionMatrix(Y_test[:,i], Y_pred[:,i], genre)

genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'History', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']


Y_test = np.array(Y_test)
Y_pred = np.array(Y_pred)

# plot_confusion_matrices(Y_test, Y_pred, genres)


#For each Confusion Matrix, the values represent as followed:

#Top Left: True Negative
#Top Right: False Positive
#Bottom Left: False Negative
#Bottom Right: True Positive

warnings.filterwarnings("ignore", message="X does not have valid feature names")
model_test = np.array([600,10.25]).reshape(1,-1)

print(model_test)

pred = multiLabelRandomForest.predict(model_test)

print(pred[0])

with(open('model.pkl', 'wb')) as model_file:
    pickle.dump(multiLabelRandomForest, model_file)
    print("Saved model to pickle file")