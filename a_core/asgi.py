"""
ASGI config for a_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

django_asgi_app = get_asgi_application() 
# Create the main Django app that can talk to the web server.

from a_rtchat import routing 
# We imports routing after calling get_asgi_application() to prevent circular imports : If you import your app’s routing before Django finishes loading, it may try to use models or URL configs before Django has set them up → boom circular import or initialization error.

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
        ),
        
    }
) 
# Routes requests based on connection type (HTTP → Django, WebSocket → Channels/WebSocket handlers).