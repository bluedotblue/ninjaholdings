import pandas as pd

#Loading both customers and tranactions csvs relative path
customers = pd.read_csv(r'customers (2).csv')
transactions = pd.read_csv(r'transactions (1) (1).csv')

#Data cleaning, converted column datatypes, dropped nulls and duplicate values
customers = customers.convert_dtypes()
customers_convert_dates = customers[['signup_date']].astype('datetime64[us]')
customers = customers.drop(columns = ['signup_date'])
customers = pd.concat([customers, customers_convert_dates], axis = 1).dropna().drop_duplicates()
transactions = transactions.convert_dtypes()
transactions_convert_dates = transactions[['transaction_date']].astype('datetime64[us]')
transactions = transactions.drop(columns = ['transaction_date'])
transactions = pd.concat([transactions, transactions_convert_dates], axis = 1).dropna().drop_duplicates()

#Grouping transaction amounts by customer and month 
months = transactions['transaction_date'].dt.month.to_frame().rename(columns = {'transaction_date': 'transaction_month'})
t = pd.concat([transactions, months], axis = 1)
transformed_transactions = t.groupby(by = ['customer_id','transaction_month']).amount.agg('sum').to_frame()
transformed_transactions.to_csv('transformed_transactions.csv')

print("ETL Processing of customers and transactions csvs complete. \nOutput saved to transformed_transactions.csv")