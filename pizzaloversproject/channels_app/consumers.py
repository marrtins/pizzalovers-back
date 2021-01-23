import json

from channels.generic.websocket import WebsocketConsumer
from pizzaloversproject.back.models import User
from pizzaloversproject.back.models import Message
from asgiref.sync import async_to_sync
from pizzaloversproject.back.service import getPizzaLoversRank


class EventConsumer(WebsocketConsumer):

    def init_connection(self, data):
        content = {
            'command': 'init_connection',
            'content': getPizzaLoversRank()
        }
        self.send_message(content)

    commands = {
        'init_connection': init_connection,
    }

    def connect(self):
        self.room_name = 'room'
        self.room_group_name = 'events'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # leave group room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def event_message(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
