# soal no.2

def duplikat (buah):
    hasil = []
    for i in buah:
        hasil.append(i)
        hasil.append(i)
    return hasil
print(duplikat(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))
