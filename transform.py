import pandas as pd
import os

# for further analysis, we are going to split the table into multiple tables,
# where each table contains data only from one cryptocurrency
def split_by_symbol(df):
    symbol_dict = {}
    for symbol in df['Symbol'].unique():
        symbol_df = df[df['Symbol'] == symbol].copy()
        symbol_dict[symbol] = symbol_df
    return symbol_dict

def save_table(table, name):
    os.makedirs("data", exist_ok=True)
    file_name = f"{name}.csv"
    table.to_csv(os.path.join("data", file_name), index=False)

def save_tables_dict(table_dict):
    os.makedirs("data", exist_ok=True)
    for name, table in table_dict.items():
        file_name = f"{name}.csv"
        table.to_csv(os.path.join("data", file_name), index=False)
