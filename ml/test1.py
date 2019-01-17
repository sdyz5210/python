#!/usr/bin/python
#coding:utf-8
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,classification_report,confusion_matrix
from sklearn.preprocessing import MinMaxScaler  # 标准化数据
from sklearn.preprocessing import StandardScaler
#m = MinMaxScaler()
s = StandardScaler()

datas = pd.read_excel('/home/celloud/zhangyan/work17/20181109.xlsx', sheet_name=1)
datas_test = pd.read_excel('/home/celloud/zhangyan/work17/20181109.xlsx', sheet_name=2)

X = datas.iloc[:,0:-1] 
y = datas.iloc[:,-1] 

#print(X)
print("X shape :",X.shape)
print("y shape :",y.shape)

#过采样（SMOTE）
from imblearn.over_sampling import SMOTE
X_resampled_smote, y_resampled_smote = SMOTE(random_state=18).fit_sample(X, y)

print("X_resampled_smote shape :",X_resampled_smote.shape)
print("y_resampled_smote shape :",y_resampled_smote.shape)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_resampled_smote, y_resampled_smote, test_size=0.2, random_state=16) #默认shuffle=True
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=16) #默认shuffle=True
X_test = datas_test.iloc[:,0:-1].values 
y_test = datas_test.iloc[:,-1].values  

print("X_train shape :",X_train.shape)
print("X_test shape :",X_test.shape)

X_train = s.fit_transform(X_train)
X_test = s.transform(X_test)

param_test= {'C':[1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,0.3,0.5,0.6,0.7,0.8,0.9,1,1.5,2,3,4,5,10,100,1000,1e4,1e5,1e6,1e7],'penalty': ['l1','l2']}


lr = LogisticRegression()   

from sklearn.model_selection import GridSearchCV
gcv = GridSearchCV(estimator = lr , param_grid = param_test, scoring='roc_auc', cv=5) #roc_auc

gcv.fit(X_train,y_train)
print(gcv.best_params_, gcv.best_score_)

y_predict = gcv.predict(X_test)

#print('y_test:', y_test.tolist())
#print('y_predict:', y_predict)
print('Accuracy of gcv_train :', gcv.score(X_train, y_train))
print('Accuracy of gcv_test  :', gcv.score(X_test, y_test))
print('accuracy_score       :', accuracy_score(y_test, y_predict))
print('precision_score      :', precision_score(y_test, y_predict))
print('recall_score         :', recall_score(y_test, y_predict))
print('f1_score             :', f1_score(y_test, y_predict))
print('confusion_matrix:')
print(confusion_matrix(y_test, y_predict))  #横向标签，纵向预测
print(confusion_matrix(y_test, y_predict).T) #横向预测，纵向标签
print(classification_report(y_test, y_predict, target_names=['label_0', 'label_1']))
print(gcv)

