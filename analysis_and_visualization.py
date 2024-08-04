import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def which_coins(dict):
    for coin in dict.keys():
        print(coin)

def selected_coins(dict, selected_list):
    selected_dict = {coin: dict[coin] for coin in selected_list if coin in dict}
    return selected_dict

def selected_coins_table(table, selected_list):
    selected_table = table[table['Symbol'].isin(selected_list)]
    return selected_table


def plot_prices(table_dict, column_name):
    plt.figure(figsize=(14, 7))  
    
    for name, table in table_dict.items():
        if column_name in table.columns:
            plt.plot(table['Date'], table[column_name], label=f"{name} {column_name}")
    
    plt.title(f"Price Movement of Coins")
    plt.xlabel("Date")
    plt.ylabel("Price in $")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_market_cap(table_dict, column_name='Market Cap ($)'):
    plt.figure(figsize=(14, 7))  
    
    for name, table in table_dict.items():
        if column_name in table.columns:
            plt.plot(table['Date'], table[column_name], label=f"{name} {column_name}")
    
    plt.title(f"Market Cap Movement of Coins")
    plt.xlabel("Date")
    plt.ylabel("Market Cap in $")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_volume(table_dict, column_name='Volume (24hr) ($)'):
    plt.figure(figsize=(14, 7))  
    
    for name, table in table_dict.items():
        if column_name in table.columns:
            plt.plot(table['Date'], table[column_name], label=f"{name} {column_name}")
    
    plt.title(f"Movement of  24-Hour Volume of Coins")
    plt.xlabel("Date")
    plt.ylabel("Volume in $")
    plt.grid(True)
    plt.legend()
    plt.show()

def weekly_volatility(table_dict):
    print("Weekly Volatility:")
    for name, table in table_dict.items():
        weekly = table["% 7d"].std()
        print(f"{name}: ", '{:.2f}'.format(weekly), "%")
    
def plot_volatility(table_dict):
    plt.figure(figsize=(10, 5))
    
    for name, table in table_dict.items():
        if "% 7d" in table.columns:
            table["% 7d"].hist(bins=50, label=f"{name}", alpha=0.5)

    plt.legend()
    plt.title("Distribution of Weekly Returns")
    plt.xlabel("Weekly Return in %")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.show()

import plotly.express as px
def interactive_cumulative(table_dict):
    combined_df = pd.DataFrame()

    
    for name, table in table_dict.items():
        table["Cumulative_Return (%)"] = ((1 + table["% 7d"].astype(float) / 100).cumprod() - 1) * 100
        table["Symbol"] = name
        combined_df = pd.concat([combined_df, table], ignore_index=True)
    
   
    fig = px.line(combined_df,
                  x="Date",
                  y="Cumulative_Return (%)",
                  color="Symbol",
                  title="Weekly Cumulative Return for All Cryptocurrencies",
                  labels={"Cumulative_Return (%)": "Weekly Cumulative Return (%)"})
    fig.show()

def calculate_crypto_roi(table_dict, frequency=20):
    crypto_names = []
    profit_loss_data = []
    final_amounts = []
    total_portfolio_value = 0
    print("Final outcome of the strategy:")
    
    for name, table in table_dict.items():
        num_coins_bought = 0.0
        invested_money = 0.0
        selling_price = table["Price ($)"].iloc[-1]
        
        for row_index in range(len(table)):
            row = table.iloc[row_index]
            if row_index % frequency == 0:
                current_price = row["Price ($)"]
                num_coins_bought += 0.01
                invested_money += current_price * 0.01
        
        print(" ")
        print(f"Coins of {name} owned: {num_coins_bought}")
        print(f"Money invested in {name}: {round(invested_money, 2)} $.")
        
        if invested_money >= num_coins_bought * selling_price:
            loss = num_coins_bought * selling_price - invested_money
            print(f"Loss: {round(loss, 2)}$")
            profit_loss_data.append(loss)
        else:
            profit = num_coins_bought * selling_price - invested_money
            print(f"Profit: {round(profit, 2)}$")
            profit_loss_data.append(profit)
        
        print(" ")
        total_portfolio_value += num_coins_bought * current_price
        crypto_names.append(name)
        final_amounts.append(num_coins_bought * current_price)
    
    plt.figure(figsize=(10, 8))
    colors = ["blue", "green", "red", "purple", "orange"]
    plt.bar(crypto_names, profit_loss_data, color=colors)
    plt.title("Profit/Loss")
    plt.xlabel("Cryptocurrencies")
    plt.ylabel("Amount in $")
    plt.show()

def calculate_correlation_matrix(df, columns):
    selected_data = df[columns]
    correlation_matrix = selected_data.corr()
    
    return correlation_matrix

# add moving average
def moving_average(table_dict, days):
    for name, table in table_dict.items():
        table[f"Moving_Average_{days}"] = table["Price ($)"].rolling(days).mean()
        table_dict[name] = table
    return table_dict



    