from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ana sayfa: Tüm bulmacaların listesi
    path('', views.home, name='home'),
    
    # YENİ EKLENEN: Sudoku sayfası
    path('sudoku/', views.sudoku_view, name='sudoku'),
    
    # Detay sayfası: Seçilen klasik bulmacayı açar (Örn: /coz/hafta-1/)
    path('coz/<str:slug>/', views.puzzle_detail, name='puzzle_detail'),
]