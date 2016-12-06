from code.constants import path_fmt,col_names
import pandas as pd


datatype = 'train'
table_set = ["overdue","loan_time","user_info",]

res_df = pd.DataFrame()
for table in table_set:
    path = path_fmt[table]%(datatype,datatype)
    df = pd.read_csv(path,header = None)
    df.columns = col_names[table]
    try:
        res_df = pd.merge(res_df,df, how='left', on='uid')
    except:
        res_df = df
res_df.to_csv('../../tmp/XY.csv')
