import json
import os
from django.shortcuts import render
from django.conf import settings

def index(request):
    # Dosya yolunu oluştur
    json_path = os.path.join(settings.BASE_DIR, 'data', 'bulmaca.json')
    
    # Dosyayı aç ve oku
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        # Dosya okunamazsa hata vermesin, boş veri göndersin (Debug için)
        print(f"HATA: JSON okunamadı! {e}")
        puzzle_data = {}

    # HTML'e gönder
    return render(request, 'game/index.html', {
        'puzzle': puzzle_data
    })