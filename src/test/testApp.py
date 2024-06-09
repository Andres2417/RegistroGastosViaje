import unittest
from unittest.mock import MagicMock, patch

from src.model.ConversorDivisas import ConversorDivisas
from src.model.Viaje import Viaje

class TestReporteDiario(unittest.TestCase):
    """
    Verificar que el método obtener_reporte_diario de la clase Viaje genere un reporte diario de
    gastos correctamente cuando se registra al menos un gasto en el viaje.

    Resultado esperado:
        - Se espera que el reporte generado contenga un solo día
        (5 de junio de 2024) con los detalles del gasto registrado.

        Validación:
        - Se verifica que la longitud del reporte sea igual a 1, lo que indica que se ha generado
        correctamente un reporte para un día específico.
    """
    def test_obtener_reporte_diario(self):
        viaje = Viaje('Paris', '2024-06-01', '2024-06-10', 500000)
        viaje.registrar_gasto('2024-06-05', 100, 'efectivo', 'transporte', 'eur')
        reporte = viaje.obtener_reporte_diario()
        self.assertEqual(len(reporte), 1)

class TestConversorDivisas(unittest.TestCase):
    """
           Verifica que el método obtener_tasa de la clase ConversorDivisas obtenga correctamente la tasa de
           conversión cuando se simula una respuesta exitosa de la API externa.

           Resultado esperado:
           - Se espera que el valor devuelto por el método obtener_tasa sea igual a 4000,
           que es la tasa de conversión simulada.

           Validación:
           - Se verifica que el valor devuelto por el método obtener_tasa sea igual a 4000,
           lo que indica que la tasa de conversión se obtuvo correctamente.
           """

    @patch('src.model.ConversorDivisas.requests.get')
    def test_obtener_tasa(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [{'random': 4000}]
        mock_get.return_value = mock_response
        tasa = ConversorDivisas.obtener_tasa()
        self.assertEqual(tasa, 4000)



class TestRegistroGasto(unittest.TestCase):

    def test_registrar_gasto_exitoso(self):
        """
        Verifica que el método registrar_gasto de la clase Viaje registre un gasto correctamente en el viaje.

        Resultado esperado:
        - Se espera que el gasto se registre correctamente en el viaje,
        aumentando la longitud de la lista de gastos del viaje en 1.

        Validación:
        - Se verifica que la longitud de la lista de gastos del viaje después de llamar al método registrar_gasto
         sea igual a 1 más la longitud antes de llamar al método.
        """
        viaje = Viaje('Paris', '2024-06-01', '2024-06-10', 500000)
        longitud_inicial_gastos = len(viaje.gastos)
        viaje.registrar_gasto('2024-06-05', 100, 'efectivo', 'transporte', 'USD')
        self.assertEqual(len(viaje.gastos), longitud_inicial_gastos + 1)



if __name__ == '__main__':
    unittest.main()