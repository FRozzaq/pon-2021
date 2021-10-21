import pandas

NAMA_FILE = "DAFTAR PESERTA PON 2021.csv"


class DataPeserta:
    @staticmethod
    def get_data():
        return pandas.read_csv(NAMA_FILE)

    def getplayersinkelas(self, kategori, gender):
        data = self.get_data()
        kelas = data[data.kategori == kategori]
        return kelas[kelas.gender == gender]
