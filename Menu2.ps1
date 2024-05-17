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
(2) Escaneo de puertos
(3) Imagen API
(4) Imagen Fernet
(5) Metadatos de la Imagen
(6) Trasmisión
(7) Webscrapping
(8) 3 tareas se conecten
(9) Salir
=====================
"@
}

# Función para ejecutar el script de Python con argparse
function EjecutarScriptConArgparse {
    param (
        [string]$rutaScript,
        [string[]]$argsPython
    )

    & python $rutaScript @argsPython
}

# Lo pongo a esperar 2 segundos
function EsperarDosSegundos {
    Start-Sleep -Seconds 2
}

# Muestra el mensaje según el horario
function MostrarMensajeDeHorario {
    $saludo = ObtenerSaludo
    Write-Host $saludo ", ¿Qué deseas hacer hoy pinponero?"
}

# Mostrar el mensaje de acuerdo al horario
MostrarMensajeDeHorario

# Esperar 2 segundos
EsperarDosSegundos

# Mostrar el menú
MostrarMenu

# Preguntar al pinponero que va a hacer
$opcion = Read-Host "Seleccione una opción del menú (1-9)"

# Arrays/Lista con los nombres de los programas
$rutaCodigos = @("ScriptConArgparse","escaneopuertos.py","imagenAPI.py","imagenFernet.py","metadatos_imag.py","trasmision.py","webscrappy.py")

# Ejecutar el script correspondiente a la opción seleccionada
switch ($opcion) {
    "1" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "2" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "3" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "4" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "5" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "6" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "7" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "8" {
        $argsPython = "--opcion1","valor1","--opcion2","valor2","--opcion3","valor3","--opcion4","valor4","--opcion5","valor5","--opcion6","valor6","--opcion7","valor7","--opcion8","valor8"
        EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0]) -argsPython $argsPython
    }
    "9" {exit}
    Default { Write-Host "Opción no válida, por favor elija otra opción." }
}
