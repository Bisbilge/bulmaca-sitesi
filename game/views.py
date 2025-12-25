import json
import os
from django.shortcuts import render
from django.conf import settings
from pathlib import Path

# Data klasörünün tam yolu
DATA_DIR = Path(settings.BASE_DIR) / 'data'

def home(request):
    """Klasördeki tüm JSON dosyalarını bulup listeler."""
    puzzles = []
    
    if DATA_DIR.exists():
        for filename in os.listdir(DATA_DIR):
            if filename.endswith('.json') and filename != 'bulmaca.json': 
                # Not: 'bulmaca.json' yedek kalabilir, listeye eklemeyelim istersen.
                # Hepsini eklemek istersen "and filename !=..." kısmını sil.
                
                try:
                    with open(DATA_DIR / filename, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        puzzles.append({
                            # Dosya adını ID olarak kullanıyoruz (uzantısız)
                            'id': filename.replace('.json', ''), 
                            'title': data.get('title', 'İsimsiz Bulmaca')
                        })
                except:
                    pass # Hatalı dosyaları görmezden gel

    return render(request, 'game/home.html', {'puzzles': puzzles})

def puzzle_detail(request, slug):
    """Linkten gelen isme (slug) göre dosyayı bulup açar."""
    filename = f"{slug}.json"
    file_path = DATA_DIR / filename
    
    # Dosya varsa oku, yoksa 404 ver
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            puzzle_data = json.load(f)
        
        return render(request, 'game/index.html', {
            'puzzle': puzzle_data
        })
    else:
        return render(request, 'game/404.html')