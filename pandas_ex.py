# -*- Encoding: UTF-8 -*- #

import pandas as pd

dataframe_ex = pd.DataFrame({'서울지표':[100, 110, 120, 130, 135], 
              '부산지표':[70, 90, 80, 90, 100], 
              '대구지표':[50, 60, 65, 69, 80]}, 
             index=[2016, 2017, 2018, 2019, 2020])

#print(dataframe_ex)
#print(dataframe_ex['서울GDP'][2020])
#print(dataframe_ex.loc[2020]['서울GDP'])

#series_ex2 = pd.Series([100, 90, 120, 110, 105], index=['월', '화', '수', '목', '금'])

print(dataframe_ex.sort_values(by='서울지표', ascending=False),end='\n\n')

print(dataframe_ex[ dataframe_ex['부산지표'] > 80 ])
