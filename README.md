# tg-scrape

To install cryptg: pip install telethon-tgcrypto

Telegram Scraper Bot: Bot will scrape for token addresses in specific telegram chats and pull specific financial data to be displayed. It will look to pull:

- Token name [DONE]
- Token Symbol [DONE]
- Number of times it has been mentioned in chats

To Do:
- Update 'insert_data' function to properly insert data pulled from telegram (might have to convert the code in tg_scrape from dictionary to list of tuples)
- Integrate 'insert_data' into main file to update the actual table
- Create function to count the number of times a token is mentioned
 

Optional:
- FDV
- Liquidity
- Pair created for how long
- Transactions for the past 5min, 1 hour, 6 hour, 24 hour
- Volume for the past 5min, 1 hour, 6 hour, 24 hour
- Performance for the past 5min, 1 hour, 6 hour, 24 hour
- Sentiment analysis

Todo: Start pulling financial data for tokens using API