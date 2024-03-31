import unittest
import sys
import os
import report_cards


class TestExtraction(unittest.TestCase):
    def setUp(self):
        os.system(f'rm -r {report_cards.folder}*.json')

    def test_extractor(self):
        report_cards.main()
        pdfs = [i for i in os.listdir(report_cards.folder) if i.endswith('.pdf')]
        jsons = [i for i in os.listdir(report_cards.folder) if i.endswith('.json')]
        self.assertEqual(len(pdfs), len(jsons))


if __name__ == '__main__':
    unittest.main()
