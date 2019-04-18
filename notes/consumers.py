from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json  # to transform the recieved data from json to array and vice versa

from . import models  # using models to save our data


class NoteConsumer(WebsocketConsumer):  # it extends the WebSocketConsumer class
    def connect(self):
        self.room_group_name = "notes"
        # once a connection is made, we create a room called notes

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name  # we close the room and channel
        )

    def receive(self, text_data):  # what is done when data is received
        text_data_json = json.load(text_data)
        title = text_data_json["title"]
        content = text_data_json["content"]
        id = text_data_json["id"]

        # now use the model to find the note by id, update its content and save it
        note = models.Note.objects.get(pk=id)
        note.title = title
        note.content = content
        note.save()

        # now we sync the data with the channel group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "add_note", "title": title, "content": content, "id": id},
        )
        # above: created a new channel group, we pass in the type, which is a method, as well as title, content and id

        # this method accepts and extracts everything from the event: title, content, id
        def add_note(self, event):
            title = event["title"]
            content = event["content"]
            id = event["id"]
            self.send(  # sends extracted data to listening channel
                text_data=json.dumps({"title": title, "content": content, "id": id})
            )

