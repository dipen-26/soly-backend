"""
soly/urls.py

URL configuration for the Soly project.
This file maps URL patterns to views and includes routes for all major apps and admin functionality.
It organizes the API endpoints and ensures requests are routed to the correct logic.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('api/accounts/', include('accounts.urls')),  # User management endpoints
    path('api/streams/', include('streams.urls')),  # Live streaming endpoints
    path('api/analytics/', include('analytics.urls')),  # Analytics endpoints
    path('api/chat/', include('chat.urls')),  # Real-time chat endpoints
    path('api/content/', include('content.urls')),  # VODs, highlights, playlists endpoints
    path('api/notifications/', include('notifications.urls')),  # Notifications endpoints
    path('api/monetization/', include('monetization.urls')),  # Monetization endpoints
    # Knox token authentication endpoints
    path('api/auth/', include('knox.urls')),
    # Optionally, add session authentication endpoints if needed
]

# This file is the central routing hub for the backend, connecting all features and APIs.
# Each path ensures modularity and separation of concerns for maintainable development.
