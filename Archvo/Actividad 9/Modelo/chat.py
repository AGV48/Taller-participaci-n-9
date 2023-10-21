from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.datos = []

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    partes = linea.strip().split(',')
                    if len(partes) == 7:
                        estacion = partes[0].strip()
                        temperatura = float(partes[4])
                        humedad = float(partes[5])
                        presion = float(partes[6])
                        viento = partes[7].strip().split(',')
                        velocidad_viento = float(viento[0])
                        direccion_viento = viento[1]

                        self.datos.append((temperatura, humedad, presion, velocidad_viento, direccion_viento))

                if not self.datos:
                    raise ValueError("No se encontraron datos válidos en el archivo.")
                
                # Calcular las estadísticas
                temperatura_promedio = sum(x[0] for x in self.datos) / len(self.datos)
                humedad_promedio = sum(x[1] for x in self.datos) / len(self.datos)
                presion_promedio = sum(x[2] for x in self.datos) / len(self.datos)
                velocidad_viento_promedio = sum(x[3] for x in self.datos) / len(self.datos)

                # Calcular dirección predominante del viento
                direcciones = [x[4] for x in self.datos]
                direccion_predominante = self.calcular_direccion_predominante(direcciones)

                return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_predominante)
        except FileNotFoundError:
            raise ValueError("El archivo especificado no se encontró.")

    def calcular_direccion_predominante(self, direcciones):
        # Definir las direcciones y sus equivalentes en grados
        direcciones_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5, "SE": 135,
            "SSE": 157.5, "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5, "W": 270,
            "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        # Convertir las direcciones a grados y calcular el promedio
        grados = [direcciones_grados[d] for d in direcciones]
        promedio_grados = sum(grados) / len(grados)

        # Encontrar la dirección más cercana al promedio en grados
        direcciones_inversas = {v: k for k, v in direcciones_grados.items()}
        direccion_predominante = min(direcciones_grados, key=lambda x: abs(direcciones_grados[x] - promedio_grados))

        return direcciones_inversas[direccion_predominante]

# Ejemplo de uso
archivo_datos = "datos.txt"
datos = DatosMeteorologicos(archivo_datos)
resultado = datos.procesar_datos()

print("Estadísticas meteorológicas:")
print(f"Temperatura promedio: {resultado[0]:.2f}°C")
print(f"Humedad promedio: {resultado[1]:.2f}%")
print(f"Presión promedio: {resultado[2]:.2f} hPa")
print(f"Velocidad del viento promedio: {resultado[3]:.2f} km/h")
print(f"Dirección predominante del viento: {resultado[4]}")
