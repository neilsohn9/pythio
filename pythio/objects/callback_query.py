from typing import Optional

from pythio import objects
from . import Object


class CallbackQuery(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            author: "objects.User" = None,
            message: "objects.Message" = None,
            inline_message_id: Optional[str] = None,
            chat_instance: Optional[str] = None,
            data: Optional[str] = None,
            game_short_name: Optional[str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.author: "objects.User" = author
        self.message: "objects.Message" = message
        self.inline_message_id: str = inline_message_id
        self.chat_instance: str = chat_instance
        self.data: str = data
        self.game_short_name: str = game_short_name

    async def answer(self, text: str, reply_markup: Optional[int] = None, client=None):
        client = client or self.client
        return await client.send_message(self.message.chat.id, text, reply_markup)
