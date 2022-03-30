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


def delete_indels(ref, alt):
    if len(ref) == 1 and len(alt) > 1:
        return str(alt).split(',')[0]
    else:
        return alt


def extract_relevant_inf_snp(df):
    # extracting a DataFrame containing fields 'POS', 'REF', 'ALT'
    df = df.iloc[:, [1, 3, 4]]
    df['ALT'] = df.apply(lambda x: delete_indels(x['REF'], x['ALT']), axis=1)
    return df
