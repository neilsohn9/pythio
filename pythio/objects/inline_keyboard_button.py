from typing import Optional

from . import Object


class InlineKeyboardButton(Object):

    def __init__(
            self,
            text: Optional[str] = None,
            callback_data: Optional[str] = None,
            url: Optional[str] = None,
            switch_inline_query: Optional[str] = None,
            switch_inline_query_current_chat: Optional[str] = None,
            # pay: Optional[bool] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.callback_data: str = callback_data
        self.url: str = url
        self.switch_inline_query: str = switch_inline_query
        self.switch_inline_query_current_chat: str = switch_inline_query_current_chat
        self.pay: bool = pay
