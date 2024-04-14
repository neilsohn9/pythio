from typing import Optional, List, Union, BinaryIO

from pythio import objects
from . import Object


class Message(Object):

    def __init__(
            self,
            id: Optional[int] = None,
            author: "objects.User" = None,
            date: "objects.Date" = None,
            chat: "objects.Chat" = None,
            forward_from: "objects.User" = None,
            forward_from_chat: "objects.Chat" = None,
            forward_from_message_id: Optional[int] = None,
            forward_date: "objects.Date" = None,
            reply_to_message: "objects.Message" = None,
            edit_date: "objects.Date" = None,
            text: Optional[str] = None,
            animation: "objects.Animation" = None,
            entities: List["objects.Entity"] = None,
            caption_entities: List["objects.Entity"] = None,
            audio: "objects.Audio" = None,
            document: "objects.Document" = None,
            photo: List["objects.Photo"] = None,
            video: "objects.Video" = None,
            voice: "objects.Voice" = None,
            caption: Optional[str] = None,
            contact: "objects.Contact" = None,
            location: "objects.Location" = None,
            new_chat_members: List["objects.User"] = None,
            left_chat_member: "objects.User" = None,
            new_chat_title: Optional[str] = None,
            new_chat_photo: List["objects.Photo"] = None,
            delete_chat_photo: Optional[bool] = None,
            group_chat_created: Optional[bool] = None,
            supergroup_chat_created: Optional[bool] = None,
            channel_chat_created: Optional[bool] = None,
            pinned_message: None = None,
            invoice: "objects.Invoice" = None,
            successful_payment: "objects.SuccessfulPayment" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.author: "objects.User" = author
        self.date: "objects.Date" = date
        self.chat: "objects.Chat" = chat
        self.forward_from: "objects.User" = forward_from
        self.forward_from_chat: "objects.Chat" = forward_from_chat
        self.forward_from_message_id: int = forward_from_message_id
        self.forward_date: "objects.Date" = forward_date
        self.reply_to_message: "objects.Message" = reply_to_message
        self.edit_date: "objects.Date" = edit_date
        self.text: Optional[str] = text
        self.animation: "objects.Animation" = animation
        self.entities: List["objects.Entity"] = entities
        self.caption_entities: List["objects.Entity"] = caption_entities
        self.audio: "objects.Audio" = audio
        self.document: "objects.Document" = document
        self.photo: List["objects.Photo"] = photo
        self.video: "objects.Video" = video
        self.voice: "objects.Voice" = voice
        self.caption: Optional[str] = caption
        self.contact: "objects.Contact" = contact
        self.location: "objects.Location" = location
        self.new_chat_members: List["objects.User"] = new_chat_members
        self.left_chat_member: "objects.User" = left_chat_member
        self.new_chat_title: Optional[str] = new_chat_title
        self.new_chat_photo: List["objects.Photo"] = new_chat_photo
        self.delete_chat_photo: Optional[bool] = delete_chat_photo
        self.group_chat_created: Optional[bool] = group_chat_created
        self.supergroup_chat_created: Optional[bool] = supergroup_chat_created
        self.channel_chat_created: Optional[bool] = channel_chat_created
        self.pinned_message: None = pinned_message
        self.invoice: "objects.Invoice" = invoice
        self.successful_payment: "objects.SuccessfulPayment" = successful_payment

    async def reply_animation(
            self,
            animation: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            caption: Optional[int] = None,
            client=None
    ):
        client = client or self.client
        return await client.send_animation(
            self.chat.id, animation, duration, width, height, caption, self.id
        )

    async def reply_audio(
            self,
            audio: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: Optional[str] = None,
            duration: Optional[int] = None,
            title: Optional[str] = None,
            client=None
    ):
        client = client or self.client
        return await client.send_audio(self.chat.id, audio, caption, duration, title, self.id)

    async def reply_contact(
            self,
            phone_number: Optional[str],
            first_name: Optional[str],
            last_name: Optional[str] = None,
            client=None
    ):
        client = client or self.client
        return await client.send_contact(self.chat.id, phone_number, first_name, last_name, self.id)

    async def reply_document(
            self,
            document: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: Optional[str] = None,
            reply_markup: "objects.ReplyMarkup" = None,
            client=None
    ):
        client = client or self.client
        return await client.send_document(self.chat.id, document, caption, reply_markup, self.id)

    async def reply_location(self, latitude: int, longitude: int, client=None):
        client = client or self.client
        return await client.send_location(self.chat.id, longitude, latitude, self.id)

    async def reply_media_group(self, media: List["objects.InputMedia"], client=None):
        client = client or self.client
        return await client.send_media_group(self.chat.id, media)

    async def reply_photo(
            self,
            photo: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: Optional[str] = None,
            reply_markup: "objects.ReplyMarkup" = None,
            client=None
    ):
        client = client or self.client
        return await client.send_photo(self.chat.id, photo, caption, reply_markup, self.id)

    async def reply_video(
            self,
            video: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            caption: Optional[str] = None,
            client=None
    ):
        client = client or self.client
        return await client.send_video(self.chat.id, video, duration, width, height, caption)

    async def reply_voice(
            self,
            voice: Union[str, bytes, BinaryIO, "objects.InputMedia"],
            caption: Optional[str] = None,
            duration: Optional[int] = None,
            client=None
    ):
        client = client or self.client
        return await client.send_voice(self.chat.id, voice, caption, duration, self.id)

    async def reply(self, text: str, reply_markup: "objects.ReplyMarkup" = None, client=None):
        client = client or self.client
        return await client.send_message(self.chat.id, text, reply_markup, self.id)

    async def edit_text(self, text: str, reply_markup: Optional[int] = None, client=None):
        client = client or self.client
        return await client.edit_message_text(self.chat.id, self.id, text, reply_markup)

    async def delete(self, client=None):
        client = client or self.client
        return await client.delete_message(self.chat.id, self.id)

    async def forward(self, chat_id: int, client=None):
        client = client or self.client
        return await client.forward_message(chat_id, self.chat.id, self.id)

    async def copy(
            self,
            chat_id: int,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: Optional[int] =None,
            client=None
    ):
        client = client or self.client
        if self.text:
            return await client.send_message(chat_id, self.text, reply_markup, reply_to_message_id)

        elif self.photo and len(self.photo) == 1:
            return await client.send_photo(
                chat_id, self.photo[0].id,self.caption, reply_markup, reply_to_message_id
            )
        elif self.photo:
            from . import InputMediaPhoto
            return await client.send_media_group(
                chat_id, [InputMediaPhoto(photo.id) for photo in self.photo]
            )
        elif self.audio:
            return await client.send_audio(
                chat_id, self.audio.id, caption=self.caption, reply_to_message_id=reply_to_message_id
            )
        elif self.video:
            return await client.send_video(
                chat_id, self.video.id, caption=self.caption, reply_to_message_id=reply_to_message_id
            )
        elif self.animation:
            return await client.send_animation(
                chat_id, self.animation.id, caption=self.caption, reply_to_message_id=reply_to_message_id
            )
        elif self.contact:
            return await client.send_contact(
                chat_id,
                self.contact.phone_number,
                self.contact.first_name,
                self.contact.last_name,
                reply_to_message_id=reply_to_message_id
            )
        elif self.location:
            return await client.send_location(
                chat_id,
                self.location.longitude,
                self.location.latitude,
                reply_to_message_id=reply_to_message_id
            )
        elif self.voice:
            return await client.send_voice(
                chat_id,
                self.voice.id,
                caption=self.caption,
                reply_to_message_id=reply_to_message_id
            )
        elif self.document:
            return await client.send_document(
                chat_id, self.document.id, self.caption, reply_markup, reply_to_message_id
            )
        raise TypeError('Message is not copyable')
