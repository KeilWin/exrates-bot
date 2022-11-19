from net_data.net import NetRequests


def get_url(url):
    nr = NetRequests(url)
    response = nr.get_rates()
    print(response)


if __name__ == '__main__':
    get_url('https://www.cbr-xml-daily.ru/daily_json.js')
