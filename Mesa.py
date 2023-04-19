# Mesa.py
# 4/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase abstracta Mesa

import abc


class Mesa(abc.ABC):
    """Clase abstracta Mesa
    """

    def __init__(self, tipoMesa: str, costoCubierta: float):
        """Constructor que inicializa todos los parámetros

        --------------------------------------------------
        Parameters
        ----------
        tipoMesa: str
            Tipo de la mesa
        costoCubierta: float
            Costo por metro cuadrado de la cubierta
        """
        self._tipoMesa = tipoMesa
        self._costoCubierta = costoCubierta

    @abc.abstractmethod
    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """

    @abc.abstractmethod
    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """

    @abc.abstractmethod
    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return f'Tipo de mesa: {self._tipoMesa}, Costo por metro cuadrado de la cubierta: {self._costoCubierta:.2f}'

    @abc.abstractmethod
    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return f'{self.__module__}, {self.__class__.__name__}, Tipo de mesa: {self._tipoMesa}, Costo por metro cuadrado de la cubierta: {self._costoCubierta:.2f}'
