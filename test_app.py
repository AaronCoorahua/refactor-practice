import unittest
from app import CalculaGanador

class CalculaGanadorTest(unittest.TestCase):
    def setUp(self):
        self.calculador = CalculaGanador()

    def test_ganador(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0']
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Eddie Hinesley'])

    def test_empate(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],        
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Aundrea Grace'])

    def test_segunda_vuelta(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Max Antunez', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '40810962', 'Max Antunez', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57537797', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533554', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], 
            ['Áncash', 'Asunción', 'Acochaca', '86777546', 'Aundrea Grace', '1'],  
            ['Áncash', 'Asunción', 'Acochaca', '86772655', 'Aundrea Grace', '1'],     
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Eddie Hinesley','Aundrea Grace'])

if __name__ == '__main__':
    unittest.main()