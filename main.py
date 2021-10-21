from data_peserta import DataPeserta
from championship_rekap import ChampionshipRekap
from partai import Partai

champ_rekap = ChampionshipRekap()
data_peserta = DataPeserta()
partai = Partai()

rekap_tanding_df = partai.rekap_tanding_df()
total_peserta = champ_rekap.total_peserta()
jml_peserta_tunggal = champ_rekap.peserta_tunggal()
jml_peserta_ganda = champ_rekap.peserta_ganda()
jml_peserta_regu = champ_rekap.peserta_regu()
jml_peserta_tanding = rekap_tanding_df['jml_peserta'].sum()

total_partai_tanding = rekap_tanding_df['jml_partai'].sum()
total_partai_tunggal = jml_peserta_tunggal + 12
total_partai_ganda = int(jml_peserta_ganda / 2 + 6)
total_partai_regu = int(jml_peserta_regu / 3 + 6)

asumsi_satu_partai = 15  # minutes

time_needed_tanding = int(jml_peserta_tanding * asumsi_satu_partai / 60 / 8)

print(rekap_tanding_df)
print(f"total peserta: {total_peserta} org")
print(f"jumlah peserta tanding: {jml_peserta_tanding} org")
print(f"jumlah peserta tunggal: {jml_peserta_tunggal} org")
print(f"jumlah peserta ganda: {jml_peserta_ganda} org / {int(jml_peserta_ganda/2)} tim")
print(f"jumlah peserta regu: {jml_peserta_regu} org / {int(jml_peserta_regu/3)} tim")

print(f"jumlah partai tanding: {total_partai_tanding}")
print(f"jumlah partai tunggal: {jml_peserta_tunggal}")
print(f"jumlah partai ganda: {total_partai_ganda}")
print(f"jumlah partai regu: {total_partai_regu}")

print(f"waktu yg dibutuhkan: {time_needed_tanding} hari")

