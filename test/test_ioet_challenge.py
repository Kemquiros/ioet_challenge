import unittest
from ioet_challenge.reader import Reader

from ioet_challenge.scheduler import ACME_Scheduler

class ACME_TEST(unittest.TestCase):

    def test_reader_default_path(self):
        new_reader = Reader()
        self.assertEqual(new_reader.path, "./data/data1.txt")

    def test_reader_custom_path(self):
        test_path = "my_folder/data.txt"
        new_reader = Reader(test_path)
        self.assertEqual(new_reader.path, test_path)

    def test_reader_data_not_found(self):
        test_path = "my_bad_folder/bad_file.txt"
        new_reader = Reader(test_path)
        with self.assertRaises((FileNotFoundError,SystemExit)):
            new_reader.load_data()

    def test_reader_load_data(self):
        new_reader = Reader()
        new_reader.load_data()
        self.assertGreaterEqual(len(new_reader.data),5)

    def test_calc_salary_slot(self):
        acme_scheduler = ACME_Scheduler(None) 
        self.assertEqual(acme_scheduler.calc_salary_slot("MO",3,40,6,40),3*25)

if __name__ == '__main__':
    unittest.main()