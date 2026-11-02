# =============================================================================
# Descripción : Calculadora de ampliación de disco (Windows)
# Versión     : 1.0
# Autor       : Angel Mora Llamozas
# =============================================================================

#Clear-Host
Write-Host "===================================================================" -ForegroundColor Cyan
Write-Host "   CALCULADORA DE AMPLIACIÓN DE DISCO (WINDOWS)   " -ForegroundColor Cyan
Write-Host "===================================================================`n" -ForegroundColor Cyan

# 1. Entrada de datos respecto al consumo de un disco 
$tamanoActual = Read-Host "Ingrese el tamaño actual del disco (ej. 12.2 o 50)" ;
$unidadMedida = Read-Host "Unidad de medida (GB / TB)" ;
$espacioLibre = Read-Host "Ingrese el espacio LIBRE actual (ej. 35.4 GB -> 0.0354 en TB)" ;
$porcentajeUsoActual = Read-Host "Ingrese el % de USO actual (ej. 99)" ;

# Convertimos a formato numérico
$tamanoActual = [double]$tamanoActual ;
$espacioLibre = [double]$espacioLibre ;
$porcentajeUsoActual = [double]$porcentajeUsoActual ;

# 2. Espacio ocupado
$espacioUsado = $tamanoActual - $espacioLibre ;

Write-Host "`n-------------------------------------------------------------------" -ForegroundColor Yellow
Write-Host " RESUMEN ACTUAL" -ForegroundColor Yellow
Write-Host "-------------------------------------------------------------------" -ForegroundColor Yellow
Write-Host "Tamaño Total Actual : $tamanoActual$unidadMedida" ;
Write-Host "Espacio Usado       : $espacioUsado$unidadMedida" ;
Write-Host "Espacio Libre       : $espacioLibre$unidadMedida" ;
Write-Host "Uso Actual          : $porcentajeUsoActual %" ;

# 3. Objetivo de espacio a liberar en el disco
Write-Host "`n-------------------------------------------------------------------" -ForegroundColor Yellow
Write-Host " OBJETIVO DE OPTIMIZACIÓN" -ForegroundColor Yellow
Write-Host "-------------------------------------------------------------------" -ForegroundColor Yellow
$pctLibreDeseado = Read-Host "Ingrese el % de ESPACIO LIBRE que desea tener (ej. 10, 15, 20)" ;
$pctLibreDeseado = [double]$pctLibreDeseado ;

if ($pctLibreDeseado -le 0 -or $pctLibreDeseado -ge 100) {
    Write-Host "`n[ERROR] El porcentaje libre deseado debe ser entre 1 y 99." -ForegroundColor Red ;
    exit ;
}

# 4. Cálculamos la cantidad de disco a aumentar, nuevo tamaño del disco y el nuevo espacio libre 
$pctLibreDecimal =$pctLibreDeseado / 100 ;
$nuevoTamanoTotal =$espacioUsado / (1 - $pctLibreDecimal) ;$discoAumentar = $nuevoTamanoTotal -$tamanoActual ;
$nuevoEspacioLibre = $nuevoTamanoTotal -$espacioUsado ;

# 5. Resultados obstenidos en base a los calculos en el paso 4
Write-Host "`n===================================================================" -ForegroundColor Green
Write-Host " RESULTADOS Y RECOMENDACIÓN" -ForegroundColor Green
Write-Host "===================================================================" -ForegroundColor Green
Write-Host ("Para lograr un {0}% de espacio libre (Uso al {1}%):" -f $pctLibreDeseado, (100 - $pctLibreDeseado)) ;

if ($discoAumentar -gt 0) {
    Write-Host ("`n -> DISCO A AUMENTAR     : {0:N2} {1}" -f $discoAumentar,$unidadMedida) -ForegroundColor Cyan ;
    Write-Host (" -> NUEVO TAMAÑO TOTAL    : {0:N2} {1}" -f $nuevoTamanoTotal,$unidadMedida) ;
    Write-Host (" -> NUEVO ESPACIO LIBRE   : {0:N2} {1}" -f $nuevoEspacioLibre,$unidadMedida) ;
} else {
    Write-Host "`nEl disco ya cumple con el espacio libre deseado." -ForegroundColor Yellow ;
}
Write-Host "===================================================================`n" -ForegroundColor Green
