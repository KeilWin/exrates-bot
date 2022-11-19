import os


class BotMessages:
    _start: str
    _currency: str

    @property
    def start(self):
        return self._start

    @property
    def currency(self):
        return self._currency

    def __init__(self):
        self._start = os.getenv('TELEGRAM_MESSAGE_START_RU')
        self._currency = os.getenv('TELEGRAM_MESSAGE_CURRENCY')
