from code.constants import Y_path_fmt,X_path_fmt
import pandas as pd

datatype = 'train'
'''Y'''
Y_path = Y_path_fmt%(datatype,datatype)
loan_time_df = pd.read_csv(Y_path,header = None)
loan_time_df.columns = ['id','loan_time']

'''X'''
'''1. bank_detail'''
X_path = X_path_fmt['bank_detail']%(datatype,datatype)
bank_detail_df = pd.read_csv(X_path,header = None)

'''GO ON'''



