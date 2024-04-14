from typing import Optional

from . import Object


class Voice(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            duration: Optional[int] = None,
            mime_type: Optional[str] = None,
            size: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.duration: int = duration
        self.mime_type: str = mime_type
        self.size: int = size
