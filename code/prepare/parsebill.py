from code.constants import path_fmt,col_names,table_set
import pandas as pd
import numpy as np
from os import path

table = "bill_detail"
datatype = 'train'

prepath = path.dirname(__file__)
input_path = path.join(prepath,path_fmt[table]%(datatype,datatype))
output_path = path.join(prepath,'../../tmp/bill_detail_clean.csv')

df = pd.read_csv(input_path,header = None)
df.columns = col_names[table]

'''col = ["PayStatus"]'''
df_group = df[df.PayStatus == 0].groupby(by = 'uid')
res_dic = dict()
for uid,group in df_group:
    selectFeature = dict(
                    billNum=group.shape[0],
                    bankNum = len(np.unique(group['bankid'])),
                    AvgLastBill = group['LastBill'].mean(),
                    MaxCreditAmount =group['CreditAmount'].max(),
                    AvgCurrentBalance = group['CurrentBalance'].mean(),
                    AvgCurrentleastPayment = group['CurrentleastPayment'].mean(),
                    AvgTransactionNum = group['TransactionNum'].mean(),
                    MaxTransactionNum = group['TransactionNum'].max(),
                    AvgCurrentBill = group['CurrentBill'].mean(),
                    )

    res_dic[uid] = selectFeature
print 'need selecting more features'
res_df = pd.DataFrame(res_dic)

res_df.to_csv(output_path)