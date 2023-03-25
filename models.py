import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def predict_di(data):
    df=pd.read_csv("kc_house_data.csv")
    df=df.drop('id',axis=1)
    df.drop('sqft_lot',axis=1,inplace=True)
    df.drop('floors',axis=1,inplace=True)
    df.drop('waterfront',axis=1,inplace=True)
    df.drop('view',axis=1,inplace=True)
    df.drop('condition',axis=1,inplace=True)
    df.drop('yr_built',axis=1,inplace=True)
    df.drop('yr_renovated',axis=1,inplace=True)
    df.drop('zipcode',axis=1,inplace=True)
    df.drop('long',axis=1,inplace=True)
    df.drop('sqft_lot15',axis=1,inplace=True)
    df.drop('date',axis=1,inplace=True)
    x=df.drop('price',axis=1)
    y=df['price']
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/3,random_state=0)
    sc=StandardScaler()
    lg= LogisticRegression()
    x_train=sc.fit_transform(x_train)
    x_test=sc.transform(x_test)
    lg.fit(x_train,y_train)
    pre=lg.predict(data)
    return pre