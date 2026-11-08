# Documento de Decisiones de Diseño

## Portada

**Proyecto:** Agenda de una clínica veterinaria  
**Asignatura:** Programación I 
**Integrante:** Yeniffer Fernanda Arias Ordoñez  
**Docente:** Natalia Marcela Castellanos Gomez  
**Fecha de entrega:** 08/11/2026  
**Repositorio:** `[agregar URL cuando esté creado o confirmado]`

## Introducción

Este documento explica el diseño de un programa de consola para organizar el registro de pacientes animales y la programación de citas en una clínica veterinaria. El alcance es deliberadamente acotado: registra animales y responsables, relaciona cada cita con un veterinario y permite guardar notas breves en el historial de cada paciente. No diagnostica, recomienda tratamientos ni conserva la información entre ejecuciones.

La clínica veterinaria fue elegida por Yeniffer después de descartar el contexto de gestión académica trabajado previamente. El sistema ofrece un escenario concreto para explicar abstracción, herencia, encapsulamiento, polimorfismo, composición y excepciones propias del dominio.

## Descripción general

El punto de entrada es `main.py`. Allí se crean datos de demostración, se registran pacientes en una instancia de `Clinica`, se recorre una colección heterogénea y se muestran resultados normales y excepcionales. Las entidades se encuentran en `src/modelos.py`, el servicio que coordina registros y programación está en `src/clinica.py`, y las excepciones se definen en `src/excepciones.py`.

La agenda asigna una duración ilustrativa a cada paciente según datos de su tipo. Estos minutos y el horario de 08:00 a 18:00 son supuestos de demostración, no reglas médicas ni políticas confirmadas de una clínica real.

## Decisiones de diseño

### Responsabilidades de las clases

`Clinica` mantiene el registro de pacientes y coordina la creación de citas. `Responsable` almacena nombre y teléfono, y permite consultar sus animales. `Veterinario` representa al profesional y verifica que sus citas no se crucen. `Cita` mantiene la fecha, el estado, la duración y las referencias al paciente, al responsable y al veterinario. `HistoriaClinica` agrega y devuelve notas breves. Estas responsabilidades separan la información y las reglas que pertenecen a cada concepto.

### Abstracción y herencia

`Animal` es abstracta porque expresa datos compartidos por los pacientes, pero no representa un tipo específico que el programa deba crear directamente. Declara `resumen()` y `duracion_atencion()` como operaciones abstractas: cada tipo concreto debe implementar su descripción y estimación.

`Perro`, `Gato` y `Ave` heredan de `Animal` porque cada uno es un animal. Comparten identificador, nombre, edad, responsable e historial. Cada clase hija agrega información propia: tamaño para `Perro`, entorno interior/exterior para `Gato` y tipo de ave para `Ave`. Las tres sobrescriben `resumen()` y `duracion_atencion()`. Por ejemplo, la duración del perro depende del tamaño, la del gato de su entorno declarado y la del ave de su tipo. Son valores didácticos para mostrar variación de comportamiento.

### Polimorfismo

En `main.py`, la lista `pacientes` contiene instancias de las tres clases concretas. Un único ciclo llama a `resumen()` y `duracion_atencion()` en cada elemento, sin condicionales que pregunten qué subtipo se está recorriendo. Python ejecuta la implementación correspondiente al objeto.

### Relaciones y composición

Un `Responsable` puede estar relacionado con varios animales. Cada `Cita` hace referencia a un paciente, a su responsable y a un veterinario; la clínica registra pacientes y citas, y cada veterinario administra sus citas.

La composición se aplica entre `Animal` e `HistoriaClinica`: el constructor de `Animal` crea un historial propio y el paciente lo expone para agregar o consultar entradas. El historial forma parte del expediente del paciente dentro del alcance de este modelo. No se modela mediante herencia porque un historial no es un tipo de animal; es un objeto que el paciente contiene.

### Excepciones del dominio

`PacienteNoRegistradoError` se lanza desde `Clinica.programar_cita()` cuando el animal no pertenece al registro de la clínica. `CitaOcupadaError` se lanza desde `Veterinario.agendar()` cuando el intervalo se cruza con otra cita de ese profesional. `HorarioInvalidoError` se lanza al construir `Cita` cuando su hora de inicio queda fuera del horario ilustrativo. `main.py` captura las tres excepciones e imprime mensajes, luego continúa con las siguientes demostraciones.

## Cambios de diseño durante el desarrollo

La propuesta inicial consideró clínica veterinaria, control de equipaje en aeropuerto y citas de clínica. Se eligió la clínica veterinaria y se acotó el alcance a consola, registro de pacientes, citas e historial breve. Tras ejecutar la primera versión, la salida mostró «1 años» para un paciente de un año. Se añadió la propiedad común `edad_texto` en `Animal` y las tres subclases la usan en sus resúmenes para elegir «año» o «años». Esta corrección surgió de la revisión de salida durante el desarrollo asistido.

También se definieron duraciones de agenda por tipo de paciente y el horario de 08:00 a 18:00 como supuestos demostrativos. No representan políticas confirmadas de una clínica real ni recomendaciones médicas.

## Uso de herramientas de inteligencia artificial

Se utilizó ChatGPT para interpretar los criterios de la actividad, proponer contextos, diseñar las entidades, generar y ajustar el borrador de código, redactar el README y el diagrama UML, y ejecutar la demostración. De las ideas propuestas se conservó la clínica veterinaria; las opciones de aeropuerto y agenda de citas genérica no se seleccionaron. El código inicial se ajustó para mostrar correctamente la edad en singular y para impedir que la duración de una cita exceda el horario de cierre.

La autora debe revisar, comprender y poder explicar el código antes de la entrega. La ejecución de esta versión por ChatGPT no sustituye la revisión personal de Yeniffer. En esta conversación no se confirmó todavía una explicación individual o sustentación del código.

## Verificación del sistema

ChatGPT ejecutó manualmente `main.py` tres veces en el entorno de trabajo con Python 3.12.14. Las ejecuciones iniciales permitieron detectar el plural «1 años»; después de corregirlo, la ejecución final terminó con código 0 y mostró «1 año». La salida incluyó dos citas aceptadas, un rechazo de paciente no registrado, un cruce de agenda, un horario inválido y el mensaje de finalización, lo que demuestra que el flujo continuó después de cada excepción.

La revisión del código confirmó una colección de las tres subclases recorrida con un ciclo que llama a los mismos métodos, la composición del historial dentro de cada paciente y las tres excepciones lanzadas desde `Clinica.programar_cita()`, `Veterinario.agendar()` y el constructor de `Cita`, respectivamente. No se creó ni ejecutó una suite de pruebas automatizadas. Esta evidencia corresponde a la ejecución asistida en el entorno de ChatGPT; Yeniffer debe repetir la ejecución en su propio entorno y revisar el código antes de entregar.

## Conclusiones

La versión implementada integra las clases del dominio en una demostración ejecutable: cada paciente especializado comparte una interfaz, mientras que la cita y la clínica coordinan relaciones y validaciones. La ejecución de referencia permitió corregir un detalle de presentación de edad y comprobar que los errores de dominio no detienen las demostraciones posteriores. Los minutos de agenda y el horario se mantienen como supuestos didácticos y deberían ajustarse si se usara información real de una clínica.

**Borrador de reflexión individual para revisar antes de entregar:** «Al revisar este proyecto, relacioné la herencia con los tipos de pacientes que comparten datos, y el polimorfismo con el ciclo que llama a los mismos métodos para perros, gatos y aves. También observé que la composición sirve para representar el historial que pertenece a cada paciente. La corrección de “1 años” me mostró la importancia de revisar la salida del programa, además de su lógica. La solución es una base didáctica; antes de entregarla debo poder explicar cada clase y cada validación con mis propias palabras.»

Usar esta reflexión solo si coincide con lo que Yeniffer realmente comprendió al revisar y ejecutar el programa. Puede editarla para que describa con precisión su experiencia.

## Referencias y herramientas consultadas

- Universidad de Manizales, **Actividad colaborativa N.º 3. Proyecto Final**, documento suministrado para la actividad.
- Python Software Foundation, [documentación del módulo `abc` de Python 3.12](https://docs.python.org/3.12/library/abc.html), consultada para la clase base abstracta y `@abstractmethod`.
- Python Software Foundation, [documentación del módulo `datetime` de Python 3.12](https://docs.python.org/3.12/library/datetime.html), consultada para fechas, horas y duración de citas.
