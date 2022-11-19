import os


from dotenv import load_dotenv


from bot import ExchangesRatesBot, BotMessages
from net_data import NetRequests
from storage import Storage


def create_net():
    net = NetRequests(os.getenv("CBR_DAILY_DATA_URL"))
    return net


def create_storage(net: NetRequests):
    storage = Storage(net)
    return storage


def create_bot_messages():
    messages = BotMessages()
    return messages


def create_exchange_bot(messages: BotMessages, storage: Storage):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = ExchangesRatesBot(token, messages, storage)
    return bot


def start():
    load_dotenv()
    net = create_net()
    storage = create_storage(net)
    messages = create_bot_messages()
    bot = create_exchange_bot(messages, storage)
    bot.start(skip_updates=True)


if __name__ == '__main__':
    start()
