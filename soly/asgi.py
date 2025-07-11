"""
soly/asgi.py

ASGI config for the Soly project.
This file sets up the ASGI application, which is used for handling asynchronous requests (WebSockets, HTTP/2, etc.).
It exposes the ASGI callable as a module-level variable named `application`.
For more information, see Django's ASGI deployment documentation.
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soly.settings')

# The ASGI application instance used by ASGI servers
application = get_asgi_application()

# This file is essential for deploying Django with asynchronous capabilities (e.g., live chat, streaming).
# It ensures the project can handle real-time features and scalable connections.
