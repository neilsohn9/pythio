from typing import Optional, Union, BinaryIO
from os.path import isfile

from . import Object


class InputMedia(Object):

    def __init__(
            self,
            type: Optional[str] = None,
            media: Union[str, bytes, BinaryIO] = None,
            caption: Optional[str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.type: str = type
        try:
            if isfile(media):
                media = open(media, 'rb')
        except TypeError:
            pass
        self.media: Union[str, bytes, BinaryIO] = media
        self.caption: str = caption

    @property
    def is_json_serializable(self):
        return isinstance(self.media, str)
