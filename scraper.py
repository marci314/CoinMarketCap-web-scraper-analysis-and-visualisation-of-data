import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

def get_data():
    # desired columns containing information about cryptocurrencies that we will fill while scraping and then create a dataframe for further analysis
    dates = []
    names = []
    symbols = []
    market_caps = []
    prices = []
    circulating_supplies = []
    volumes_24hr = []
    pct_changes_7day = []
    # empty dataframe
    df = pd.DataFrame()
    
    # function that scrapes urls for all available dates and appends them into list
    all_dates = []
    def scrape_date():
        url = 'https://coinmarketcap.com/historical/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        a_tags = soup.find_all('a', class_='historical-link cmc-link')
        for tag in a_tags:
            href = tag.get('href')
            all_dates.append(href)
    
    # scrape available dates
    scrape_date()
    
    # Filter the dates to include only those up to 2024-07-28 and within the last 192 weeks
    cutoff_date = datetime.strptime("20240728", "%Y%m%d")
    start_date = cutoff_date - timedelta(weeks=192)
    filtered_dates = [date for date in all_dates if start_date <= datetime.strptime(date.split('/')[-2], "%Y%m%d") <= cutoff_date]
    
    # function that will scrape data on cryptocurrency on given date, meaning we can loop through list of dates and get data on all dates
    def scrape_data_date(date):
        url = 'https://coinmarketcap.com' + date
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        tr = soup.find_all('tr', attrs={'class': 'cmc-table-row'})
        count = 0
        for row in tr:
            if count == 10:
                break
            count += 1

            try:
                crypto_date = date
            except AttributeError:
                crypto_date = None
            dates.append(crypto_date)

            try:
                name_column = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
                crypto_name = name_column.find('a', attrs={'class': 'cmc-table__column-name--name cmc-link'}).text.strip()
            except AttributeError:
                crypto_name = None
            names.append(crypto_name)

            try:
                crypto_symbol = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol'}).text.strip()
            except AttributeError:
                crypto_symbol = None
            symbols.append(crypto_symbol)

            try:
                crypto_market_cap = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
            except AttributeError:
                crypto_market_cap = None
            market_caps.append(crypto_market_cap)

            try:
                crypto_price = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
            except AttributeError:
                crypto_price = None
            prices.append(crypto_price)

            try:
                crypto_circulating_supply = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip().split(' ')[0]
            except AttributeError:
                crypto_circulating_supply = None
            circulating_supplies.append(crypto_circulating_supply)

            try:
                crypto_volume_24hr_td = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h'})
                crypto_volume_24hr = crypto_volume_24hr_td.find('a', attrs={'class': 'cmc-link'}).text.strip()
            except AttributeError:
                crypto_volume_24hr = None
            volumes_24hr.append(crypto_volume_24hr)

            try:
                crypto_pct_7day = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d'}).text.strip()
            except AttributeError:
                crypto_pct_7day = None
            pct_changes_7day.append(crypto_pct_7day)
    
    # get first and last available dates so we know which time frame is available for analysis
    date_format = "%Y%m%d"
    first_date = datetime.strptime(all_dates[0].split('/')[-2], date_format).strftime('%Y-%m-%d')
    last_date = datetime.strptime(all_dates[-1].split('/')[-2], date_format).strftime('%Y-%m-%d')
        
    # loop through all filtered dates (urls) up to 2024-07-28 within the last 192 weeks
    for date in filtered_dates[:30]:
        scrape_data_date(date)

    # combine extracted lists (columns) into dataframe
    df = pd.DataFrame({
        'Date': dates,
        'Name': names,
        'Symbol': symbols,
        'Market Cap ($)': market_caps,
        'Price ($)': prices,
        'Circulating Supply ($)': circulating_supplies,
        'Volume (24hr) ($)': volumes_24hr,
        '% 7d': pct_changes_7day
    })

    return df

