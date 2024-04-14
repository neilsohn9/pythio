from typing import Optional

from pythio import objects
from . import Object


class Entity(Object):

    def __init__(
            self,
            type: Optional[str] = None,
            offset: Optional[int] = None,
            length: Optional[int] = None,
            url: Optional[str] = None,
            user: 'objects.User' = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.type: str = type
        self.offset: int = offset
        self.length: int = length
        self.url: str = url
        self.user: 'objects.User' = user
