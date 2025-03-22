# tg-scrape

[Finished]

To install cryptg: pip install telethon-tgcrypto

Telegram Scraper: Script will scrape for token addresses across all telegram chats and show the top mentions to show popularity across your chat groups. It will look to pull:
- Token address
- Timestamp
- Number of times the token has been mentioned across all chats

Main Functionality:
- Scrape messages across chats and pull token addresses [DONE]
- Write into database, making the address and timestamp unique identifiers [DONE]
- Number of times it has been mentioned in chats [DONE]
- Print the addresses that were captured in chronological order [DONE]

Future Functionality:
- Have it count the number of token mentions by date period rather than number of messages per chat (use get_token_counts function)
- Pull token symbol and name using API
- FDV
- Liquidity
- Pair created for how long
- Transactions for the past 5min, 1 hour, 6 hour, 24 hour
- Volume for the past 5min, 1 hour, 6 hour, 24 hour
- Performance for the past 5min, 1 hour, 6 hour, 24 hour
- Sentiment analysis
