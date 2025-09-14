import pandas as pd


# essayons de  charger ldes données pour les municipales 2020
municipales_2020 = dict()

for i in range(1,20):
    numero_arrandissement=f"{i:02}"
    nom_df=f"arrandissement_{numero_arrandissement}"
    nom_fichier=f"./data/municipales_2020/ddct_berp_municipales_2020_tour1_ardt_{numero_arrandissement}_20200315.csv"
    municipales_2020[nom_df] = pd.read_csv(
        nom_fichier,
    )
