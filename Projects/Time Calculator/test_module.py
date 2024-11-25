import unittest
from Time_Calculator import add_time

class UnitTests(unittest.TestCase):

    def test_1(self):
        calculated_answer = add_time('3:30 PM', '2:12')
        correct_answer = '5:42 PM'
        self.assertEqual(calculated_answer, correct_answer)

    def test_2(self):
        calculated_answer = add_time('11:55 AM', '3:12')
        correct_answer = '3:07 PM'
        self.assertEqual(calculated_answer, correct_answer)

    def test_3(self):
        calculated_answer = add_time('2:59 AM', '24:00')
        correct_answer = '2:59 AM (next day)'
        self.assertEqual(calculated_answer, correct_answer)

    def test_4(self):
        calculated_answer = add_time('11:59 PM', '24:05')
        correct_answer = '12:04 AM (2 days later)'
        self.assertEqual(calculated_answer, correct_answer)

    def test_5(self):
        calculated_answer = add_time('8:16 PM', '466:02')
        correct_answer = '6:18 AM (20 days later)'
        self.assertEqual(calculated_answer, correct_answer)

    def test_6(self):
        calculated_answer = add_time('3:30 PM', '2:12', 'Monday')
        correct_answer = '5:42 PM, Monday'
        self.assertEqual(calculated_answer, correct_answer)

    def test_7(self):
        calculated_answer = add_time('2:59 AM', '24:00', 'saturDay')
        correct_answer = '2:59 AM, Sunday (next day)'
        self.assertEqual(calculated_answer, correct_answer)

    def test_8(self):
        calculated_answer = add_time('11:59 PM', '24:05', 'Wednesday')
        correct_answer = '12:04 AM, Friday (2 days later)'
        self.assertEqual(calculated_answer, correct_answer)

    def test_9(self):
        calculated_answer = add_time('8:16 PM', '466:02', 'tuesday')
        correct_answer = '6:18 AM, Monday (20 days later)'
        self.assertEqual(calculated_answer, correct_answer)

if __name__ == '__main__':
    unittest.main()
