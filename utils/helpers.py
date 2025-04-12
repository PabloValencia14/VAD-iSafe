"""
Funciones auxiliares comunes para el proyecto,
por ejemplo, manejo de archivos, conversiones de formatos, etc.
"""

def guardar_resultados(datos, ruta):
    """
    Guarda los datos en un archivo en la ruta especificada.
    """
    try:
        with open(ruta, 'w') as f:
            f.write(str(datos))
    except Exception as e:
        print(f"Error al guardar resultados: {e}")

def convertir_formato(data, formato):
    """
    Función de ejemplo para conversión de formatos de datos.
    """
    # Lógica de conversión a implementar
    return data
