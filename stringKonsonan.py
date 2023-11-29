# soal no.4
def filter_konsonan(string_input):
    konsonan = ""
    for char in string_input:
        if char.isalpha() and char.lower() not in 'aeiou':
            konsonan += char
    return konsonan

# contoh penggunaan
input_string = "Nurul Fikri"
hasil = filter_konsonan(input_string)
print("Hasilnya:", hasil)