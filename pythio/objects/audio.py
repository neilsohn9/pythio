from typing import Optional
from . import Object


class Audio(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            title: Optional[str] = None,
            duration: Optional[int] = None,
            performer: Optional[str] = None,
            mime_type: Optional[str] = None,
            size: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.title: str = title
        self.duration: int = duration
        self.performer: str = performer
        self.mime_type: str = mime_type
        self.size: int = size
