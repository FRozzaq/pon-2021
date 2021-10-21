from data_peserta import DataPeserta
from kelas_tanding import KelasTanding
import pandas

data_peserta = DataPeserta()


class ChampionshipRekap:
    @staticmethod
    def rekap_tanding_dict(gender):
        kelas = KelasTanding()

        kelas_list = kelas.create_kelas("J")  # create kelas A PA, B PA ... A PI, B PI etc
        jumlah_kelas = kelas.getjumlahkelas("J")
        kelas_tanding = kelas.getkelasraw(jumlah_kelas)
        kelas_pa = kelas_list[0:jumlah_kelas]
        kelas_pi = kelas_list[jumlah_kelas:]

        if gender == "PA":
            return {
                "kelas": kelas_pa,
                "jml_peserta": [len(data_peserta.getplayersinkelas(i, "L")) for i in kelas_tanding],
            }
        elif gender == "PI":
            return {
                "kelas": kelas_pi,
                "jml_peserta": [len(data_peserta.getplayersinkelas(i, "P")) for i in kelas_tanding],
            }

    def jumlah_peserta_tanding_list(self):
        sum_tanding_pa = pandas.DataFrame(self.rekap_tanding_dict("PA"))
        sum_tanding_pi = pandas.DataFrame(self.rekap_tanding_dict("PI"))

        jml_peserta_pa_list = sum_tanding_pa["jml_peserta"].tolist()
        jml_peserta_pi_list = sum_tanding_pi["jml_peserta"].tolist()
        jml_peserta_pa_list.extend(jml_peserta_pi_list)
        return jml_peserta_pa_list

    @staticmethod
    def total_peserta():
        return len(data_peserta.get_data())

    @staticmethod
    def peserta_tunggal():
        return len(data_peserta.getplayersinkelas("TUNGGAL", "L")) + len(
            data_peserta.getplayersinkelas("TUNGGAL", "P"))

    @staticmethod
    def peserta_ganda():
        return len(data_peserta.getplayersinkelas("GANDA", "L")) + len(
            data_peserta.getplayersinkelas("GANDA", "P"))

    @staticmethod
    def peserta_regu():
        return len(data_peserta.getplayersinkelas("REGU", "L")) + len(data_peserta.getplayersinkelas("REGU", "P"))
