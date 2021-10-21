import pandas

from data_peserta import DataPeserta


class Peserta:
    @staticmethod
    def create_peserta(nama, kontingen, gender, birth, kategori):
        data = DataPeserta()
        data_peserta = data.get_data()
        data_peserta_dict = data_peserta.to_dict()
        new_index = len(data_peserta_dict)
        data_peserta_dict["nama"][new_index] = nama
        print(data_peserta_dict["nama"][new_index])
        data_peserta_dict["kontingen"][new_index] = kontingen
        data_peserta_dict["gender"][new_index] = gender
        data_peserta_dict["birth"][new_index] = birth
        data_peserta_dict["kategori"][new_index] = kategori
        new_data = pandas.DataFrame(data_peserta_dict)
        new_data.to_csv("1.csv")
        return new_data

# data = DataPeserta()
# data_peserta = data.get_data()
# data_peserta_dict = data_peserta.to_dict()


peserta = Peserta()
new_data = peserta.create_peserta("test", "test", "test", "test", "test")
print(new_data)
