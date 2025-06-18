import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales

class TestOperacionesComparacion(unittest.TestCase):
    def test_es_mayor_que(self):
 # Casos donde a debe ser mayor que b
        self.assertGreater(es_mayor_que(5, 3), 0) # Ejemplo de aserción: 5 > 3 ->True
        self.assertTrue(es_mayor_que(10, 5)) # Otra forma de probar True
 # Casos donde a NO es mayor que b (debería retornar False)
        self.assertFalse(es_mayor_que(3, 5))
        self.assertFalse(es_mayor_que(5, 5))
    
    def test_es_menor_que(self):
 # Casos donde a debe ser menor que b
        self.assertTrue(es_menor_que(3, 5), 1) # Ejemplo de aserción: 3 < 5 -> True
        self.assertTrue(es_menor_que(0, 1))
 # Casos donde a NO es menor que b (debería retornar False)
        self.assertFalse(es_menor_que(5, 3))
        self.assertFalse(es_menor_que(5, 5))
    
    def test_es_mayor_o_igual_que(self):
 # Casos donde a debe ser mayor o igual que b
        self.assertTrue(es_mayor_o_igual_que(5, 3))
        self.assertTrue(es_mayor_o_igual_que(5, 5))
        self.assertGreaterEqual(es_mayor_o_igual_que(7, 7), 0) # Otra forma de probar True
 # Casos donde a NO es mayor o igual que b (debería retornar False)
        self.assertFalse(es_mayor_o_igual_que(3, 5))
    
    def test_es_menor_o_igual_que(self):
 # Casos donde a debe ser menor o igual que b
        self.assertTrue(es_menor_o_igual_que(3, 5))
        self.assertTrue(es_menor_o_igual_que(5, 5))
        self.assertLessEqual(es_menor_o_igual_que(2, 2), 1) # Otra forma de probar True
 # Casos donde a NO es menor o igual que b (debería retornar False)
        self.assertFalse(es_menor_o_igual_que(5, 3))
    
    def test_son_iguales(self):
 # Casos donde a y b son iguales
        self.assertTrue(son_iguales(7, 7))
        self.assertEqual(son_iguales(10, 10), True)
 # Casos donde a y b NO son iguales
        self.assertFalse(son_iguales(7, 8))
        self.assertEqual(son_iguales(1, 2), False)

if __name__ == '__main__':
 unittest.main()
       