from typing import Optional, List

from pythio import objects
from . import Object


class Video(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            duration: Optional[int] = None,
            thumb: List['objects.Photo'] = None,
            mime_type: Optional[str] = None,
            size: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.thumb: List['objects.Photo'] = thumb
        self.mime_type: str = mime_type
        self.size: int = size
