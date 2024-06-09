from datetime import datetime

from src.model.ConversorDivisas import *


class Gasto:
    def __init__(self, fecha, valor, metodo_pago, tipo_gasto, moneda):
        """
        Inicializa un objeto Gasto.

        Args:
            fecha (datetime.date): La fecha del gasto.
            valor (float): El valor del gasto en la moneda original.
            metodo_pago (str): El método de pago ('efectivo' o 'tarjeta').
            tipo_gasto (str): El tipo de gasto (transporte, alojamiento, etc.).
            moneda (str): La moneda del gasto ('USD' o 'EUR').
        """
        self.fecha = fecha
        self.valor = valor
        self.metodo_pago = metodo_pago
        self.tipo_gasto = tipo_gasto
        self.valor_en_cop = ConversorDivisas.convertir_a_cop(valor, moneda)

    def to_dict(self):
        """
        Convierte el objeto Gasto a un diccionario para su serialización.

        Returns:
            dict: El diccionario con los datos del gasto.
        """
        return {
            'fecha': self.fecha.strftime("%Y-%m-%d"),
            'valor': self.valor,
            'metodo_pago': self.metodo_pago,
            'tipo_gasto': self.tipo_gasto,
            'valor_en_cop': self.valor_en_cop
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Gasto a partir de un diccionario.

        Args:
            data (dict): El diccionario con los datos del gasto.

        Returns:
            Gasto: El objeto Gasto creado.
        """
        fecha = datetime.strptime(data['fecha'], "%Y-%m-%d").date()
        gasto = Gasto(fecha, data['valor'], data['metodo_pago'], data['tipo_gasto'], 'COP')
        gasto.valor_en_cop = data['valor_en_cop']
        return gasto