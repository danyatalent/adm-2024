import unittest
from combination import *

class TestComb(unittest.TestCase):
    """Класс тестирования возможностей класса CombinatorialScheme и его наследников"""
    def test_sum_rule(self):
        """Тест для правила суммы."""
        sum_rule = SumRule("Test Sum Rule")
        n = 5
        k = 3
        expected_result = n * k
        self.assertEqual(sum_rule.execute(n, k, 1), expected_result)

    def test_product_rule(self):
        """Тест для правила произведения."""
        product_rule = ProductRule("Test Product Rule")
        n = 5
        k = 3
        expected_result = n ** k
        self.assertEqual(product_rule.execute(n, k, 1), expected_result)

    def test_perm_with_rep(self):
        """Тест для перестановок с повторениями."""
        perm_with_rep = PermWithRep("Test Perm With Rep")
        n = 5
        k = 3
        expected_result = n ** k
        self.assertEqual(perm_with_rep.execute(n, k, 1), expected_result)

    def test_perm_without_rep(self):
        """Тест для перестановок без повторений."""
        perm_without_rep = PermWithoutRep("Test Perm Without Rep")
        n = 5
        k = 3
        expected_result = 60
        self.assertEqual(perm_without_rep.execute(n, k, 1), expected_result)

    def test_comb_with_rep(self):
        """Тест для сочетаний с повторениями."""
        comb_with_rep = CombWithRep("Test Comb With Rep")
        n = 5
        k = 3
        expected_result = 35
        self.assertEqual(comb_with_rep.execute(n, k, 1), expected_result)

    def test_comb_without_rep(self):
        """Тест для сочетаний без повторений."""
        comb_without_rep = CombWithoutRep("Test Comb Without Rep")
        n = 5
        k = 3
        expected_result = 10
        self.assertEqual(comb_without_rep.execute(n, k, 1), expected_result)

    def test_arrange_with_rep(self):
        """Тест для размещений с повторениями"""
        arrange_with_rep = ArrangeWithRep("Test Arrange With Rep")
        n = 5
        k = 3
        expected_result = n ** k
        self.assertEqual(arrange_with_rep.execute(n, k, 1), expected_result)

    def test_arrange_without_rep(self):
        """Тест для размещений без потворений"""
        arrange_without_rep = ArrangeWithoutRep("Test Arrange Without Rep")
        n = 5
        k = 3
        expected_result = 60
        self.assertEqual(arrange_without_rep.execute(n, k, 1), expected_result)


if __name__ == '__main__':
    unittest.main()