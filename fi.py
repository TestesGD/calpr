import math
'''''
n = int(input('digite: '))


t1,t2 = 0,1


for _ in range(n+1):
    print(t1, end=' ')
    t1,t2 = t2, t1 + t2
'''
def sobra(tipo):
    tipos = {
        'reto':10,
        'cortes':15,
        'diagonal':20
    }
    return tipos.get(tipo.lower() , 10)
area =float(input('Digite a area: '))
lad_d_cm =float(input('digite a largura da base:'))
lad_e_cm =float(input('digite a altura: '))
tipo = input('digite o tipo: ')


lad_d_m= lad_d_cm /100
lad_e_m = lad_e_cm / 100

por  = sobra(tipo)

area_n = area / (lad_d_m * lad_e_m)
area_n *= (1 + por / 100)

area_n = math.ceil(area_n)
print(f'São necessarios {area_n:.2f} ')