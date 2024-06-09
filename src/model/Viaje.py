import json
import os
from datetime import datetime
from tkinter import filedialog
import tkinter as tk
from src.model.ConversorDivisas import ConversorDivisas
from src.model.Gasto import Gasto


class Viaje:
    def __init__(self, destino, fecha_inicio, fecha_final, presupuesto_diario):
        """
        Inicializa un objeto Viaje.

        Args:
            destino (str): El destino del viaje.
            fecha_inicio (str): La fecha de inicio del viaje en formato 'YYYY-MM-DD'.
            fecha_final (str): La fecha final del viaje en formato 'YYYY-MM-DD'.
            presupuesto_diario (float): El presupuesto diario en pesos colombianos (COP).
        """
        self.destino = destino
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        self.fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d").date()
        self.presupuesto_diario = presupuesto_diario
        self.gastos = []

    def registrar_gasto(self, fecha, valor, metodo_pago, tipo_gasto, moneda):
        """
        Registra un gasto en el viaje.

        Args:
            fecha (str): La fecha del gasto en formato 'YYYY-MM-DD'.
            valor (float): El valor del gasto en la moneda original.
            metodo_pago (str): El método de pago ('efectivo' o 'tarjeta').
            tipo_gasto (str): El tipo de gasto (transporte/alojamiento/alimentación/entretenimiento/compras).
            moneda (str): La moneda del gasto ('USD' o 'EUR').
        """

        fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        gasto = Gasto(fecha, valor, metodo_pago, tipo_gasto, moneda)
        self.gastos.append(gasto)

    def obtener_reporte_diario(self):
        """
        Obtiene un reporte diario de los gastos.

        Returns:
            dict: Un diccionario con los gastos diarios, separados por método de pago y el total.
        """
        reporte = {}
        for gasto in self.gastos:
            if gasto.fecha not in reporte:
                reporte[gasto.fecha] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            reporte[gasto.fecha][gasto.metodo_pago] += gasto.valor_en_cop
            reporte[gasto.fecha]['total'] += gasto.valor_en_cop

        return reporte

    def obtener_reporte_por_tipo(self):
        """
        Obtiene un reporte de los gastos por tipo.

        Returns:
            dict: Un diccionario con los gastos por tipo, separados por método de pago y el total.
        """
        reporte = {}
        for gasto in self.gastos:
            if gasto.tipo_gasto not in reporte:
                reporte[gasto.tipo_gasto] = {'efectivo': 0, 'tarjeta': 0, 'total': 0}
            reporte[gasto.tipo_gasto][gasto.metodo_pago] += gasto.valor_en_cop
            reporte[gasto.tipo_gasto]['total'] += gasto.valor_en_cop

        return reporte

    import os
    import json

    def guardar_en_archivo(self, filename):
        """
        Guarda los datos del viaje en un archivo JSON.

        Args:
            filename (str): El nombre del archivo donde se guardarán los datos.
        """
        if not os.path.exists("docs"):
            os.makedirs("docs")

        filename += ".json"
        tasa = ConversorDivisas.obtener_tasa()  # variable para que se guarde la tasa con la que se trabajó
        data = {
            'destino': self.destino,
            'fecha_inicio': self.fecha_inicio.strftime("%Y-%m-%d"),
            'fecha_final': self.fecha_final.strftime("%Y-%m-%d"),
            'presupuesto_diario': self.presupuesto_diario,
            "tasa_conversion": tasa,
            'gastos': [gasto.to_dict() for gasto in self.gastos]
        }
        filepath = os.path.join("docs", filename)  # ruta completa del archivo
        with open(filepath, 'w') as file:  # se abre el archivo con la ruta completa
            json.dump(data, file, indent=4)

    @staticmethod
    def cargar_de_archivo():
        """
        Carga los datos de un viaje desde un archivo JSON seleccionado por el usuario.

        Returns:
            Viaje: El objeto Viaje cargado desde el archivo.
        """
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        filename = filedialog.askopenfilename(
            title="Seleccione el archivo de viaje",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        if not filename:
            print("No se seleccionó ningún archivo.")
            return None

        with open(filename, 'r') as file:
            data = json.load(file)
            viaje = Viaje(data['destino'], data['fecha_inicio'], data['fecha_final'], data['presupuesto_diario'])
            viaje.gastos = [Gasto.from_dict(gasto_data) for gasto_data in data['gastos']]
            return viaje
