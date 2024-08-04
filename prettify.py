import pandas as pd

def clean_format(df):
    # transform date column to datetime type
    df['Date'] = pd.to_datetime(df['Date'].str.split('/').str[-2], format='%Y%m%d')
    
    # replace "$" and commas in specified columns
    df['Market Cap ($)'] = df['Market Cap ($)'].str.replace('[$,]', '', regex=True)
    df['Price ($)'] = df['Price ($)'].str.replace('[$,]', '', regex=True)
    df['Volume (24hr) ($)'] = df['Volume (24hr) ($)'].str.replace('[$,]', '', regex=True)
    df['Circulating Supply ($)'] = df['Circulating Supply ($)'].str.replace(',', '')

    # replace symbols and percentage signs in the % 7d column
    df['% 7d'] = df['% 7d'].str.replace('--', '0').str.lstrip('>').str.lstrip('<').str.rstrip('%')
    
    # convert specified columns to numeric type and fill NaN values
    convert_to_num_type = ['Market Cap ($)', 'Price ($)', 'Circulating Supply ($)', 'Volume (24hr) ($)', '% 7d']
    df[convert_to_num_type] = df[convert_to_num_type].apply(lambda x: pd.to_numeric(x))
    df[convert_to_num_type] = df[convert_to_num_type].fillna(method="ffill")
    
    # round numeric columns to 3 decimal places
    columns_to_round = [col for col in df.columns if col not in ["Date", "Symbol", "Name"]]
    df[columns_to_round] = df[columns_to_round].round(3)

    return df
