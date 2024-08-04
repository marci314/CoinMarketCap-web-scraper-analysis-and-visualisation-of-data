# CoinMarketCap-web-scraper-analysis-and-visualisation-of-data

Author: Marcel Blagotinšek

In the course Introduction to Programming, I prepared a project focused on data analysis of cryptocurrencies. In this project, I selected several major cryptocurrencies, imported and extracted the necessary data for further analysis, saved the tables (files named crypto_symbol.csv in the "data" directory), and finally presented the results using Jupyter Notebook.

The cryptocurrency data required for this analysis is sourced from CoinMarketCap. The scripts for data acquisition, cleaning, and analysis are written in separate .py files, while in Jupyter Notebook, I call and execute functions from these files to keep the workflow organized and clear.

## USAGE AND INSTRUCTIONS

The script scraper.py contains the program designed to fetch data exclusively from CoinMarketCap. Although the Jupyter Notebook includes findings and results for my chosen set of cryptocurrencies and the observation period, users can modify scripts in order to set their own interval and set of cryptocurrencies before running the Jupyter Notebook. It is crucial to ensure that the date is formatted correctly and that the cryptocurrency symbols are accurate according to CoinMarketCap. While the results of the analysis for other cryptocurrencies may differ, the user will still obtain various calculations and visualizations of price movements, market capitalization, and more, which can then be used for their own analysis and presentations.

When users download all the necessary .py files and the main project file .ipynb, they need to ensure that all required packages are installed if they haven't already done so. The packages I used are: requests, datetime, bs4, pandas, numpy, matplotlib.pyplot, plotly.express, and os. After installing the required packages, users can run the program located in the report.ipynb file.

### PROJECT FILES

1. scraper.py: Contains the script for fetching historical cryptocurrency data from CoinMarketCap.
2. prettify.py: Includes functions to clean and format the fetched data.
3. transform.py: Contains functions to split, save, and manage data for individual cryptocurrencies.
4. analysis_and_visualization.py: Includes various functions for analyzing and visualizing the cryptocurrency data.
5. report.ipynb: The main Jupyter Notebook file that calls functions from the above scripts, performs the analysis, and presents the results.

By following these steps, users can replicate the analysis for their chosen set of cryptocurrencies and observation periods, leveraging the scripts provided to gain insights and present their findings effectively.
