# Personalizo el saludo según el horario

Set-ExecutionPolicy -ExecutionPolicy Bypass
function ObtenerSaludo {
    $horaActual = Get-Date
    $hora = $horaActual.Hour

    if ($hora -ge 5 -and $hora -lt 12) {
        return "Buenos dÃƒÂ­as"
    } elseif ($hora -ge 12 -and $hora -lt 18) {
        return "Buenas tardes"
    } else {
        return "Buenas noches"
    }
}

# Menu
function MainMenu {
    @"
=====================
||      Menu:      ||
=====================
(1) Descargar imagen random, limpia metadatos, encripta el mensaje en la imagen
(2) Desencriptar mensaje y crear reporte
(3) Escaneo de puertos
(4) Obtener imagenes de una web
(5) Checar si API es maliciosa
(6) Salir
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
    Write-Host $saludo ", Que deseas hacer hoy pinponero?"
}

# Mostrar el mensaje de acuerdo al horario
MostrarMensajeDeHorario

# Esperar 2 segundos
EsperarDosSegundos

# Mostrar el menú
MainMenu

# Preguntar al pinponero que va a hacer

# Arrays/Lista con los nombres de los programas
$rutaCodigos = @("imagenAPI.py","imagenFernet.py","transmision.py","escaneopuertos.py","webscraping.py","ConsultaDeApis.py")

# Ejecutar el script correspondiente a la opción seleccionada
while ($true)
{
    $argsPython = @()
    $opcion = Read-Host "Seleccione una opción del menú (1-6)"
    switch ($opcion) {
        "1" {
            try {
                $imagen = EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[0])
                $mg = Read-Host "Escriba el mensaje que se encriptará"
                $argsPython = "-m","encriptar","-p",$imagen,"-me", $mg
                $e = EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[1]) -argsPython $argsPython
            } catch {
                Write-Host "Error: No se pudo obtener la imagen de la API."
            }
        }
        "2" {
            if (-not $imagen) {
                Write-Host "Error: No se ha descargado ninguna imagen. Por favor, seleccione la opción 1 primero."
                break
            }
            $argsPython = "-m","desencriptar","-p",$imagen, "-me", $e
            echo "Este es el código decifrado:" @(EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[1]) -argsPython $argsPython)
        }
        "3" {#
            $ip = Read-Host "Escriba una IP para escanear puertos populares"
            if ($web -eq ""){
            $argsPython = "--host","2.2.2.2"
            EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[3])
            }else{
            $argsPython = "--host",$ip
            EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[3]) -argsPython $argsPython
        }
        }
        "4" {
            $web = Read-Host "Escriba una página para verificar si es segura, déjela en blanco para usar la página por defecto"
            if ($web -eq ""){
            EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[4])
            }else{
            $argsPython = "--web",$web
            EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[4]) -argsPython $argsPython
            }
        }
        
        "5" {
            $ip = Read-Host "Escriba una IP para saber si es segura"
            $argsPython = "--ip",$ip
            if ($ip -eq ""){
            $argsPython = "--ip","1.1.1.1"
            EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[5])
            }else{

            EjecutarScriptConArgparse -rutaScript @(Join-Path -Path $PWD -ChildPath $rutaCodigos[5]) -argsPython $argsPython
            }
        }
        "6" {exit}
        Default { Write-Host "Opción no válida, por favor elija otra opción." }
    }
}
