from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import PizzaLover, Message


def getPizzaLoversRank():
    pizzaLovers = PizzaLover.objects.order_by('-numberOfVotes')[:10]
    response = [['UserName', 'NumberOfVotes']]
    response += [[a.userID.username, a.numberOfVotes] for a in pizzaLovers]
    return response


def message_to_json(message):
    return {
        'id': str(message.id),
        'content': message.content
    }

def notifyUsers():
    resp = getPizzaLoversRank()

    message = Message.objects.create(content=str(resp))
    layer = get_channel_layer()

    content = {
        'command': 'new_message',
        'message': message_to_json(message)
    }
    async_to_sync(layer.group_send)(
        'events',
        {
            'type': 'event_message',
            'message': content
        }
    )
