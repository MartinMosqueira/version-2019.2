import unittest
from tool_string import ToolString

class TestPractica(unittest.TestCase):

    def test_mayuscula_1(self):
        tool_string = ToolString()
        self.assertTrue(tool_string.is_upper('SAN LUIS'))

    def test_mayuscula_2(self):
        tool_string = ToolString()
        self.assertTrue(tool_string.is_upper('PYTHON'))

    def test_no_mayuscula_1(self):
        tool_string = ToolString()
        self.assertFalse(tool_string.is_upper('cordoba'))

    def test_no_mayuscula_2(self):
        tool_string = ToolString()
        self.assertFalse(tool_string.is_upper('flask'))


    def test_palindromo_1(self):
        tool_string = ToolString()
        self.assertTrue(tool_string.is_palindromo('neuquen'))

    def test_palindromo_2(self):
        tool_string = ToolString()
        self.assertTrue(tool_string.is_palindromo('agita falsos usos la fatiga'))

    def test_no_palindromo_1(self):
        tool_string = ToolString()
        self.assertFalse(tool_string.is_palindromo('mendoza'))

    def test_no_palindromo_2(self):
        tool_string = ToolString()
        self.assertFalse(tool_string.is_palindromo('la programacion requiere muchas horas de practica'))


if __name__ == '__main__':
    unittest.main()