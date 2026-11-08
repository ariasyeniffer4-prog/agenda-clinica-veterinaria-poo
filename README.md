# Agenda de una clínica veterinaria

Proyecto académico de consola para practicar programación orientada a objetos en Python. El sistema registra pacientes animales, responsables y veterinarios, y programa citas con validaciones sencillas. También permite consultar y agregar notas breves a la historia clínica de un paciente.

## Alcance

Esta demostración no diagnostica, recomienda tratamientos, factura ni guarda datos al cerrar el programa. Los minutos asignados por tipo de paciente son valores didácticos para mostrar comportamiento polimórfico; no son recomendaciones clínicas. El horario ilustrativo es de 08:00 a 18:00.

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

El programa crea ejemplos, recorre una colección heterogénea de pacientes y presenta casos normales y excepcionales. Para ejecutarlo, use `py main.py` en Windows o `python main.py` en otros entornos.

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

- Resultado observado: el programa terminó con código 0, mostró dos citas aceptadas, capturó los tres errores de dominio y continuó hasta el mensaje final.
- También se comprobaron manualmente la validación estricta del booleano de `Gato` y el rechazo de campos obligatorios vacíos.
- La salida de ejecución y estas comprobaciones están en `evidencias/ejecucion_programa.txt`.

## Repositorio y participación

- URL del repositorio público: https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo
- Commit de documentación y punto de entrada: [ff53194](https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/ff53194b4be827b68f15127c08ad6232db82898c)
- Commit de inicialización del paquete: [fc6952e](https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/fc6952eb1b4864b8e767191cbc48e98b0769dda7)
- Commit de excepciones: [18816f0](https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/18816f068039f0bc68e76151e295eb9efeec6678)
- Commit de gestión de citas: [e1fa9a3](https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/e1fa9a3acf0a15e92f0419f23f3db034a1ea72a2)
- Commit de modelos POO: [edc3ffb](https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/edc3ffb35313cad01bb73589488e13545f7f6544)
