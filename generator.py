import json

TITLE = "Twitter Time 2025"

# Resimdeki yapıya birebir uygun Grid Haritası
# Boşluklar # ile gösterilir.
# Harflerin yerleşimi senin attığın görsele göre hesaplandı.

RAW_GRID = """
########T###############
#####S##İ###############
#####O##R###############
#####SUBAR##############
#####Y##M###############
##K##A##İ#######K#######
##A##L##S#K#####A#######
##D##Ç##U#I#####MAHMUT##
##I##Ü####Z#####E#######
HAKMAR#YAPI#####R#G#M###
##Ö##Ü####L#BEYZADOĞAN##
##Y##M####A#Ö#####Y#R###
####SERGENYALÇIN####U###
####E#######Ü####GÜLLÜ##
GÜZELGÖTLÜM#K#S#########
####İ#######B#T##D######
#ÖTENAZİ###HASANPERÇİN##
#Z##S#######Ş#N##V######
#G##U#######I#L##L#M####
#E###########BERKEMAL###
##############Y##T#N####
###################İ####
###################F####
###################EVRİM
###################S####
###################T####
""".strip().split('\n')

CLUES = {
    "across": {
        "3": "Bir dağ",
        "6": "Tabela",
        "7": "... Tanal",
        "8": "Bimden çıktıktan sonra girmek için izin almamız gerek yer",
        "9": "Fenerbahçenin şampiyon olamama sebebi",
        "10": "Yahudi yalakası",
        "11": "Polis yemeği",
        "12": "Dövme sevmeyen twitter kullanıcısı",
        "13": "Maçı kazanamaz",
        "14": "Bu sene kaybettiğimiz kadın sanatçı",
        "15": "Bir iltifat",
        "18": "Cevahirin istediği hak",
        "19": "Pembe tayt",
        "21": "Asayiş",
        "22": "Çocukları döven kadın oyuncunun ismi",


    },
    "down": {
        "1": "Üzerine yazı yazılan tatlı",
        "2": "Zeliha Bürtek",
        "4": "... Boğası",
        "5": "...mı çok seviyorum",
        "6": "Tabela",
        "12": "Hapse girerek hepimizi sevindiren kişi",
        "13": "2 fenocun uğruna kavge ettiği kız",
        "16": "Babamın tarlaya gitmek için aldığı termosun markası",
        "17": "Öcalan'ın meclise gelmesini isteyen siyasetçi",
        "20": "Yılın grubu",

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