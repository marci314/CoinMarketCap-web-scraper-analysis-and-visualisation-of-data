import pandas as pd

def clean_format(df):
    
    # with the following code we first transform date column in order to convert it to datetime type
    df['Date'] = pd.to_datetime(df['Date'].str.split('/').str[-2], format='%Y%m%d')
    
    # by inspecting dataframe mid cleaning we come across "$" and commas in columns and we replace them with ""
    df['Market Cap ($)'] = df['Market Cap ($)'].str.replace('[$,]', '', regex=True)
    df['Price ($)'] = df['Price ($)'].str.replace('[$,]', '', regex=True)
    df['Volume (24hr) ($)'] = df['Volume (24hr) ($)'].str.replace('[$,]', '', regex=True)
    df['Circulating Supply ($)'] = df['Circulating Supply ($)'].str.replace(',', '')

    # replace the sign that symbolizes no change with 0, and remove "<|>|%" from last column
    df['% 7d'] = df['% 7d'].str.replace('--', '0').str.lstrip('>').str.lstrip('<').str.rstrip('%')
    
    # for further analysis and calculations we need to convert whole table to numeric type    
    convert_to_num_type = ['Market Cap ($)', 'Price ($)', 'Circulating Supply ($)', 'Volume (24hr) ($)', '% 7d']
    df[convert_to_num_type] = df[convert_to_num_type].apply(lambda x: pd.to_numeric(x))
    df[convert_to_num_type] = df[convert_to_num_type].fillna(method="ffill")
    
    # rount to 3 decimal 
    columns_to_round = [col for col in df.columns if (col != "Date" or col != "Symbol" or col != "Name")]
    df[columns_to_round] = df[columns_to_round].round(3)

    return df

