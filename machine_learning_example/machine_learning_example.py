from sklearn import tree
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

iris = pd.read_csv('iris.csv')
features = iris.iloc[:,0:4]
labels = iris['class']

train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size=0.2)    

#clf = tree.DecisionTreeClassifier()
clf = RandomForestClassifier()


clf.fit(train_feats, train_labels)

predictions = clf.predict(test_feats)
#predictions = clf.predict([['7', '3.2', '4.7', '1.4']])
#
#print(predictions)


print('Expected\t', 'Predicted')
for index, prediction in enumerate(predictions,0):
    print(test_labels.iloc[index], '\t\t', prediction)
    
    if prediction != test_labels.iloc[index]:
        print ('not matched')
        
        
print ('Accuracy', str(accuracy_score(test_labels, predictions)*100) + '%')
