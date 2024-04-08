from network import Network
from util import message
from exceptions import *

import asyncio


class Client:

    def __init__(self, token: str, timeout: float = 20) -> None:
        self.loop = asyncio.get_event_loop()
        self.network = Network(token=token, timeout=timeout)

        if not token:
            raise TokenNotInvalid('`token` did\'t passed')

    async def request(self, method: str, data: dict = None, files: dict = None) -> dict:
        try:
            return await self.network.connect(method=method, data=data, files=files)
        except Exception as err:
            print(__file__, err, __file__)

    async def on_message(self):
        '''Use this method to receive updates
        Example:
            from bale import Client
            import asyncio

            client = Client('token', timeout=10)
            async def main():
                async for update in client.on_message():
                    print(update.text)
                    await update.reply('hello __from__ **balepy**')

            asyncio.run(main())
        '''
        payload: dict = {
            'offset': -1, 'limit': 100
        }
        while True:
            update = await self.request('getupdates', payload)
            payload['offset'] = 1
            if update != None and update != []:
                break

        payload['offset'], payload['limit'] = update[len(update)-1]['update_id'], 1
        while True:
            responce = await self.request('getupdates', payload)
            if responce != None and responce != []:
                payload['offset'] += 1
                final_responce = message(responce[0], self.network.token, self.network.timeout)
                if final_responce.chat_type in filters:
                    return final_responce

    async def send_message(
            self,
            chat_id: str | int,
            text: str,
            reply_markup: int = None,
            reply_to_message_id: int = None
    ) -> dict:
        payload: dict = {
            'chat_id': chat_id,
            'text': text,
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to_message_id
        }
        return await self.request('sendmessage', data=payload)
