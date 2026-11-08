# Agenda de una clínica veterinaria

Proyecto académico de consola para practicar programación orientada a objetos en Python. El sistema registra pacientes animales, responsables y veterinarios, y programa citas con validaciones sencillas. También permite consultar y agregar notas breves a la historia clínica de un paciente.

## Alcance

Esta demostración no diagnostica, recomienda tratamientos, factura ni guarda datos al cerrar el programa. Los minutos asignados por especie y características son valores didácticos para mostrar comportamiento polimórfico; no son recomendaciones clínicas. El horario ilustrativo es de 08:00 a 18:00.

## Requisitos

- Python 3.10 o posterior.
- No requiere paquetes externos.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

En Windows también se puede usar:

```powershell
py main.py
```

El programa crea ejemplos, recorre una colección heterogénea de pacientes y presenta casos normales y excepcionales. ChatGPT ejecutó la versión actual con Python 3.12.14 y observó que terminó correctamente, incluyó los tres casos excepcionales y continuó hasta el final. La autora debe revisar el código y puede repetir la ejecución en su propio entorno; consulte `Documento_Decisiones_Diseno.md` para distinguir esa evidencia asistida de una verificación personal.

## Estructura

```text
proyecto_clinica_veterinaria/
├── main.py
├── README.md
├── Diagrama_UML.md
├── Documento_Decisiones_Diseno.md
└── src/
    ├── __init__.py
    ├── clinica.py
    ├── excepciones.py
    └── modelos.py
```

## Clases y responsabilidades

- `Animal` define la interfaz y los datos comunes de un paciente; es abstracta.
- `Perro`, `Gato` y `Ave` especializan a `Animal`. Cada clase sobrescribe `resumen()` y `duracion_atencion()`.
- `Responsable` mantiene datos de contacto y la relación con sus animales.
- `HistoriaClinica` administra entradas breves. Cada `Animal` crea y contiene su propio historial.
- `Veterinario` administra sus citas y detecta cruces de horario.
- `Cita` relaciona paciente, responsable y veterinario, además de la fecha, duración y estado.
- `Clinica` registra pacientes y coordina la programación.

## Excepciones del dominio

- `PacienteNoRegistradoError`: la clínica rechaza una cita para un paciente que no figura en sus registros.
- `CitaOcupadaError`: el veterinario rechaza una cita cuyo intervalo se cruza con otra.
- `HorarioInvalidoError`: `Cita` rechaza una hora de inicio fuera del horario configurado.

El programa principal captura esas excepciones y sigue con las demostraciones posteriores.

## Verificación de referencia

- Entorno de esta verificación: Python 3.12.14 incluido en el entorno de trabajo de ChatGPT.
- Resultado observado: ejecución final de `main.py` con código 0; dos citas aceptadas; tres errores de dominio capturados; mensaje final impreso.
- Corrección realizada tras la primera ejecución: el resumen de edad ahora presenta «1 año» en singular.
- No se ejecutó una suite automatizada. Esta verificación asistida no se presenta como ejecución personal de la autora.

## Repositorio y participación

- URL del repositorio de este proyecto: `[agregar cuando se cree o se confirme]`
- Commit de la autora relacionado con esta actividad: `[agregar el enlace o identificador real cuando exista]`

## Uso de IA

Durante la preparación de esta propuesta se utilizó ChatGPT para ordenar requisitos, proponer y delimitar el diseño, redactar código y documentación, revisar la salida y corregir la forma singular/plural de la edad. La autora debe comprender y poder explicar el resultado; el detalle de las propuestas conservadas y ajustadas está en `Documento_Decisiones_Diseno.md`.
