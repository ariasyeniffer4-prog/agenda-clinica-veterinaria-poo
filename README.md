# Agenda de una clínica veterinaria

Proyecto académico de consola para practicar programación orientada a objetos en Python. El sistema registra pacientes animales, responsables y veterinarios, y programa citas con validaciones sencillas. También permite consultar y agregar notas breves a la historia clínica de un paciente.

## Alcance

Esta demostración no diagnostica, recomienda tratamientos, factura ni guarda datos al cerrar el programa. Los minutos asignados por especie y características son valores didácticos para mostrar comportamiento polimórfico; no son recomendaciones clínicas. El horario ilustrativo es de 08:00 a 18:00.

## Requisitos y ejecución

- Python 3.10 o posterior.
- No requiere paquetes externos.

Desde la carpeta raíz:

    python main.py

En Windows:

    py main.py

El programa crea ejemplos, recorre una colección heterogénea de pacientes y presenta casos normales y excepcionales. La versión actual se ejecutó con Python 3.12.14 y terminó correctamente. En `Documento_Decisiones_Diseno.md` se describe esa verificación asistida; debo revisar y comprender el código antes de entregarlo.

## Estructura

```
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

- Entorno: Python 3.12.14 incluido en el entorno de trabajo de ChatGPT.
- Resultado observado: ejecución final de `main.py` con código 0; dos citas aceptadas; tres errores de dominio capturados; mensaje final impreso.
- Corrección tras la primera ejecución: el resumen de edad ahora presenta «1 año» en singular.
- No se ejecutó una suite automatizada. Esta fue una verificación asistida y no la presento como una ejecución personal mía.

## Repositorio y participación

- URL del repositorio público: https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo
- Commits relacionados con la actividad: disponibles en el historial del repositorio.

## Uso de IA

Utilicé ChatGPT como apoyo para proponer y revisar borradores de código y documentación. Revisé y ajusté el resultado para esta actividad; debo comprender y poder explicar lo que entregue.
