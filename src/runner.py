from src.helpers import read_vcf, extract_relevant_inf
import os


if __name__ == '__main__':
    directory = "../data"
    VCFs_dict = {}

    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            result = read_vcf(f)
            # append in VCFs dictionary by extracting relevant information
            sample_name = list(result.keys())[-1]
            VCFs_dict[sample_name] = extract_relevant_inf(result)
            print(VCFs_dict)
