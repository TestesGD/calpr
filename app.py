"""""
lista = [1,2,5,9,4,5]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i],lista[j]= lista[j],lista[i]

lista.reverse()
print(lista)"""
import math
class Concreto:
    """"
    Class que calcula propriedades de um retângulo    
    """ 
    def __init__(self,base = None, altura = None,raio=None):
        self.base = base
        self.altura = altura
        self.raio = raio

    def area_tri(self):
        
        area = (self.base * self.altura) / 2
        return f"A área do triângulo é: {area}"
    def area_ret(self):
        
        area = self.base * self.altura
        return f"A área do retângulo é: {area}"

    def area_c(self):
        area = math.pi * self.raio **2

        return f'A area do círculo é: {area:.2f}' 

    @staticmethod
    def calcular_pecas(area, largura_cm, altura_cm, tipo):
        tipos = {
            'reto': 10,
            'cortes': 15,
            'diagonal': 20
        }

        largura_m = largura_cm / 100
        altura_m = altura_cm / 100

        porcentagem = tipos.get(tipo.lower(), 10)

        pecas = area / (largura_m * altura_m)
        pecas *= (1 + porcentagem / 100)

        return math.ceil(pecas)