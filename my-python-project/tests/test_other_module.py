import unittest
from src import other_module

class TestOtherModule(unittest.TestCase):

    def setUp(self):
        pass

    def test_function_in_other_module(self):
        # Call the function you want to test
        # result = other_module.function_name()
        # self.assertEqual(expected_result, result)
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()