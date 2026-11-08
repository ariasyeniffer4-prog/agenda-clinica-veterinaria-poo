# Agenda de una clínica veterinaria

Proyecto académico de consola para practicar programación orientada a objetos en Python. El sistema registra pacientes animales, responsables y veterinarios, y programa citas con validaciones sencillas. También permite consultar y agregar notas breves a la historia clínica.

## Alcance

Esta demostración no diagnostica, recomienda tratamientos, factura ni guarda datos al cerrar el programa. Los minutos asignados por tipo de paciente son valores didácticos para mostrar comportamiento polimórfico; no son recomendaciones clínicas. El horario ilustrativo es de 08:00 a 18:00.

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

Para ejecutarlo, use `py main.py` en Windows o `python main.py` en otros entornos.

## Estructura

```text
proyecto_clinica_veterinaria/
├── main.py
├── README.md
├── Diagrama_UML.md
├── Documento_Decisiones_Diseno.md
├── evidencias/
│   └── ejecucion_programa.txt
└── src/
    ├── __init__.py
    ├── clinica.py
    ├── excepciones.py
    └── modelos.py
```

## Clases y responsabilidades

- `Animal` define datos y operaciones comunes; es abstracta.
- `Perro`, `Gato` y `Ave` heredan de `Animal` y sobrescriben `resumen()` y `duracion_atencion()`.
- `Responsable` mantiene sus datos de contacto y animales asociados.
- `HistoriaClinica` administra entradas breves; cada animal contiene su historial.
- `Veterinario` administra citas y detecta cruces de horario.
- `Cita` relaciona paciente, responsable y veterinario.
- `Clinica` registra pacientes y coordina la programación.

## Excepciones del dominio

- `PacienteNoRegistradoError`: se intenta citar un paciente no registrado.
- `CitaOcupadaError`: el intervalo se cruza con otra cita del veterinario.
- `HorarioInvalidoError`: la cita queda fuera del horario configurado.

El programa principal captura estas excepciones y continúa con las demostraciones.

## Verificación de referencia

- La ejecución final terminó con código 0, mostró dos citas aceptadas y capturó los tres errores de dominio, continuando hasta el mensaje final.
- En el entorno de verificación, `py.exe` no pudo iniciar; el mismo programa se ejecutó con Python 3.14.4 mediante su ruta absoluta.
- Se comprobaron manualmente la validación estricta de `Gato` y el rechazo de campos obligatorios vacíos.
- La salida y las comprobaciones están en `evidencias/ejecucion_programa.txt`.

## Repositorio

https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo

## Uso de IA

Utilicé ChatGPT para estructurar el código y la documentación; ajusté `Gato` para aceptar solo `True` y `False`, en lugar de convertir cualquier valor automáticamente.
