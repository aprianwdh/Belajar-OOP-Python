class Anime:
    #variabel class
    jumlah = 0

    def __init__(self,NamaAnime,Genre,Episode): # Constructor init
        self.nama_anime = NamaAnime
        self.genre_anime = Genre
        self.episode_anime = Episode
        Anime.jumlah += 1
        print(f"Membuat Object Dengan Nama {NamaAnime}")


anime1 = Anime("Hyouka","Slice Of Life",12)
print(Anime.jumlah)
anime2 = Anime("AOT","Action",24)
print(Anime.jumlah)

