from typing import Optional
from . import Object


class Animation(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            name: Optional[str] = None,
            size: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            duration: Optional[int] = None,
            mime_type: Optional[str] = None,
            unique_id: Optional[str] = None,
            **kwargs
    ):
        self.id: str = id
        self.name: str = name
        self.size: int = size
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.mime_type: str = mime_type
        self.unique_id: str = unique_id
        super().__init__(**kwargs)
