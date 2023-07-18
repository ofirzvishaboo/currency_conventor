import unittest
import functions
import API


dollar = API.get_data()[0]
shekel = API.get_data()[2]
eur = API.get_data()[1]


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('hello')

    def test_03(self):
        assert eur > dollar

    def test_02(self):
        assert dollar > shekel


    def test_04(self):
        data = functions.make_file_into_list()
        for line in data:
            try:
                if int(line[1]) > 4:
                    checking_results = float(line[3]) / float(line[1])
                else:
                    checking_results = float(line[3]) * float(line[1])
                assert checking_results == float(line[0])
            except ValueError:
                continue

    def test_01(self):
        assert eur > shekel

    @classmethod
    def tearDownClass(self):
        print(f"Dollar rate: {dollar}, EUR rate: {eur},"
              f" shekel rate: {shekel}")
