# Personalizo el saludo según el horario
function ObtenerSaludo {
    $horaActual = Get-Date
    $hora = $horaActual.Hour

    if ($hora -ge 5 -and $hora -lt 12) {
        return "Buenos días"
    } elseif ($hora -ge 12 -and $hora -lt 18) {
        return "Buenas tardes"
    } else {
        return "Buenas noches"
    }
}

# Menú
function MostrarMenu {
    @"
=====================
||      Menú:      ||
=====================
(1) Argparse (con también el help)
(2) Socket
(3) API
(4) Módulo extra no nativo
(5) Módulo instalado por PIP
(6) 3 de las tareas generen reportes como output
(7) 2 deben tener función main
(8) 3 tareas se conecten
(9) Salir
=====================
"@
}

# Función para ejecutar el script de Python
function EjecutarScript {
    param (
        [string]$rutaScript
    )

    Invoke-Item $rutaScript
}

# Función para ejecutar el script de Python con argparse
function EjecutarScriptConArgparse {
    param (
        [string]$rutaScript,
        [string[]]$argsPython
    )

    & python $rutaScript @argsPython
}

# Ejemplo de como usarlo
# EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py"

# Lo pongo a esperar 5 segundos
function EsperarCincoSegundos {
    Start-Sleep -Seconds 2
}

# Muestra el mensaje según el horario
function MostrarMensajeDeHorario {
    $saludo = ObtenerSaludo
    Write-Host $saludo ", ¿Qué deseas hacer hoy pinponero?"
}

# Mostrar el mensaje de acuerdo al horario
MostrarMensajeDeHorario

# Esperar 5 segundos
EsperarCincoSegundos

# Mostrar el menú
MostrarMenu

# Preguntar al pinponero que va a hacer
$opcion = Read-Host "Seleccione una opción del menú (1-9)"

# Ejecutar el script correspondiente a la opción seleccionada
switch ($opcion) {
    "1" { EjecutarScript -rutaScript "C:\Usuario\Documentos\script_con_argparse.py" -argsPython "--opcion1 valor1", "--opcion2 valor2", "--opcion3 valor3", "--opcion4 valor4", "--opcion5 valor5", "--opcion6 valor6", "--opcion7 valor7", "--opcion8 valor8" }
    "2" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "3" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "4" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "5" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "6" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "7" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "8" { EjecutarScript -rutaScript "C:\Usuario\Documentos\Script.py" }
    "9" {exit}
    Default { Write-Host "Opción no válida, por favor elija otra opción pinponero:D" }
}
