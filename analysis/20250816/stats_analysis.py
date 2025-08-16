import pandas as pd
from scipy import stats
from os.path import join
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from scipy.stats import tukey_hsd


from mylib import genomes
from mylib import create_gnome_mean_df
from mylib import compute_t_test
from mylib import create_gnome_count_df

def attic():
     l = list()
     tl = list()
     for ppn in population_names:
          l.append(f"group_{ppn}=mdf['{ppn}']")
          tl.append(f"group_{ppn}")

     st = "\n".join(l)
     tukey_arg = ",".join(tl)

     print(st)
     print(tukey_arg)
     # import matplotlib.pyplot as plt
     # fig, ax = plt.subplots(1, 1)
     # ax.boxplot(mdf[population_names])
     # ax.set_xticklabels(population_names) 
     # ax.set_ylabel("mean") 
     # plt.show()


     population_name_1 = "GBR"
     population_name_2 = "ESN"

     compute_t_test(mdf=mdf,population_name_1=population_name_1,population_name_2=population_name_2)
     
     # population_name_2 = "ASW"
     # population_name_1 = "GBR"
     # population_name_2 = "ASW"
     # t_statistic, p_value = stats.ttest_ind(mdf[population_name_1], mdf[population_name_2], equal_var=True)
     # print(f"\nTwo-Sample Independent T-Test for {population_name_1} and {population_name_2}:")
     # print(f"T-statistic: {t_statistic:.4f}")
     # print(f"P-value: {p_value:.4f}")

if __name__ == "__main__":
     root_dir = join(Path.home(),"cp_als")
     # outputfile= join(root_dir,"analysis/20250816/mean_variant_count_all_populations.csv")
     # mdf = create_gnome_mean_df(root_dir=root_dir,genomes=genomes,outputfile=outputfile)
     outputfile= join(root_dir,"analysis/20250816/variant_count_all_populations.csv")
     mdf = create_gnome_count_df(root_dir=root_dir,genomes=genomes,outputfile=outputfile)
     
     population_names = list(mdf.columns)

     group_ACB=mdf['ACB']
     group_ASW=mdf['ASW']
     group_BEB=mdf['BEB']
     group_CDX=mdf['CDX']
     group_CHB=mdf['CHB']
     group_CHS=mdf['CHS']
     group_CLM=mdf['CLM']
     group_ESN=mdf['ESN']
     group_FIN=mdf['FIN']
     group_GBR=mdf['GBR']
     group_GIH=mdf['GIH']
     group_GWD=mdf['GWD']
     group_IBS=mdf['IBS']
     group_ITU=mdf['ITU']
     group_JPT=mdf['JPT']
     group_KHV=mdf['KHV']
     group_LWK=mdf['LWK']
     group_MSL=mdf['MSL']
     group_MXL=mdf['MXL']
     group_PEL=mdf['PEL']
     group_PJL=mdf['PJL']
     group_PUR=mdf['PUR']
     group_STU=mdf['STU']
     group_TSI=mdf['TSI']
     group_YRI=mdf['YRI']

     res = tukey_hsd(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)
     
     #f_statistic, p_value = f_oneway(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)

     #print(f"F-Statistic: {f_statistic:.2f}")
     #print(f"P-Value: {p_value:.4f}")


     pass