import unittest
import functions

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('hello')

    # def test_03(self):
    #     assert MyTest.eur > MyTest.dollar
    #
    # def test_02(self):
    #     assert MyTest.dollar > MyTest.shekel


    def test_04(self):
        data = functions.make_file_into_list()
        for line in data:
            try:
                checking_results = float(line[3]) * float(line[1])
                assert checking_results == float(line[0])
            except ValueError:
                continue

    # def test_01(self):
    #     assert MyTest.shekel1 > MyTest.shekel
    #
    # @classmethod
    # def tearDownClass(self):
    #     print(f"Dollar rate: {MyTest.dollar/MyTest.shekel}, EUR rate: {MyTest.eur/MyTest.shekel},"
    #           f" shekel rate for usd: {MyTest.shekel/MyTest.dollar}, shekel rate for eur: {MyTest.shekel}")
