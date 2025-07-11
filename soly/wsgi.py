"""
soly/wsgi.py

WSGI config for the Soly project.
This file sets up the WSGI application, which is used for handling synchronous HTTP requests.
It exposes the WSGI callable as a module-level variable named `application`.
For more information, see Django's WSGI deployment documentation.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soly.settings')

# The WSGI application instance used by WSGI servers
application = get_wsgi_application()

# This file is essential for deploying Django with traditional synchronous web servers (e.g., Gunicorn, uWSGI).
# It ensures the project can handle standard HTTP requests and serve web pages or APIs.
