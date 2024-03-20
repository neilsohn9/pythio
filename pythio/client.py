import requests


class Client:
    def __init__(self, api_token: str, timeout: float = 10):
        self.api_token = api_token
        self.timeout = timeout
        self.session = requests.session()

        if not api_token:
            raise ValueError('`api_token` did\'t passed')

    @property
    def url(self) -> str:
        return f'https://api.telegram.org/bot{self.api_token}/'


    def request(self, method: str, payload: dict = None) -> dict:
        with self.session.post(url=self.url + method, data=payload, timeout=self.timeout) as responce:
            if responce.status_code != requests.codes.ok:
                print(__file__, responce.status_code, responce, __file)
            else:
                return responce.json()


    async def get_me(self) -> dict:
        return self.request(method='getme')
