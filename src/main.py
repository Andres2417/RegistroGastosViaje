from model.Viaje import Viaje

def main():
    while True:
        print("\n1. Registrar viaje")
        print("2. Registrar gasto")
        print("3. Ver reporte diario")
        print("4. Ver reporte por tipo de gasto")
        print("5. Guardar viaje en archivo")
        print("6. Cargar viaje de archivo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            destino = input("Ingrese el destino del viaje: ")
            fecha_inicio = input("Ingrese la fecha de inicio del viaje (YYYY-MM-DD): ")
            fecha_final = input("Ingrese la fecha final del viaje (YYYY-MM-DD): ")
            presupuesto_diario = float(input("Ingrese el presupuesto diario en COP: "))

            viaje = Viaje(destino, fecha_inicio, fecha_final, presupuesto_diario)

        elif opcion == '2':
            fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
            valor = float(input("Ingrese el valor del gasto: "))
            metodo_pago = input("Ingrese el método de pago (efectivo/tarjeta): ")
            tipo_gasto = input(
                "Ingrese el tipo de gasto (transporte/alojamiento/alimentación/entretenimiento/compras): ")
            moneda = input("Ingrese la moneda del gasto (USD/EUR): ")
            viaje.registrar_gasto(fecha, valor, metodo_pago, tipo_gasto, moneda)
        elif opcion == '3':
            reporte_diario = viaje.obtener_reporte_diario()
            for fecha, datos in reporte_diario.items():
                print(f"Fecha: {fecha}")
                print(f"  Efectivo: {datos['efectivo']} COP")
                print(f"  Tarjeta: {datos['tarjeta']} COP")
                print(f"  Total: {datos['total']} COP")
        elif opcion == '4':
            reporte_tipo = viaje.obtener_reporte_por_tipo()
            for tipo, datos in reporte_tipo.items():
                print(f"Tipo de gasto: {tipo}")
                print(f"  Efectivo: {datos['efectivo']} COP")
                print(f"  Tarjeta: {datos['tarjeta']} COP")
                print(f"  Total: {datos['total']} COP")
        elif opcion == '5':
            filename = input("Ingrese el nombre del archivo para guardar: ")
            viaje.guardar_en_archivo(filename)
            print("Viaje guardado.")
        elif opcion == '6':
            viaje_cargado = Viaje.cargar_de_archivo()
            if viaje_cargado:
                viaje = viaje_cargado
                print("Viaje cargado.")
        elif opcion == '7':
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()