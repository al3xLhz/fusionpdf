import os
import sys
from PyPDF2 import PdfMerger


def fusion_pdf(archivos_pdf):
    """
    Fusiona varios archivos PDF en el orden especificado y guarda el resultado con el nombre de la carpeta actual
    """

    if len(archivos_pdf) < 2:
        print("Error: Debes proporcionar al menos dos archivos PDF para fusionar")
        print("Uso: fusionpdf archivo1.pdf archivo2.pdf [archivo3.pdf...]")
        return

    #Verificar que todos los archivos existen
    for archivo in archivos_pdf:
        if not os.path.exists(archivo):
            print(f"Error: El archivo '{archivo}' no existe")
            return
        if not archivo.lower().endswith('.pdf'):
            print(f"Error: '{archivo}' no parece ser un archivo PDF")
            return

    #Obtener el nombre de la carpeta actual
    nombre_carpeta = os.path.basename(os.getcwd())
    nombre_archivo_salida = f"{nombre_carpeta}.pdf"

    #Crear un objeto PdfMerger
    merger = PdfMerger()

    try:
        #Agregar cada archivo PDF al merger
        for archivo in archivos_pdf:
            print(f"Agregando: {archivo}...")
            merger.append(archivo)

        #Guardar el archivo fusionado
        merger.write(nombre_archivo_salida)
        merger.close()
        print(f"Archivos fusionado exitosamente en '{nombre_archivo_salida}'")
    except Exception as e:
        print(f"Error al fusionar los PDFs: {e}")
        return


if __name__ == "__main__":
    #Obtener los nombres de los archivos de los argumentos de linea de comandos
    if len(sys.argv) < 2:
        print("Error: No se proporcionaron archivos para fusionar")
        print("Uso: fusionpdf archivo1.pdf archivo2.pdf [archivo3.pdf...]")
    else:
        fusion_pdf(sys.argv[1:])