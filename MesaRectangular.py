# MesaRectangular.py
# 4/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase MesaRectangular

from Mesa import Mesa


class MesaRectangular(Mesa):
    """Clase MesaRectangular la cual hereda a la clase abstracta Mesa
    """

    def __init__(self, costoCubierta: float, ancho: float, largo: float, costoPata: float):
        """Constructor que inicializa todos los parámetros de la clase

        --------------------------------------------------------------
        Parameters
        ----------
        costoCubierta: float
            Costo por metro cuadrado de la cubierta
        ancho: float
            Ancho de la cubierta
        largo: float
            Largo de la cubierta
        costoPata: float
            Costo por pata de la mesa
        """
        super().__init__('Mesa Rectangular', costoCubierta)
        self.__ancho = ancho
        self.__largo = largo
        self.__costoPata = costoPata

    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """
        return self.__ancho * self.__largo

    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """
        return (self._costoCubierta * self.calculaArea()) + (self.__costoPata * 4)

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return super().__str__() + f', ancho: {self.__ancho:.2f}, largo: {self.__largo:.2f}, costo pata: {self.__costoPata:.2f}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return super().__repr__() + f', ancho: {self.__ancho:.2f}, largo: {self.__largo:.2f}, costo pata: {self.__costoPata:.2f}'


if (__name__ == '__main__'):
    mesaRectangular1 = MesaRectangular(50.0, 1.0, 1.0, 30.0)
    mesaRectangular2 = MesaRectangular(70.0, 1.0, 1.2, 40.0)
    mesaRectangular3 = MesaRectangular(100.0, 1.2, 1.5, 50.0)
    mesasRectangulares = [mesaRectangular1, mesaRectangular2, mesaRectangular3]

    for mesa in mesasRectangulares:
        print(mesa)
        print(f'Área = {mesa.calculaArea():.2f}')
        print(f'Costo = {mesa.calculaCosto():.2f}\n')
