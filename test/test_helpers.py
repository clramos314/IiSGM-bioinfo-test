import unittest

from src.helpers import read_vcf


class Test(unittest.TestCase):
    def test_read_vcf_ok(self):
        result = read_vcf("../data/10082989-0-COL2.combined.hf.SNP.final.vcf")
        self.assertIsNotNone(result)

    def test_read_vcf_not_found(self):
        with self.assertRaises(FileNotFoundError):
            result = read_vcf("")


if __name__ == '__main__':
    unittest.main()
