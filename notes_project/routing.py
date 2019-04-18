from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notes.routing  # here we import our routing.py module from notes for use below


application = ProtocolTypeRouter(
    {"websocket": AuthMiddlewareStack(URLRouter(notes.routing.websocket_urlpatterns))}
)

