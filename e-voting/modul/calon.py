listCalon = []

def tambah_calon():
    idCalon = input("Masukan ID Calon: ")
    if any (C['id']) == idCalon for C in lisCalon):
        print("ID sudah terdaftar.")
        return
    namaCalon = input("Masukan Nama Calon: ")
    vimiCalon = input("Masukan Nama Visi Misi: ")

    listCalon.append({"id": idCalon, "Nama": namaCalon, "Visi": vimiCalon, "Jumlah suara:" 0})