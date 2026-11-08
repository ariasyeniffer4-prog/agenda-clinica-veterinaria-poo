# Documento de Decisiones de Diseño

## Portada

**Proyecto:** Agenda de una clínica veterinaria  
**Asignatura:** Programación I  
**Integrante:** Yeniffer Fernanda Arias Ordoñez  
**Docente:** Natalia Marcela Castellanos Gomez  
**Fecha:** 08/11/2026  
**Repositorio público:** https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo  
**Commit de documentación y punto de entrada:** ff53194 — https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo/commit/ff53194b4be827b68f15127c08ad6232db82898c

## Introducción

Este documento explica las decisiones de una aplicación de consola para registrar pacientes animales y programar citas en una clínica veterinaria. El sistema relaciona cada animal con una persona responsable, permite asignar citas a veterinarios y conserva notas breves en el historial de cada paciente. No diagnostica, recomienda tratamientos, factura ni conserva datos entre ejecuciones.

La clínica veterinaria se eligió después de identificar que el proyecto previo de Yeniffer ya abordaba gestión académica, contexto excluido por la actividad. El problema se delimitó a la agenda de pacientes, citas e historial breve para practicar los conceptos de programación orientada a objetos en Python.

## Descripción de la solución

El archivo main.py crea los objetos de demostración y coordina los casos normales y excepcionales. El paquete src contiene los modelos, el servicio de clínica y las excepciones del dominio. La duración de atención y el horario de 08:00 a 18:00 son supuestos de demostración, no recomendaciones médicas ni políticas confirmadas de una clínica real.

## Decisiones de diseño

### Clases y responsabilidades

Animal es la clase abstracta que concentra identificador, nombre, edad, responsable e historial. Perro, Gato y Ave agregan información propia de cada tipo. Responsable guarda datos de contacto y sus animales. Veterinario representa al profesional y mantiene su agenda. Cita relaciona paciente, responsable, veterinario, fecha, duración y estado. HistoriaClinica administra notas breves. Clinica registra pacientes y coordina la programación.

### Abstracción, herencia y sobrescritura

Animal hereda de ABC y declara resumen() y duracion_atencion() como operaciones abstractas. No se instancia directamente porque el sistema requiere el comportamiento concreto de uno de los tipos modelados. Perro, Gato y Ave son animales, así que heredan de la clase común y comparten sus datos y operaciones.

Cada subtipo agrega un dato propio: tamaño del perro, entorno interior/exterior del gato y tipo de ave. Los tres sobrescriben resumen() y duracion_atencion(). La duración cambia con los datos de cada clase: tamaño para el perro, entorno para el gato y tipo de ave para el ave. Los minutos asignados solo sirven para mostrar variación de comportamiento.

### Polimorfismo

En main.py, la lista pacientes contiene instancias de Perro, Gato y Ave. Un único ciclo llama a resumen() y duracion_atencion() para cada elemento sin condicionales que identifiquen su tipo. Cada objeto ejecuta su propia implementación.

### Relaciones y composición

Un Responsable se relaciona con uno o varios animales. Cada Cita relaciona un paciente con su responsable y un veterinario; la clínica y el profesional mantienen sus colecciones de citas. La composición se usa entre Animal e HistoriaClinica: cada paciente crea y contiene su propio historial como parte esencial de su expediente dentro de este alcance. No es herencia porque una historia clínica no es un tipo de animal; es un objeto que pertenece al paciente.

### Excepciones del dominio

PacienteNoRegistradoError se lanza desde Clinica.programar_cita() si el paciente no está registrado. CitaOcupadaError se lanza desde Veterinario.agendar() si el horario se cruza con otra cita del mismo profesional. HorarioInvalidoError se lanza al construir Cita cuando la duración no cabe dentro del horario ilustrativo. main.py captura estos tres errores, muestra mensajes y continúa con las siguientes demostraciones.

## Cambios durante el desarrollo

Se consideraron varias ideas antes de elegir la clínica veterinaria; el control de equipaje y una agenda de citas genérica no fueron seleccionados. El alcance se concretó en un programa de consola con registro, citas e historial breve. La primera ejecución mostró “1 años” para un paciente de un año. Se añadió edad_texto en Animal y se modificaron los resúmenes de los tres subtipos para mostrar correctamente “año” o “años”. También se validó que la duración completa de la cita no exceda la hora de cierre.

## Uso de inteligencia artificial

ChatGPT se utilizó para interpretar los criterios, comparar contextos, proponer el diseño, generar y ajustar el borrador de código, redactar el README y el diagrama UML, revisar la salida y ejecutar el programa. Se conservó la clínica veterinaria; se descartaron las otras ideas propuestas. La corrección singular/plural y la validación del final de la cita se incorporaron tras revisar el código y su salida. Yeniffer debe comprender, verificar y poder explicar el resultado antes de entregarlo.

## Verificación

ChatGPT ejecutó main.py tres veces con Python 3.12.14 en el entorno de trabajo. Tras corregir el resumen de edad, la ejecución final terminó con código 0, mostró dos citas aceptadas y capturó los tres errores previstos: paciente no registrado, cruce de horario y hora fuera del horario de atención. El programa continuó hasta imprimir el mensaje final. La revisión del código confirmó el ciclo polimórfico y la composición del historial. No se ejecutó una suite automatizada. Esta evidencia corresponde a la ejecución asistida y no se presenta como ejecución personal de la autora.

## Conclusiones

La solución integra abstracción, herencia, encapsulamiento, polimorfismo, composición y excepciones en un ejemplo de agenda veterinaria acotado. La revisión de la salida permitió corregir el plural de la edad y comprobar que los errores controlados no detienen la demostración. Las duraciones y el horario son supuestos didácticos que requerirían validación si se adaptara el programa a una clínica real.

**Borrador de reflexión individual para validar:** Al revisar este proyecto, relacioné la herencia con los tipos de pacientes que comparten datos y el polimorfismo con el ciclo que llama a los mismos métodos para perros, gatos y aves. También observé que la composición representa el historial que pertenece a cada paciente. La corrección de “1 años” mostró la importancia de revisar la salida del programa además de su lógica. Antes de entregar, debo poder explicar cada clase y cada validación con mis propias palabras.

Usar la reflexión anterior solo si representa la experiencia real de Yeniffer; puede editarse para describir con precisión su aprendizaje.

## Referencias y herramientas consultadas

- Universidad de Manizales, Actividad colaborativa N.º 3. Proyecto Final, documento suministrado para la actividad.
- Python Software Foundation, documentación oficial del módulo abc: https://docs.python.org/3.12/library/abc.html
- Python Software Foundation, documentación oficial del módulo datetime: https://docs.python.org/3.12/library/datetime.html
- ChatGPT, OpenAI, como apoyo para interpretar requisitos, proponer, programar, documentar y revisar la demostración.
