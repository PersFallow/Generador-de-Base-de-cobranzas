from collections import Counter
import os

CARPETA_BASES = "bases"

pais = "CL"
anio = "2026"
mes = "05"
dia = "31"
ARCHIVO_SALIDA = f"{pais}_{anio}{mes}{dia}.txt"

def main():
   
    if not os.path.exists(CARPETA_BASES):
        os.makedirs(CARPETA_BASES)
        print(
            f"Se creó la carpeta '{CARPETA_BASES}'. Guarda allí tus archivos .txt y vuelve a ejecutar."
        )
        return
   
    archivos_a_procesar = [
        os.path.join(CARPETA_BASES, f)
        for f in os.listdir(CARPETA_BASES)
        if f.endswith(".txt")
    ]

    if not archivos_a_procesar:
        print(f"No se encontraron archivos .txt para procesar en la carpeta '{CARPETA_BASES}'.")
        return
    print(f"Archivos detectados ({len(archivos_a_procesar)}): {[os.path.basename(a) for a in archivos_a_procesar]}")

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as archivo:
        pass
   
    if validar_cantidad_apariciones_clientes(archivos_a_procesar):
        for archivo in archivos_a_procesar:
            procesar_archivo(archivo)
        print(f"Archivo {ARCHIVO_SALIDA} generado correctamente.")
    else:
        print("Proceso detenido: Error de clientes duplicados.")
   

def validar_cantidad_apariciones_clientes(archivos):
   
    INDICE_COLUMNA_CLIENTE = 1
    MAXIMA_CANTIDAD_APARICIONES = 2

    conteo_clientes = Counter()

    for base in archivos:
        try:
            with open(base, "r", encoding="utf-8") as archivo:
                encabezados = archivo.readline()
                for linea in archivo:
                    columnas = linea.split()
                    if not columnas:
                        continue
                    try:
                        id_cliente = columnas[INDICE_COLUMNA_CLIENTE]
                        conteo_clientes[id_cliente] += 1
                    except IndexError:
                        continue
        except FileNotFoundError:
            print(f"Error: El archivo {base} no existe.")
            return False

    clientes_infractores = {
        cliente: total
        for cliente, total in conteo_clientes.items()
        if total > MAXIMA_CANTIDAD_APARICIONES
    }

    if clientes_infractores:
        print(f"Validación de clientes fallida. Se encontraron {len(clientes_infractores)} clientes que superan las 2 apariciones:")
        for cliente, veces in clientes_infractores.items():
            print(f"  - Cliente '{cliente}': aparece {veces} veces en el archivo.")
        return False
    else:
        print("Validación de clientes exitosa")
        return True

def procesar_archivo(ruta_origen):

    with open(ruta_origen, "r", encoding="utf-8") as archivo, open(
        ARCHIVO_SALIDA, "a", encoding="utf-8"
    ) as base:
        encabezados = archivo.readline()

        for linea in archivo:
            columnas = linea.split()
           
            if not columnas:
                continue

            try:
                agencia = columnas[0]
                cliente = columnas[1]
                desde = formatear_fecha(columnas[2])
                hasta = formatear_fecha(columnas[3])
                deuda = formatear_importe(columnas[4])
                mora = columnas[5]
                campania = columnas[6]

                base.write(f"{agencia}\t{cliente}\t{desde}\t{hasta}\t{deuda}\t{mora}\t{campania}\n")

            except IndexError:
                print(f"Línea omitida por falta de columnas: {linea.strip()}")
                continue

def formatear_fecha(fecha):
    mes, dia, anio = fecha.split("/")
    return f"{anio}-{mes}-{dia}"

def formatear_importe(importe):
    try:
        importe_limpio = importe.replace(",", ".")
        numero = float(importe_limpio)
        return f"{numero:.2f}"
    except ValueError:
        return importe

main()
