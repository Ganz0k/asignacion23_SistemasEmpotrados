# MesaRedonda.py
# 4/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase MesaRedonda

from Mesa import Mesa
from math import pi


class MesaRedonda(Mesa):
    """Clase MesaRedonda la cual hereda a la clase abstracta Mesa
    """

    def __init__(self, costoCubierta: float, radio: float, costoPedestal: float):
        """Constructor que inicializa todos los parámetros de la clase

        --------------------------------------------------------------
        Parameters
        ----------
        costoCubierta: float
            Costo por metro cuadrado de la cubierta
        radio: float
            Radio de la mesa
        costoPedestal: float
            Costo del pedestal de la mesa
        """
        super().__init__('Mesa Redonda', costoCubierta)
        self.__radio = radio
        self.__costoPedestal = costoPedestal

    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """
        return pi * (self.__radio ** 2)

    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """
        return (self._costoCubierta * self.calculaArea()) + self.__costoPedestal

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return super().__str__() + f', radio: {self.__radio:.2f}, costo pedestal: {self.__costoPedestal:.2f}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return super().__repr__() + f', radio: {self.__radio:.2f}, costo pedestal: {self.__costoPedestal:.2f}'


if (__name__ == '__main__'):
    mesaRedonda1 = MesaRedonda(50.0, 0.50, 200.0)
    mesaRedonda2 = MesaRedonda(70.0, 0.60, 250.0)
    mesaRedonda3 = MesaRedonda(100.0, 0.75, 500.0)
    mesasRedondas = [mesaRedonda1, mesaRedonda2, mesaRedonda3]

    for mesa in mesasRedondas:
        print(mesa)
        print(f'Área = {mesa.calculaArea():.2f}')
        print(f'Costo = {mesa.calculaCosto():.2f}\n')
