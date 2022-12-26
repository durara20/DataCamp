import pandas as pd 
import numpy as np 
np.random.seed = 2021
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from knnclass import KNN

iris = load_iris()
X, y, labels, feature_names  = iris.data, iris.target, iris.target_names, iris['feature_names']
df_iris= pd.DataFrame(X, columns= feature_names) 
df_iris['label'] =  y
features_dict = {k:v for k,v in  enumerate(labels)}
df_iris['label_names'] = df_iris.label.apply(lambda x: features_dict[x])

X=iris.data
y=iris.target

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=1)

scaler= MinMaxScaler()
X_train_scaled= scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
 
k_best = 0 # 'compute the best k'
score_best = 0 #'compute the best score'
for k in range(1,len(X_test)):#second parameter is a size of a test set
    model=KNN(k_neighbours=k)
    model.fit(X_train_scaled,y_train)
    score = model.score(X_test_scaled,y_test)
    if score>score_best:
        score_best=score
        k_best=k
    
print ('The best k = {} , score = {}'.format(k_best,score_best ))