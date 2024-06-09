Registro de Gastos de Viaje
Esta aplicación permite a los usuarios llevar un registro de sus gastos durante un viaje, tanto dentro del país como en el extranjero. En caso de viajes internacionales, la aplicación convierte automáticamente los gastos a pesos colombianos utilizando una API de conversión de divisas.

Funcionalidades Principales
Registro de Viaje: Los usuarios pueden establecer el lugar de destino, la fecha de inicio, la fecha final y el presupuesto estimado para cada día del viaje.
Registro de Gastos: Durante el viaje, los usuarios pueden registrar la fecha, el valor gastado, el método de pago (efectivo o tarjeta) y el tipo de gasto (transporte, alojamiento, alimentación, entretenimiento o compras).
Seguimiento de Presupuesto: La aplicación muestra la diferencia con el presupuesto diario, que puede ser positiva, cero o negativa en caso de excederse.
Reportes Financieros: Al finalizar el viaje, los usuarios pueden visualizar dos tipos de reportes: el valor gastado cada día, separado por efectivo y tarjeta, y el total; y el valor gastado por tipo de gasto, separado por efectivo y tarjeta, y el total.
Guardado de Información: Toda la información se guarda en un archivo para su posterior consulta.
Implementación de Conversión de Divisas
Se simula el cambio de dólares a pesos colombianos mediante una API que genera un número aleatorio entre 3500 y 4500. Para el cambio de euros, se suma 200 al valor retornado por la misma API.

Pasos del Proceso Personal
Planeación: Revisión de requisitos, creación de un diagrama de clases de análisis y estimación del tiempo para cada fase.
Desarrollo - Diseño: Elaboración de diagramas de clases de diseño y diagramas de secuencia para las funciones principales.
Desarrollo - Código: Implementación del código de acuerdo con el diseño realizado.
Desarrollo - Análisis de Código: Selección y corrección de tres advertencias importantes mostradas por el analizador.
Desarrollo - Pruebas: Diseño y ejecución de pruebas para garantizar el correcto funcionamiento de la aplicación.
Retrospectiva: Escritura de propuestas de mejora basadas en problemas u oportunidades identificados durante el proceso.
Ejemplo de Uso de API de Conversión de Divisas
python
Copiar código
import requests

def uso_api():
    response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
    print(response.json())

if __name__ == '__main__':
    uso_api()
