from typing import Optional

from pythio import objects
from . import Object


class EditedMessage(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            author: 'objects.User' = None,
            date: 'objects.Date' = None,
            chat: 'objects.Chat' = None,
            edit_date: 'objects.Date' = None,
            text: Optional[str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.author: 'objects.User' = author
        self.date: 'objects.Date' = date
        self.chat: 'objects.Chat' = chat
        self.edit_date: 'objects.Date' = edit_date
        self.text: str = text
