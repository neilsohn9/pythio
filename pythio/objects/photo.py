from typing import Optional

from . import Object


class Photo(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            size: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.size: int = size
