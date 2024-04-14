from typing import Optional

from . import Object


class WebhookInfo(Object):

    def __init__(
            self,
            url: Optional[str],
            has_custom_certificate: Optional[bool],
            pending_update_count: Optional[int],
            **kwargs
    ):
        super().__init__(**kwargs)
        self.url: str = url
        self.has_custom_certificate: bool = has_custom_certificate
        self.pending_update_count: int = pending_update_count
