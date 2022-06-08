import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from datetime import date,tzinfo
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest 
   
def inputPrediction(initial1,final1):
    dataset=pd.read_csv("Date&Transactionvalue.csv")
    dataset
    data1=pd.read_csv("Transactions.csv")
# In[27]:
    result1 = pd.merge(data1,dataset,on='Date')
    result1['Date'] = result1['Date'].astype('datetime64[ns]')
    result =result1.loc[(result1['Date'].dt.year>=int(initial1)) &(result1['Date'].dt.year<=int(final1) )]
    data3 = result[['Transaction_value','block','Transactions']]
    outliers_fraction=0.05
    scaler = StandardScaler()
    np_scaled = scaler.fit_transform(data3)
    data3 = pd.DataFrame(np_scaled)
# train isolation forest
    model =  IsolationForest(contamination=outliers_fraction)
    model.fit(data3)
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111,projection='3d')
    X = result.iloc[:,1:4].values
    colors = np.array(['red', 'blue'])
    y_pred = model.fit_predict(data3)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], s=25, color=colors[(y_pred + 1) // 2] )
    plt.title('Transactions vs block vs Sum of Transaction_value: Red represents Anomalies')
    result['anomaly_IsolationForest'] = model.predict(data3)
    result['anomaly_IsolationForest'] = result['anomaly_IsolationForest'].apply(lambda x: x == -1)
    result['anomaly_IsolationForest'] = result['anomaly_IsolationForest'].astype(int)
    return result['anomaly_IsolationForest'].value_counts()
pickle.dump(IsolationForest,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


#print(inputPrediction(2012,2013))