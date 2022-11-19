from aiogram import Bot, Dispatcher, executor, types


from .models.bot_messages import BotMessages
from storage import Storage


class ExchangesRatesBot:
    _token: str
    _messages: BotMessages
    _bot: Bot
    _dispatcher: Dispatcher
    _storage: Storage

    @property
    def bot(self):
        return self._bot

    @property
    def dispatcher(self):
        return self._dispatcher

    def __init__(self, token: str, messages: BotMessages, storage: Storage):
        self._token = token
        self._messages = messages
        self._storage = storage

        self._bot = Bot(self._token)
        self._dispatcher = Dispatcher(self._bot)

        self._init_handlers()

    def currency_message(self, currency: dict) -> str:
        return self._messages.currency.format(
            code=currency['CharCode'],
            name=currency['Name'],
            last=currency['Value']/currency['Nominal'],
            previous=currency['Previous']/currency['Nominal']
        )

    def _init_handlers(self):
        @self._dispatcher.message_handler(commands=["start"])
        async def greeting(message: types.Message):
            await message.reply(self._messages.start)

        @self._dispatcher.message_handler(lambda message: len(message.text) == 3 and message.text.upper() in self._storage.currencies())
        async def exchange_rate(message: types.Message):
            await message.reply(self.currency_message(self._storage.currencies()[message.text.upper()]))

    def start(self, skip_updates: bool):
        executor.start_polling(self._dispatcher, skip_updates=skip_updates)
