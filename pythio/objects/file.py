from typing import Optional

from . import Object


class File(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            size: Optional[int] = None,
            path: Optional[str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.size: int = size
        self.path: str = path
