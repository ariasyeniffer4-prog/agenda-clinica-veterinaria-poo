# Agenda de una clínica veterinaria

Proyecto académico de consola para practicar programación orientada a objetos en Python. Registra pacientes animales, responsables y veterinarios, programa citas y permite guardar notas breves en la historia clínica.

## Alcance

Esta demostración no diagnostica, recomienda tratamientos, factura ni guarda datos al cerrar el programa. Los minutos de agenda por tipo de paciente y el horario de 08:00 a 18:00 son supuestos didácticos, no recomendaciones clínicas ni políticas confirmadas de una clínica real.

## Requisitos y ejecución

- Python 3.10 o posterior.
- No requiere paquetes externos.

Desde la carpeta raíz:

    python main.py

En Windows:

    py main.py

El programa crea los ejemplos, recorre una colección heterogénea de pacientes y muestra casos normales y excepcionales.

## Estructura

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

## Clases

- Animal es abstracta y define los datos y operaciones comunes.
- Perro, Gato y Ave heredan de Animal y sobrescriben resumen() y duracion_atencion().
- Responsable guarda datos de contacto y la relación con sus animales.
- HistoriaClinica administra notas breves; cada Animal contiene una.
- Veterinario administra citas y detecta cruces de horario.
- Cita relaciona paciente, responsable y veterinario.
- Clinica registra pacientes y coordina la programación.

## Excepciones personalizadas

- PacienteNoRegistradoError: se intenta citar un animal que no está en el registro de la clínica.
- CitaOcupadaError: el intervalo se cruza con otra cita del veterinario.
- HorarioInvalidoError: la cita queda fuera del horario de atención.

El programa principal captura estas excepciones y continúa con las demostraciones.

## Verificación de referencia

ChatGPT ejecutó main.py con Python 3.12.14 en el entorno de trabajo; la versión final terminó con código 0, mostró dos citas aceptadas, capturó los tres errores de dominio y continuó hasta el mensaje final. La salida inicial permitió corregir «1 años» por «1 año». No se ejecutó una suite automatizada. La ejecución y sus límites se describen en Documento_Decisiones_Diseno.md.

## Repositorio y commits

- Repositorio público: https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo
- Commit inicial de documentación y punto de entrada (ff53194): https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/ff53194b4be827b68f15127c08ad6232db82898c
- Commit de modelos POO (edc3ffb): https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/edc3ffb35313cad01bb73589488e13545f7f6544

## Uso de IA

ChatGPT se utilizó para interpretar los requisitos, proponer y delimitar el diseño, redactar y ajustar código y documentación, revisar la salida y corregir la forma singular/plural de la edad. La autora debe comprender y poder explicar el resultado; el documento de decisiones detalla las propuestas conservadas y ajustadas.
