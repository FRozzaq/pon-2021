from championship_rekap import ChampionshipRekap
from kelas_tanding import KelasTanding
import pandas


class Partai:
    @staticmethod
    def rekap_tanding_df():
        championship_rekap = ChampionshipRekap()

        kelas_tanding = KelasTanding()
        kelas_list = kelas_tanding.create_kelas("J")  # create kelas A PA, B PA ... A PI, B PI etc

        jml_peserta_list = championship_rekap.jumlah_peserta_tanding_list()

        jml_partai_list = []
        final_list = []
        semi_list = []
        quarter_list = []
        one_eight_list = []
        one_sixteen_list = []

        for i in range(len(jml_peserta_list)):
            final = 1
            semi = 2
            quarter = 4
            one_eight = 8
            one_sixteen = 16
            partai = jml_peserta_list[i] - 1
            if partai > 0:
                jml_partai_list.append(partai)
                if partai - final - semi - quarter - one_eight > 0:  # jika jumlah partai > 15
                    one_sixteen = partai - final - semi - quarter - one_eight
                elif partai - final - semi - quarter > 0:  # jika jumlah partai > 7
                    one_eight = partai - final - semi - quarter
                    one_sixteen = 0
                elif partai - final - semi > 0:  # jika jumlah partai > 3
                    quarter = partai - final - semi
                    one_eight = 0
                    one_sixteen = 0
                elif partai - final >= 1:
                    semi = partai - final
                    quarter = 0
                    one_eight = 0
                    one_sixteen = 0
                elif partai > 0:
                    semi = 0
                    quarter = 0
                    one_eight = 0
                    one_sixteen = 0
            else:
                partai = 0
                final = 0
                semi = 0
                quarter = 0
                one_eight = 0
                one_sixteen = 0
                jml_partai_list.append(partai)

            final_list.append(final)
            semi_list.append(semi)
            quarter_list.append(quarter)
            one_eight_list.append(one_eight)
            one_sixteen_list.append(one_sixteen)

        recap_player_dict = {
            "kelas": kelas_list,
            "jml_peserta": jml_peserta_list,
            "jml_partai": jml_partai_list,
            "one_sixteen": one_sixteen_list,
            "one_eight": one_eight_list,
            "quarter": quarter_list,
            "semi": semi_list,
            "final": final_list,
        }

        return pandas.DataFrame(recap_player_dict)
