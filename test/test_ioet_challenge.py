import unittest

from ioet_challenge.scheduler import ACME_Scheduler

class ACME_TEST(unittest.TestCase):

    def test_hello_world(self):
        acme_scheduler = ACME_Scheduler() 
        self.assertEqual(acme_scheduler.hello_world(), "Hello World!")

if __name__ == '__main__':
    unittest.main()