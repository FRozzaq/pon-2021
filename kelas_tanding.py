import string


class KelasTanding:
    @staticmethod
    def getjumlahkelas(kelas_tertinggi):
        alphabet = list(string.ascii_uppercase)
        for i in range(len(alphabet)):
            if alphabet[i] == kelas_tertinggi:
                return i + 1

    @staticmethod
    def getkelasraw(kelas_range):
        return list(string.ascii_uppercase)[0:kelas_range]  # kelas A,B,C etc

    def create_kelas(self, kelas_tertinggi):
        kelas_range = self.getjumlahkelas(kelas_tertinggi)
        kelas_tanding = self.getkelasraw(kelas_range)
        kelas_list = [kelas_tanding[i] + " PA" for i in range(10)]
        for i in range(10):
            kelas_list.append(kelas_tanding[i] + " PI")  # kelas A PA, B PA ... A PI, B PI etc
        return kelas_list
