from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from authentication.views import home, login_page, register_page, dashboard, logout_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Define paths for different parts of your application
    path('', home, name="home"),  # Root URL mapped to the home view
    path('home/', home, name="recipes"),  # Additional route for the home page
    path('admin/', admin.site.urls),  # Admin interface
    path('login/', login_page, name='login_page'),  # Login page
    path('register/', register_page, name='register'),  # Registration page
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard page (protected)
    path('logout/', logout_view, name='logout'),  # Logout page
]

# Add media and static files handling when in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files through staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
