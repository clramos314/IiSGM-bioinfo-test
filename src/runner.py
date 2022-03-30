import numpy as np

from src.helpers import read_vcf, extract_relevant_inf
import os
import pandas as pd
from functools import reduce


if __name__ == '__main__':
    directory = "../data"
    VCFs_dict = {}
    sample_names = []
    frames = []

    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            result = read_vcf(f)

            # append by sample names
            sample_name = list(result.keys())[-1]
            sample_names.append(sample_name)
            # result['sample_name'] = str(sample_name)

            # append by extracting relevant information
            df = extract_relevant_inf(result)
            VCFs_dict[sample_name] = df
            frames.append(df)
            # print(df)

    # merge all previous frames
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=["POS", "REF", "ALT"],
                                                    how='outer'), VCFs_dict.values())
    # print(df_merged)

    presence_absence_dict = {}
    # iterate over dataframe merged
    for index, row in df_merged.iterrows():
        snp_name = "{} {} {}".format(row["POS"], row["REF"], row["ALT"])

        # iterate over each VCFs_dict element
        for key in VCFs_dict.keys():
            item = VCFs_dict[key]

            condition = np.logical_and(item["POS"] == row["POS"], item["REF"] == row["REF"], item["ALT"] == row["ALT"])
            condition = np.array(condition)
            if True in condition:
                row[key] = 1
            else:
                row[key] = 0

        presence_absence_dict[snp_name] = row[3:]

    presence_absence_df = pd.DataFrame.from_dict(presence_absence_dict, orient='index')
    # print(presence_absence_df)

    presence_absence_df.to_csv(str('../temp/dfs_merged.tsv'), sep='\t', index=True)

