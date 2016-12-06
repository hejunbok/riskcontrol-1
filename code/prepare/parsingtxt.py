from code.constants import path_fmt,col_names,table_set
import pandas as pd

datatype = 'train'
df_set = dict()
'''table_set = ["loan_time","browse_history","bank_detail","bill_detail","user_info","overdue"]'''
for table in table_set:
    path = path_fmt[table]%(datatype,datatype)
    df = pd.read_csv(path,header = None)
    df.columns = col_names[table]
    df_set[table] = df
    print table

'''merge X and Y into table'''

res_df = pd.merge(df_set['overdue'],df_set['loan_time'],how = 'left',on = 'uid')
res_df = pd.merge(res_df,df_set['user_info'],how = 'left',on = 'uid')

print res_df.head()
res_df.to_csv('../../tmp/XY.csv')




