# PruebaMesa.py
# 4/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo de prueba para las clases Mesa, MesaRedonda y MesaRectangular

from MesaRedonda import MesaRedonda
from MesaRectangular import MesaRectangular

mesaRedonda1 = MesaRedonda(50.0, 0.50, 200.0)
mesaRedonda2 = MesaRedonda(70.0, 0.60, 250.0)
mesaRedonda3 = MesaRedonda(100.0, 0.75, 500.0)
mesaRectangular1 = MesaRectangular(50.0, 1.0, 1.0, 30.0)
mesaRectangular2 = MesaRectangular(70.0, 1.0, 1.2, 40.0)
mesaRectangular3 = MesaRectangular(100.0, 1.2, 1.5, 50.0)

mesas = [mesaRedonda1, mesaRedonda2, mesaRedonda3,
         mesaRectangular1, mesaRectangular2, mesaRectangular3]

for mesa in mesas:
    print(mesa)
    print(f'Área = {mesa.calculaArea():.2f}')
    print(f'Costo = {mesa.calculaCosto():.2f}\n')
