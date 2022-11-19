from net_data import NetRequests


class Storage:
    _net: NetRequests
    _exchange_rates: dict

    @property
    def net(self):
        return self._net

    @property
    def exchange_rates(self):
        return self._exchange_rates

    def __init__(self, net: NetRequests):
        self._net = net
        self.data_init()

    def data_init(self):
        self._exchange_rates = self._net.get_rates()

    def currencies(self):
        return self._exchange_rates['Valute']
