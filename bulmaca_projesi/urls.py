from django.contrib import admin
from django.urls import path, include  # <--- include'u ekle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),    # <--- Ana sayfayı game'e yönlendir
]