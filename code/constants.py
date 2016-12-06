

table_set = ["loan_time","browse_history","bank_detail","bill_detail","user_info","overdue"]
path_fmt = dict(
            loan_time = "../../data/%s/loan_time_%s.txt",
            browse_history = "../../data/%s/browse_history_%s.txt",
            bank_detail = "../../data/%s/bank_detail_%s.txt",
            bill_detail = "../../data/%s/bill_detail_%s.txt",
            user_info= "../../data/%s/user_info_%s.txt",
            overdue = "../../data/%s/overdue_%s.txt"
            )

col_names = dict(
                overdue = ['uid','overdue'],
                loan_time = ['uid','timestamp'] ,
                browse_history = ["uid","timestamp","pv","BrowseType"],
                bank_detail = ["uid","timestamp","iTradeType","iCost","IncomeFlag"],
                bill_detail =["uid","timestamp","bankid","LastBill","LastPayment","creditAmount","CurrentBalance","CurrentleastPayment","TransactionNum","CurrentBill","AdjustAmt","CycleInterest","AvalibeLAmt","PreBorrowAmt" ,"paystatus"] ,
                user_info = ["uid","sex","career","education","MaritalStatus","ResidenceType"],
                )