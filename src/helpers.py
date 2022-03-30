import io
import pandas as pd


def read_vcf(path):
    with open(path, 'r') as f:
        lines = [li for li in f if not li.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})


def extract_relevant_inf(df):
    # extracting a DataFrame containing fields 'POS', 'REF', 'ALT'
    return df.iloc[:, [1, 3, 4]]
