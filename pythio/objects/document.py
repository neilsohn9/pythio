from typing import Optional

from pythio import objects
from . import Object


class Document(Object):

    def __init__(
            self,
            id: Optional[str] = None,
            thumb: 'objects.Photo' = None,
            file_name: Optional[str] = None,
            mime_type: Optional[str] = None,
            size: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.thumb: None = thumb
        self.file_name: str = file_name
        self.mime_type: str = mime_type
        self.size: int = size
