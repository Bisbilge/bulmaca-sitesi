# game/views.py - SON VE DOĞRU HALİ
import json
import os
from django.shortcuts import render
from django.conf import settings

def index(request):
    # Dosya yolunu oluştur
    json_path = os.path.join(settings.BASE_DIR, 'data', 'bulmaca.json')
    
    # Dosyayı aç ve oku
    with open(json_path, 'r', encoding='utf-8') as f:
        puzzle_data = json.load(f)

    return render(request, 'game/index.html', {
        'puzzle': puzzle_data,
        'puzzle_json': json.dumps(puzzle_data)
    })