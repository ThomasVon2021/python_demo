import pandas as pd
import os

df = pd.read_excel('apps_1545.xlsx')

len = df.shape[0] #获取数据总的行数

for i in range(len):
    str_year = str(df.loc[i]["LaunchDate"])
    str_year = str_year[0:4]
    if(str_year != "2019"):
        df.drop([i],inplace=True,axis=0) #删除指定行

print(df)
df.to_excel('2019.xlsx')
