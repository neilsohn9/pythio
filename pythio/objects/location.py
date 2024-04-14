from typing import Optional

from . import Object


class Location(Object):

    def __init__(
            self,
            longitude: Optional[int] = None,
            latitude: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.longitude: int = longitude
        self.latitude: int = latitude
