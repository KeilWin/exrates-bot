# Exchange Rates Telegram Bot
Telegram bot to view exchange rate of some currencies.
For work, need to create .env file:

Telegram token

```TELEGRAM_BOT_TOKEN=""```

Start message

```TELEGRAM_MESSAGE_START_EN="Hello, this bot exists to get exchange rates against the ruble (RUB) by ISO code (USD, EUR...)"

TELEGRAM_MESSAGE_START_RU="Добро пожаловать, этот бот существует для получения курсов валют к рублю(RUB) по ISO-коду(USD, EUR...)"
```

Answer template for requested currency

```TELEGRAM_MESSAGE_CURRENCY="{code}\n{name}\n{last}\n{previous}"```

Resource with exchange data

```CBR_DAILY_DATA_URL = "https://www.cbr-xml-daily.ru/daily_json.js"```
