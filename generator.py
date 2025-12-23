import json

TITLE = "TWİTTER TİME 2025"

# Resimdeki yapıya birebir uygun Grid Haritası
# Boşluklar # ile gösterilir.
# Harflerin yerleşimi senin attığın görsele göre hesaplandı.

RAW_GRID = """
###ÖZGE#######
#H###Ü##K#####
#A#KIZILAY####
#K#A#E##M#####
#M#D#L##E#####
YAPI#G##R#####
#R#K#Ö#SANDVİÇ
###Ö#T#E######
###Y#L#L######
#####Ü#İ######
#####MANIFEST#
#######S######
###MAHMUT#####
""".strip().split('\n')

CLUES = {
    "across": {
        "1": "Eren’in eski nişanlısı",
        "5": "Tabela",
        "6": "Fenerbahçenin şampiyon olamama sebebi",
        "7": "Polis yemeği",
        "8": "Yılın Grubu",
        "9": "... Tanal"
    },
    "down": {
        "2": "Bir iltifat (Saadettin Saran)",
        "3": "Bimden çıktıktan sonra girmek için izin almamız gerek yer",
        "4": "...mi cok seviyorum",
        "5": "... Boğası",
        "7": "2 Fenocun uğruna kavga ettiği kız"
    }
}

def create_json():
    grid_array = []
    
    # Grid'i oluştur
    for line in RAW_GRID:
        # Satırın başındaki ve sonundaki görünmez boşlukları temizle ama içerdekileri tut
        # Python'da string işlemleri bazen karmaşık olabilir, o yüzden garantici olalım:
        cleaned_line = line.strip() 
        # Harfleri ayır ve listeye ekle
        row = list(cleaned_line.upper()) 
        grid_array.append(row)

    # En geniş satırı bul (Gridin genişliği o olacak)
    width = max(len(row) for row in grid_array)
    height = len(grid_array)

    # Kısa kalan satırları '#' ile doldur (Kare olması için)
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

    # Dosyaya kaydet
    file_path = 'data/bulmaca.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Başarılı! {width}x{height} boyutunda JSON oluşturuldu.")
    print("👉 Şimdi terminalden: git add . && git commit -m 'Yeni bulmaca' && git push yapabilirsin.")

if __name__ == "__main__":
    create_json()