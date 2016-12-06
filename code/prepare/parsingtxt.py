from code.constants import Y_path_fmt,X_path_fmt
import pandas as pd

datatype = 'train'

df = []

'''X'''
''' 1.user_info'''
X_path = X_path_fmt['user_info']%(datatype,datatype)
user_info_df = pd.read_csv(X_path,header = None)
user_info_df.columns = ["uid","sex","career","education","MaritalStatus","ResidenceType"]
df.append(user_info_df)

''' 2. bank_detail'''
X_path = X_path_fmt['bank_detail']%(datatype,datatype)
bank_detail_df = pd.read_csv(X_path,header = None)
bank_detail_df.columns = ["uid","timestamp","iTradeType","iCost","IncomeFlag"]
df.append(bank_detail_df)
''' 3. browse_history'''
X_path = X_path_fmt['browse_history']%(datatype,datatype)
browse_history_df = pd.read_csv(X_path,header = None)
browse_history_df.columns = ["uid","timestamp","pv","BrowseType"]
df.append(browse_history_df)

''' 4. bill_detail'''
X_path = X_path_fmt['bill_detail']%(datatype,datatype)
bill_detail_df = pd.read_csv(X_path,header = None)
bill_detail_df.columns = ["uid","timestamp","bankid","LastBill","LastPayment","creditAmount","CurrentBalance","CurrentleastPayment","TransactionNum","CurrentBill","AdjustAmt","CycleInterest","AvalibeLAmt","PreBorrowAmt" ,"paystatus"]
df.append(bill_detail_df)

'''5.loan_time'''
X_path = X_path_fmt['loan_time']%(datatype,datatype)
loan_time_df = pd.read_csv(X_path,header = None)
loan_time_df.columns = ['uid','timestamp']
df.append(loan_time_df)

'''6. Y'''
Y_path = Y_path_fmt%(datatype,datatype)
overdue_df = pd.read_csv(Y_path,header = None)
overdue_df.columns = ['uid','overdue']
df.append(overdue_df)

'''merge X and Y into table'''

res_df = pd.merge(df[-1],df[-2],how = 'left',on = 'uid')
res_df = pd.merge(res_df,df[0],how = 'left',on = 'uid')

print res_df.head()
res_df.to_csv('../../tmp/XY.csv')




