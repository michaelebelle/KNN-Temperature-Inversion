import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
inversion_data = pd.DataFrame()
excelFile = pd.ExcelFile("Plant Data.xlsx")
sheets = excelFile.sheet_names

for sheet in sheets: # loop through sheets inside an Excel file
            df = excelFile.parse(sheet_name = sheet)
            inversion_data = inversion_data.append(df)
            
print(inversion_data)

inversion_data['avgTemp'] = inversion_data['avgTemp'].astype(float)
features = ['avgDP', 'avgTemp', 'avgWindSPD']
check_rows = features[:]
check_rows.append('inversion')
inversion_data = inversion_data.dropna(subset = check_rows)
inversion_data.info()
# 
X = inversion_data.drop(columns = ['inversion', 'date'])
#inversion is the output, so I will drop

y = inversion_data['inversion']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 20) 

# len(y_train)

clf = KNeighborsClassifier(n_neighbors = 1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

scores = [] #hyperparamater tuning for the number of neighbors we need

for n in range(1, 20):
    clf = KNeighborsClassifier(n_neighbors = n)
    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))

import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(range(1,20), scores)