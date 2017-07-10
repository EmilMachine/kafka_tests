from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
iris = load_iris()

data_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

data_df.to_csv('./test_data.csv',index=False)
data_df.to_json(path_or_buf='./test_data.json',orient='records')

