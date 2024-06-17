import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    df = customers[customers['year'] == 2021]
    df = df.groupby(['customer_id', 'year'])['revenue'].sum().reset_index()
    return df[df['revenue'] > 0][['customer_id']]
   
