from typing import Optional

from . import Object


class ReplyKeyboardButton(Object):

    def __init__(
            self,
            text: Optional[str] = None,
            request_contact: Optional[bool] = None,
            request_location: Optional[bool] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.request_contact: bool = request_contact
        self.request_location: bool = request_location
