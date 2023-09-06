print("kısaltma veya onaylama olan ingilizce sözcükler")


meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "yüksek seslen gülmek",
            "SHEESH": "inançsızlık",
            "CREEPY": "korkutucu"
            }
            
            
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Bu kelime sözlükte bulunamadı bro")
