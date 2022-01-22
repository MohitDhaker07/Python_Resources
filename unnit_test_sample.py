import unittest
import sample


class TestCap(unittest.TestCase):
    def test_one(self):
        text = 'python'
        result = sample.cap_text(text)
        self.assertEqual(result, 'Python')

    # def multiple_words(self):
    #     text = 'mohit dhaker'
    #     result = sample.cap_text(text)
    #     self.assertEqual(result, 'Mohit Dhaker')

    # def count_test(self):
    #     result = sample.words_in_name()
    #     self.assertEqual(result, 5)
    #     print("Successfull")


if __name__ == '__main__':
    unittest.main()
