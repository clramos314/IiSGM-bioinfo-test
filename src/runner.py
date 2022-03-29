from src.helpers import read_vcf
import os


if __name__ == '__main__':
    directory = "../data"
    VCFs_dict = {}

    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            result = read_vcf(f)
            # append in VCFs dictionary
            VCFs_dict[list(result.keys())[-1]] = result
