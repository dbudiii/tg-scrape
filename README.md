# tg-scrape

To install cryptg: pip install telethon-tgcrypto

Telegram Scraper Bot: Bot will scrape for token addresses in specific telegram chats and pull specific financial data to be displayed. It will look to pull:

- Token name [DONE]
- Token Symbol [DONE]
- Write into database, making the address and timestamp unique identifiers [DONE]
- Number of times it has been mentioned in chats

To Do:
- Create function to count the number of times a token is mentioned and display the top 5
 

Optional:
- FDV
- Liquidity
- Pair created for how long
- Transactions for the past 5min, 1 hour, 6 hour, 24 hour
- Volume for the past 5min, 1 hour, 6 hour, 24 hour
- Performance for the past 5min, 1 hour, 6 hour, 24 hour
- Sentiment analysis
