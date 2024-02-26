import unittest
from combination import ArrangeWithRep

class TestArrangeWithRep(unittest.TestCase):

    def test_arrange_with_rep(self):
        arrange_with_rep = ArrangeWithRep("Test Arrange With Rep")
        n = 5
        k = 3
        expected_result = 5 ** 3  # Calculating the expected result manually
        self.assertEqual(arrange_with_rep.execute(5, 3, 0), expected_result)

if __name__ == '__main__':
    unittest.main()