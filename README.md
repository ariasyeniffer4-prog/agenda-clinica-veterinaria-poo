# Agenda de una clínica veterinaria

Proyecto académico de consola para practicar programación orientada a objetos en Python. El sistema registra pacientes animales, responsables y veterinarios, programa citas con validaciones sencillas y permite consultar y agregar notas breves a la historia clínica.

## Alcance

Esta demostración no diagnostica, recomienda tratamientos, factura ni guarda datos al cerrar el programa. Los minutos asignados por tipo de paciente son valores didácticos para mostrar polimorfismo; no son recomendaciones clínicas. El horario ilustrativo es de 08:00 a 18:00.

## Requisitos y ejecución

- Python 3.10 o posterior.
- No requiere paquetes externos.

Desde la carpeta raíz:

```bash
python main.py
```

En Windows:

```powershell
py main.py
```

El programa crea ejemplos, recorre una colección heterogénea de pacientes y presenta casos normales y excepcionales. La versión actual se ejecutó con Python 3.12.14 y terminó correctamente. En `Documento_Decisiones_Diseno.md` se describen los detalles de la verificación; debo revisar y comprender el código antes de entregarlo.

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
- `Perro`, `Gato` y `Ave` especializan a `Animal` y sobrescriben `resumen()` y `duracion_atencion()`.
- `Responsable` mantiene datos de contacto y la relación con sus animales.
- `HistoriaClinica` administra entradas breves; cada animal contiene su propio historial.
- `Veterinario` administra sus citas y detecta cruces de horario.
- `Cita` relaciona paciente, responsable y veterinario.
- `Clinica` registra pacientes y coordina la programación.

## Excepciones del dominio

- `PacienteNoRegistradoError`: se intenta citar un paciente que no está registrado.
- `CitaOcupadaError`: el intervalo se cruza con otra cita del veterinario.
- `HorarioInvalidoError`: la cita empieza fuera del horario configurado.

El programa principal captura las excepciones y continúa con las demostraciones.

## Verificación de referencia

- Entorno de referencia: Python 3.12.14.
- Resultado observado: ejecución final de `main.py` con código 0, dos citas aceptadas, tres errores de dominio capturados y mensaje final impreso.
- Corrección tras la primera ejecución: el resumen de edad ahora presenta «1 año» en singular.

## Repositorio y participación

- URL del repositorio público: https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo
- Commits relacionados con la actividad: disponibles en el historial del repositorio.

## Uso de IA

Utilicé ChatGPT como apoyo para proponer y revisar borradores de código y documentación. Revisé y ajusté el resultado para esta actividad; debo comprender y poder explicar lo que entregue.
