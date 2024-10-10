import unittest
from dinamica import subasta_optima

class TestSubastaOptima(unittest.TestCase):
    def test_single_offer(self):
        A = 10
        B = 5
        n = 1
        ofertas = [(10, 1, 10)]
        asignacion, max_beneficio = subasta_optima(A, B, n, ofertas)
        self.assertEqual(asignacion, [10])
        self.assertEqual(max_beneficio, 100)

    def test_multiple_offers(self):
        A = 10
        B = 5
        n = 2
        ofertas = [(10, 1, 5), (8, 2, 6)]
        asignacion, max_beneficio = subasta_optima(A, B, n, ofertas)
        self.assertEqual(asignacion, [5, 5])
        self.assertEqual(max_beneficio, 90)

    def test_no_offers(self):
        A = 10
        B = 5
        n = 0
        ofertas = []
        asignacion, max_beneficio = subasta_optima(A, B, n, ofertas)
        self.assertEqual(asignacion, [10])
        self.assertEqual(max_beneficio, 50)

    def test_partial_assignment(self):
        A = 10
        B = 5
        n = 3
        ofertas = [(10, 1, 3), (8, 2, 4), (7, 1, 2)]
        asignacion, max_beneficio = subasta_optima(A, B, n, ofertas)
        self.assertEqual(asignacion, [3, 4, 2, 1])
        self.assertEqual(max_beneficio, 86)

    def test_exact_assignment(self):
        A = 15
        B = 5
        n = 3
        ofertas = [(10, 5, 5), (8, 5, 5), (7, 5, 5)]
        asignacion, max_beneficio = subasta_optima(A, B, n, ofertas)
        self.assertEqual(asignacion, [5, 5, 5])
        self.assertEqual(max_beneficio, 125)

if __name__ == '__main__':
    unittest.main()