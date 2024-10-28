import unittest
from voraz import subasta_voraz

class TestSubastaVoraz(unittest.TestCase):
    def test_single_offer(self):
        A = 1000
        B = 100
        n = 1
        ofertas = [(500, 100, 600), (100, 0, 1000)]
        asignacion, valor_total = subasta_voraz(A, B, n, ofertas)
        self.assertEqual(asignacion.tolist(), [600, 400])
        self.assertEqual(valor_total, 340000)

    def test_multiple_offers(self):
        A = 1000
        B = 100
        n = 2
        ofertas = [(500, 100, 600), (450, 400, 800), (100, 0, 1000)]
        asignacion, valor_total = subasta_voraz(A, B, n, ofertas)
        self.assertEqual(asignacion.tolist(), [600, 400, 0])
        self.assertEqual(valor_total, 480000)

    def test_no_offers(self):
        A = 1000
        B = 100
        n = 0
        ofertas = [(100, 0, 1000)]
        asignacion, valor_total = subasta_voraz(A, B, n, ofertas)
        self.assertEqual(asignacion.tolist(), [1000])
        self.assertEqual(valor_total, 100000)

    def test_partial_assignment(self):
        A = 1000
        B = 100
        n = 3
        ofertas = [(500, 100, 600), (450, 400, 800), (300, 100, 300), (100, 0, 1000)]
        asignacion, valor_total = subasta_voraz(A, B, n, ofertas)
        self.assertEqual(asignacion.tolist(), [600, 400, 0, 0])
        self.assertEqual(valor_total, 480000)

    def test_exact_assignment(self):
        A = 1000
        B = 100
        n = 3
        ofertas = [(500, 400, 600), (100, 400, 800), (200, 100, 700), (100, 0, 1000)]
        asignacion, valor_total = subasta_voraz(A, B, n, ofertas)
        self.assertEqual(asignacion.tolist(), [600, 0, 400, 0])
        self.assertEqual(valor_total, 380000)

    def test_no_assignment(self):
        A = 1000
        B = 100
        n = 4
        ofertas = [(500, 100, 600), (450, 400, 800), (300, 100, 300), (200, 100, 700), (100, 0, 1000)]
        asignacion, valor_total = subasta_voraz(A, B, n, ofertas)
        self.assertEqual(asignacion.tolist(), [600, 400, 0, 0, 0])
        self.assertEqual(valor_total, 480000)

if __name__ == '__main__':
    unittest.main()