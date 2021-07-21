import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
rf_Grid = RandomizedSearchCV(estimator = svm_model, param_distributions = param_grid, cv = 3, verbose = 2, n_jobs = 4)

inversion_data = pd.DataFrame()
excelFile = pd.ExcelFile("Plant Data.xlsx")
sheets = excelFile.sheet_names

for sheet in sheets: # loop through sheets inside an Excel file
            df = excelFile.parse(sheet_name = sheet)
            inversion_data = inversion_data.append(df)
            
inversion_data.info()
inversion_data['avgTemp'] = inversion_data['avgTemp'].astype(float)
features = ['avgDP', 'avgTemp', 'avgWindSPD']
check_rows = features[:]
check_rows.append('inversion')
inversion_data = inversion_data.dropna(subset = check_rows)

X = inversion_data.drop(columns = ['inversion', 'date'])
#inversion is the output, so I will drop

y = inversion_data['inversion']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 20) 
svm = SVC(kernel = 'rbf')
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

svm.score(X_test, y_test) 
#hyperparamter optimization
param_grid = {'C' : [.1, 1, 10, 100],
            'gamma' : [1, .1, .01, .001],
            'kernel' : ['rbf']}

svm_model = SVC(gamma = 'auto')
rf_Grid.fit(X , y)
rf_Grid.best_params_
rf_Grid.best_estimator_
best_model = SVC(gamma = .1, kernel = 'rbf', C = 10)
best_model.fit(X_train, y_train)
best_model.score(X_test, y_test) #75 percent accurate