# -*- Encoding: UTF-8 -*- #

import pandas as pd

dataframe_ex = pd.DataFrame({'서울지표':[100, 110, 120, 130, 135], 
              '부산지표':[70, 90, 80, 90, 100], 
              '광주지표':[50, 60, 65, 69, 80]}, 
             index=[2016, 2017, 2018, 2019, 2020])

print(dataframe_ex)
#print(dataframe_ex['서울GDP'][2020])
#print(dataframe_ex.loc[2020]['서울GDP'])