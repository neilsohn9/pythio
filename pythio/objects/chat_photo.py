from typing import Optional

from . import Object


class ChatPhoto(Object):

    def __init__(
            self,
            small_id: Optional[str] = None,
            small_unique_id: Optional[str] = None,
            big_id: Optional[str] = None,
            big_unique_id: Optional[str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.small_id: str = small_id
        self.small_unique_id: str = small_unique_id
        self.big_id: str = big_id
        self.big_unique_id: str = big_unique_id
