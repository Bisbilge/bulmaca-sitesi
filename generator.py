import json

TITLE = "Haftalık Bulmaca #5: Esperanto 101"

# Grid Tasarımı
# Dikeyde ana omurga: ESPERANTO
# Yatayda kesişenler: POMO, VARMA, AMIKO, KATO, DOMO
RAW_GRID = """
###E#######
###S#######
#POMO######
###E#######
#VARMA#####
###A#######
AMIKO######
###N#######
#KATO######
DOMO#######
""".strip().split('\n')

CLUES = {
    "across": {
        "1": "Elma",
        "2": "Sıcak (Hava durumu vb.)",
        "3": "Arkadaş, dost",
        "4": "Kedi",
        "5": "Ev"
    },
    "down": {
        "1": "Umut eden kişi (veya şu an çözdüğün dilin adı)"
    }
}

def create_json():
    grid_array = []
    for line in RAW_GRID:
        # Satır başı/sonu boşluklarını temizle
        cleaned_line = line.strip() 
        row = list(cleaned_line.upper()) 
        grid_array.append(row)

    # En geniş satırı bul
    width = max(len(row) for row in grid_array)
    height = len(grid_array)

    # Eksik kareleri # ile doldur
    for row in grid_array:
        while len(row) < width:
            row.append('#')

    final_data = {
        "title": TITLE,
        "width": width,
        "height": height,
        "grid": grid_array,
        "clues": CLUES
    }

    # Dosya ismini 'esperanto.json' yapıyoruz
    file_path = 'data/esperanto.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ '{TITLE}' oluşturuldu: {file_path}")
    print("👉 Siteyi güncellemek için: git add . && git commit -m 'Esperanto bulmacasi' && git push")

if __name__ == "__main__":
    create_json()