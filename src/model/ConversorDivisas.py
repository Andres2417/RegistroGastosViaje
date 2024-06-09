import requests


class ConversorDivisas:
    @staticmethod
    def obtener_tasa():
        """
        Obtiene una tasa de conversión aleatoria de una API externa.

        Returns:
            int: La tasa de conversión obtenida.
        """
        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
        tasa = response.json()[0]['random']
        return tasa

    @staticmethod
    def convertir_a_cop(monto, moneda):
        """
        Convierte un monto de una moneda específica a pesos colombianos (COP).

        Args:
            monto (float): El monto en la moneda original.
            moneda (str): La moneda original ('USD' o 'EUR').

        Returns:
            float: El monto convertido a pesos colombianos.
        """
        tasa = ConversorDivisas.obtener_tasa()
        if moneda == "EUR":
            tasa += 200
        return monto * tasa