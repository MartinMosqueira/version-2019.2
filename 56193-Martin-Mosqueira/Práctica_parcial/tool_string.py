
class ToolString():

    def is_upper(self, cadena):
        contador = 0
        for i in cadena:
            if i.isupper() == True:
                contador = +1
        if contador != 0:
            return True
        else:
            return False

    def is_palindromo(self, cadena):
        texto = cadena.replace(' ', '').lower()
        if (texto == texto[::-1]):
            return True
        else:
            return False
