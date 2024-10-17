import unittest
from fuerza_bruta import subasta_fuerza_bruta

class TestSubastaOptima(unittest.TestCase):
    def test_single_offer(self):
        A = 1000
        B = 100
        n = 1
        ofertas = [(500, 100, 600), (100, 0, 1000)]
        mejor_asignacion, mejor_total = subasta_fuerza_bruta(A, B, n, ofertas)
        self.assertEqual(mejor_asignacion, [600,400])
        self.assertEqual(mejor_total, 340000)

    def test_multiple_offers(self):
        A = 1000
        B = 100
        n = 2
        ofertas = [(500,100, 600), (450, 400, 800), (100, 0, 1000)]
        mejor_asignacion, mejor_total = subasta_fuerza_bruta(A, B, n, ofertas)
        self.assertEqual(mejor_asignacion, [600,400, 0])
        self.assertEqual(mejor_total, 480000)

    def test_no_offers(self):
        A = 1000
        B = 100
        n = 0
        ofertas = [(100,0,1000)]
        mejor_asignacion, mejor_total = subasta_fuerza_bruta(A, B, n, ofertas)
        self.assertEqual(mejor_asignacion, [1000])
        self.assertEqual(mejor_total, 100000)

    def test_partial_assignment(self):
        A = 1000
        B = 100
        n = 3
        ofertas = [(500, 100, 600), (450, 400, 800), (300,100,300), (100, 0, 1000)]
        mejor_asignacion, mejor_total = subasta_fuerza_bruta(A, B, n, ofertas)
        self.assertEqual(mejor_asignacion, [600, 400, 0, 0])
        self.assertEqual(mejor_total, 480000)

    def test_exact_assignment(self):
        A = 1000
        B = 100
        n = 3
        ofertas = [(500, 400, 600), (100, 400, 800), (200, 100, 700), (100, 0, 1000)]
        mejor_asignacion, mejor_total = subasta_fuerza_bruta(A, B, n, ofertas)
        self.assertEqual(mejor_asignacion, [600, 0, 400, 0])
        self.assertEqual(mejor_total, 380000)

if __name__ == '__main__':
    unittest.main()