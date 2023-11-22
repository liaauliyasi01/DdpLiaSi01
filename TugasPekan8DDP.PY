#soal no.1

def say(nama,alamat,gender,umur,hobi):
    print(nama)
    print(alamat)
    print(gender)
    print(umur)
    print(hobi)
    say("Lia Auliya,Jakarta Selatan,Perempuan,20 Tahun,Menulis,Membaca,Olahraga")

#soal no.2

def kelulusan(nilai):
     if nilai < 60:
          return "Gagal"
     elif nilai >= 61 and nilai <= 70:
          return "Baik"
     elif nilai >= 71 and nilai <= 80:
          return "Sangat Baik"
     elif nilai >= 81 and nilai <= 100:
          return "Istimewa"
     else:
          return "Nilai tidak valid"
     
     print(kelulusan(90))

#soal no.3

def ganjil(a):
     if a > 1:
          for i in range(3, a+1, 2):
               print(i)
     else:
          print(1)
     ganjil(100)
          
    

