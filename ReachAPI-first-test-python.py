import requests

URL = 'https://apitempo.inmet.gov.br/estacao/dados/2020-05-02'


def fetch(session, url):
    with session.get(url) as response:
        a = response.json()
        print(a[0]["PTO_MAX"])


def main():
    with requests.Session() as session:
        # for _ in range(100):
        fetch(session, URL)

main()
