from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ana sayfa: Liste görünümü
    path('', views.home, name='home'),
    
    # Detay sayfası: /coz/hafta-1/ gibi
    path('coz/<str:slug>/', views.puzzle_detail, name='puzzle_detail'),
]