import json

TITLE = "Makarna 101"

# Grid Tasarımı
# Dikeyde ana omurga: ESPERANTO
# Yatayda kesişenler: POMO, VARMA, AMIKO, KATO, DOMO
RAW_GRID = """
##ALDENTE#######
#S###R##########
#Ü###İ##########
#Z###Ş########S#
#G#P#T########P#
KELEBEK#######A#
#Ç#S##I##L#BURGU
###T##Y##A####E#
###O##M##Z####T#
######ARRABBİATA
#########N#O##İ#
#######FİYONK###
#########A#C####
###########U####
###########K####
""".strip().split('\n')

CLUES = {
    "across": {
        "1": "Makarnanın çok yumuşamadan, hafif diri kalacak şekilde pişirilmesi (İtalyanca terim).",
        "6": "Ortası büzgülü, papyonu andıran sevimli makarna şekli.",
        "9": "Sosu tutmasıyla bilinen, matkap ucu veya tirbuşon şeklindeki makarna.",
        "10": "İtalyanca kızgın/öfkeli anlamına gelen, bol sarımsaklı ve acı biberli domates sosu.",
        "12": "Genellikle yoğurtla servis edilen, kurdeleye benzeyen makarna çeşidi.",
    },
    "down": {
        "2": "Türk mutfağında ev yapımı, kesme yassı makarna.",
        "3": "Haşlanan makarnanın suyunu dökmek için kullanılan delikli kap.",
        "4": "İtalyan mutfağının en bilinen, uzun ve ince çubuk şeklindeki hamur işi.",
        "5": "Cenova kökenli; fesleğen, çam fıstığı, sarımsak, parmesan ve zeytinyağının dövülmesiyle yapılan yeşil sos.",
        "7": "Bolonez sosun veya klasik öğrenci makarnasının ana protein kaynağı.",
        "8": "Kat kat hamur, kıyma ve beşamel sos ile fırında yapılan meşhur yemek.",
        "11": "Çorbalara ve salatalara çok yakışan, minik yuvarlak taneli makarna.",
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
    file_path = 'data/makarna.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ '{TITLE}' oluşturuldu: {file_path}")
    print("👉 Siteyi güncellemek için: git add . && git commit -m 'Esperanto bulmacasi' && git push")

if __name__ == "__main__":
    create_json()