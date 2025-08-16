import pandas as pd
from scipy import stats
from pathlib import Path
from os.path import join
import matplotlib.pyplot as plt
from scipy.stats import tukey_hsd
from scipy.stats import f_oneway

from mylib import create_mean_variant_count_all_population_df
from mylib import create_total_variant_count_all_population_df
from mylib import create_per_genome_variant_mean_all_population_df
from mylib import genomes
from mylib import compute_ttest

def attic():
    outputfile= join(root_dir, "analysis/20250816/variant_count_all_populations.csv")
    mdf = create_total_variant_count_all_population_df(root_dir=root_dir, genomes=genomes, outputfile=outputfile)

    population_names = list(mdf.columns)

    l = list()
    tl = list()
    for ppn in population_names:
        l.append(f"group_{ppn} = mdf['{ppn}']")
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


    compute_ttest(mdf=mdf, population_name_1=population_name_1, population_name_2=population_name_2)


    # population_name_1 = "GBR"
    # population_name_2 = "ASW"
    # t_statistic, p_value = stats.ttest_ind(mdf[population_name_1], mdf[population_name_2], equal_var=True)
    # print(f"\nTwo-Sample Independent T-Test for {population_name_1} and {population_name_2}:")
    # print(f"T-statistic: {t_statistic:.4f}")
    # print(f"P-value: {p_value:.4f}")

def mean_variant_all_genomes_statistical_analysis(root_dir):
    """
    This method works for all populations.

    For each population, it calculates variant mean for each gene and across all genomes.
    It then performs statistical analysis.

    """
    outputfile= join(root_dir, "analysis/20250816/mean_variant_all_genomes.csv")
    mdf = create_mean_variant_count_all_population_df(root_dir=root_dir, genomes=genomes, outputfile=outputfile)
    
    # outputfile= join(root_dir, "analysis/20250816/variant_count_all_populations.csv")
    # mdf = create_total_variant_count_all_population_df(root_dir=root_dir, genomes=genomes, outputfile=outputfile)

    group_ACB = mdf['ACB']
    group_ASW = mdf['ASW']
    group_BEB = mdf['BEB']
    group_CDX = mdf['CDX']
    group_CHB = mdf['CHB']
    group_CHS = mdf['CHS']
    group_CLM = mdf['CLM']
    group_ESN = mdf['ESN']
    group_FIN = mdf['FIN']
    group_GBR = mdf['GBR']
    group_GIH = mdf['GIH']
    group_GWD = mdf['GWD']
    group_IBS = mdf['IBS']
    group_ITU = mdf['ITU']
    group_JPT = mdf['JPT']
    group_KHV = mdf['KHV']
    group_LWK = mdf['LWK']
    group_MSL = mdf['MSL']
    group_MXL = mdf['MXL']
    group_PEL = mdf['PEL']
    group_PJL = mdf['PJL']
    group_PUR = mdf['PUR']
    group_STU = mdf['STU']
    group_TSI = mdf['TSI']
    group_YRI = mdf['YRI']

    res = tukey_hsd(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)
    # Perform one-way ANOVA
    f_statistic, p_value = f_oneway(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)

    # Print the results
    print(f"F-Statistic: {f_statistic:.2f}")
    print(f"P-Value: {p_value:.4f}")

    
    pvalue_outputfile= join(root_dir, "analysis/20250816/mean_variant_all_genomes.pvalue.csv")
    odf = pd.DataFrame(res.pvalue, index=mdf.columns, columns=mdf.columns)
    odf.to_csv(pvalue_outputfile)

    pass

def total_variant_all_genomes_statistical_analysis(root_dir):
    """
    This method works for all populations.

    For each population, it calculates variant total count for each gene and across all genomes.
    It then performs statistical analysis.

    """
    outputfile= join(root_dir, "analysis/20250816/total_variant_all_genomes.csv")
    mdf = create_total_variant_count_all_population_df(root_dir=root_dir, genomes=genomes, outputfile=outputfile)
    
    group_ACB = mdf['ACB']
    group_ASW = mdf['ASW']
    group_BEB = mdf['BEB']
    group_CDX = mdf['CDX']
    group_CHB = mdf['CHB']
    group_CHS = mdf['CHS']
    group_CLM = mdf['CLM']
    group_ESN = mdf['ESN']
    group_FIN = mdf['FIN']
    group_GBR = mdf['GBR']
    group_GIH = mdf['GIH']
    group_GWD = mdf['GWD']
    group_IBS = mdf['IBS']
    group_ITU = mdf['ITU']
    group_JPT = mdf['JPT']
    group_KHV = mdf['KHV']
    group_LWK = mdf['LWK']
    group_MSL = mdf['MSL']
    group_MXL = mdf['MXL']
    group_PEL = mdf['PEL']
    group_PJL = mdf['PJL']
    group_PUR = mdf['PUR']
    group_STU = mdf['STU']
    group_TSI = mdf['TSI']
    group_YRI = mdf['YRI']

    res = tukey_hsd(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)
    # Perform one-way ANOVA
    f_statistic, p_value = f_oneway(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)

    # Print the results
    print(f"F-Statistic: {f_statistic:.2f}")
    print(f"P-Value: {p_value:.4f}")

    
    pvalue_outputfile= join(root_dir, "analysis/20250816/total_variant_all_genomes.pvalue.csv")
    odf = pd.DataFrame(res.pvalue, index=mdf.columns, columns=mdf.columns)
    odf.to_csv(pvalue_outputfile)

    pass

def per_genome_variant_mean_statistical_analysis(root_dir):
    outputfile= join(root_dir, "analysis/20250816/per_genome_variant_mean_all_populations.csv")
    all_dict = create_per_genome_variant_mean_all_population_df(root_dir=root_dir, genomes=genomes, outputfile=outputfile)

    group_ACB = all_dict['ACB']
    group_ASW = all_dict['ASW']
    group_BEB = all_dict['BEB']
    group_CDX = all_dict['CDX']
    group_CHB = all_dict['CHB']
    group_CHS = all_dict['CHS']
    group_CLM = all_dict['CLM']
    group_ESN = all_dict['ESN']
    group_FIN = all_dict['FIN']
    group_GBR = all_dict['GBR']
    group_GIH = all_dict['GIH']
    group_GWD = all_dict['GWD']
    group_IBS = all_dict['IBS']
    group_ITU = all_dict['ITU']
    group_JPT = all_dict['JPT']
    group_KHV = all_dict['KHV']
    group_LWK = all_dict['LWK']
    group_MSL = all_dict['MSL']
    group_MXL = all_dict['MXL']
    group_PEL = all_dict['PEL']
    group_PJL = all_dict['PJL']
    group_PUR = all_dict['PUR']
    group_STU = all_dict['STU']
    group_TSI = all_dict['TSI']
    group_YRI = all_dict['YRI']

    res = tukey_hsd(group_ACB,group_ASW,group_BEB,group_CDX,group_CHB,group_CHS,group_CLM,group_ESN,group_FIN,group_GBR,group_GIH,group_GWD,group_IBS,group_ITU,group_JPT,group_KHV,group_LWK,group_MSL,group_MXL,group_PEL,group_PJL,group_PUR,group_STU,group_TSI,group_YRI)

    odf = pd.DataFrame(res.pvalue, index=all_dict.keys(), columns=all_dict.keys())
    pvalue_outputfile= join(root_dir, "analysis/20250816/per_genome_variant_mean_all_populations.pvalue.csv")
    odf.to_csv(pvalue_outputfile)

if __name__ == "__main__":
    root_dir = join(Path.home(),"cp_als")

    #per_genome_variant_mean_statistical_analysis(root_dir=root_dir)
    #mean_variant_all_genomes_statistical_analysis(root_dir=root_dir) 
    total_variant_all_genomes_statistical_analysis(root_dir=root_dir)
    pass
