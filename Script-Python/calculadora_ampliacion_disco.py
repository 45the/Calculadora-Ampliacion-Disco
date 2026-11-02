#!/usr/bin/env python3
# =============================================================================
# Descripción : Calculadora de ampliación de disco (Windows / Linux)
# Versión     : 1.0
# Autor       : Angel Mora Llamozas
# =============================================================================

import os
import sys
 
# Colores ANSI
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
 
# Habilitamos el procesamiento de secuencia de colores ANSI para la consola de Windows
if os.name == "nt":
    os.system("")

def imprimir(texto="", color=""):
    # Imprime un texto con color opcional
    print(f"{color}{texto}{RESET}" if color else texto)

def leer_numero(mensaje):
    # Solicita un número y repite la pregunta hasta que sea válido (acepta coma decimal)
    while True:
        valor = input(f"{mensaje}: ").strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            imprimir("[ERROR] Ingrese un valor numérico válido.", RED)

def formatear(numero):
    # Nos mostrara el número sin ceros innecesarios (e.j 50.0 -> 50, 12.2 -> 12.2)
    return f"{numero:g}"

def main():
    
    imprimir("===================================================================", CYAN)
    imprimir("   CALCULADORA DE AMPLIACIÓN DE DISCO (WINDOWS / LINUX)   ", CYAN)
    imprimir("===================================================================\n", CYAN)
 
    # 1. Solicita los datos respecto al consumo de un disco
    tamano_actual = leer_numero("Ingrese el tamaño actual del disco (ej. 12.2 o 50)")
    unidad_medida = input("Unidad de medida (GB / TB): ").strip()
    espacio_libre = leer_numero("Ingrese el espacio LIBRE actual (ej. 35.4 GB -> 0.0354 en TB)")
    porcentaje_uso_actual = leer_numero("Ingrese el % de USO actual (ej. 99)")
 
    # 2. Espacio ocupado
    espacio_usado = tamano_actual - espacio_libre
 
    imprimir("\n-------------------------------------------------------------------", YELLOW)
    imprimir(" RESUMEN ACTUAL", YELLOW)
    imprimir("-------------------------------------------------------------------", YELLOW)
    print(f"Tamaño Total Actual : {formatear(tamano_actual)}{unidad_medida}")
    print(f"Espacio Usado       : {formatear(espacio_usado)}{unidad_medida}")
    print(f"Espacio Libre       : {formatear(espacio_libre)}{unidad_medida}")
    print(f"Uso Actual          : {formatear(porcentaje_uso_actual)} %")
 
    # 3. Objetivo de espacio a liberar en el disco
    imprimir("\n-------------------------------------------------------------------", YELLOW)
    imprimir(" OBJETIVO DE OPTIMIZACIÓN", YELLOW)
    imprimir("-------------------------------------------------------------------", YELLOW)
    pct_libre_deseado = leer_numero("Ingrese el % de ESPACIO LIBRE que desea tener (ej. 10, 15, 20)")
 
    if pct_libre_deseado <= 0 or pct_libre_deseado >= 100:
        imprimir("\n[ERROR] El porcentaje libre deseado debe ser entre 1 y 99.", RED)
        sys.exit(1)
 
    # 4. Cálculo de la cantidad de disco a aumentar, nuevo tamaño y nuevo espacio libre
    pct_libre_decimal = pct_libre_deseado / 100
    nuevo_tamano_total = espacio_usado / (1 - pct_libre_decimal)
    disco_aumentar = nuevo_tamano_total - tamano_actual
    nuevo_espacio_libre = nuevo_tamano_total - espacio_usado
 
    # 5. Resultados obtenidos en base a los cálculos del paso 4
    imprimir("\n===================================================================", GREEN)
    imprimir(" RESULTADOS Y RECOMENDACIÓN", GREEN)
    imprimir("===================================================================", GREEN)
    print(
        f"Para lograr un {formatear(pct_libre_deseado)}% de espacio libre "
        f"(Uso al {formatear(100 - pct_libre_deseado)}%):"
    )
 
    if disco_aumentar > 0:
        imprimir(f"\n -> DISCO A AUMENTAR     : {disco_aumentar:,.2f} {unidad_medida}", CYAN)
        print(f" -> NUEVO TAMAÑO TOTAL    : {nuevo_tamano_total:,.2f} {unidad_medida}")
        print(f" -> NUEVO ESPACIO LIBRE   : {nuevo_espacio_libre:,.2f} {unidad_medida}")
    else:
        imprimir("\nEl disco ya cumple con el espacio libre deseado.", YELLOW)
    imprimir("===================================================================\n", GREEN)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        imprimir("\n\nOperación cancelada por el usuario.", YELLOW)
        sys.exit(0)
