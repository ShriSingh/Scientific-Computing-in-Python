import unittest
from Arithmetic_Formatter import arithmetic_arranger

class UnitTests(unittest.TestCase):

    def test_1(self):
        answer_produced = arithmetic_arranger(["3801 - 2", "123 + 49"], True)
        answer_expected = "  3801      123\n-    2    +  49\n------    -----"
        self.assertEqual(answer_produced, answer_expected)

    def test_2(self):
        answer_produced = arithmetic_arranger(["1 + 2", "1 - 9380"], True)
        answer_expected = "  1         1\n+ 2    - 9380\n---    ------"
        self.assertEqual(answer_produced, answer_expected)

    def test_3(self):
        answer_produced = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True)
        answer_expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(answer_produced, answer_expected)

    def test_4(self):
        answer_produced = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)
        answer_expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(answer_produced, answer_expected)

    def test_5(self):
        answer_produced = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True)
        answer_expected = "Error: Too many problems."
        self.assertEqual(answer_produced, answer_expected)

    def test_6(self):
        answer_produced = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], True)
        answer_expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(answer_produced, answer_expected)

    def test_7(self):
        answer_produced = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"], True)
        answer_expected = "Error: Numbers must only contain digits."
        self.assertEqual(answer_produced, answer_expected)

    def test_8(self):
        answer_produced = arithmetic_arranger(["3 + 855", "988 + 40"], True)
        answer_expected = "    3      988\n+ 855    +  40\n-----    -----\n  858     1028"
        self.assertEqual(answer_produced, answer_expected)
    
    def test_9(self):
        answer_produced = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
        answer_expected = "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"
        self.assertEqual(answer_produced, answer_expected)

if __name__ == "__main__":
    unittest.main()
