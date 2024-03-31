import unittest
import analyze


class TestAnalyze(unittest.TestCase):
    def setUp(self):
        self.data = analyze.df.to_dict()

    def assertAllEqual(self, *args):
        first = args[0]
        for arg in args[1:]:
            self.assertEqual(first, arg)

    def test_data(self):
        self.assertAllEqual(len(self.data['Subject1'].keys()), len(self.data['Subject2'].keys()), len(self.data['Correlation'].keys()))


if __name__ == '__main__':
    unittest.main()
