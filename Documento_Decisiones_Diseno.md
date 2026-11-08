# Documento de Decisiones de Diseño

## Portada

**Proyecto:** Agenda de una clínica veterinaria  
**Asignatura:** Programación I  
**Integrante:** Yeniffer Fernanda Arias Ordoñez  
**Docente:** Natalia Marcela Castellanos Gomez  
**Fecha:** 08/11/2026  
**Repositorio público:** https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo

## Introducción

Este documento explica el diseño de mi programa de consola para registrar pacientes animales y programar citas en una clínica veterinaria. El sistema relaciona cada animal con su responsable, permite asignar citas a veterinarios y conserva notas breves en el historial de cada paciente. No diagnostica, recomienda tratamientos ni guarda información entre ejecuciones.

En el módulo trabajé previamente el contexto de gestión académica. Elegí la clínica veterinaria, un contexto distinto y permitido por la guía, para practicar abstracción, herencia, encapsulamiento, polimorfismo, composición y excepciones del dominio.

## Descripción general

El punto de entrada es main.py. Allí creo datos de demostración, registro pacientes en Clinica, recorro una colección heterogénea y muestro casos normales y excepcionales. Las entidades están en src/modelos.py, el servicio está en src/clinica.py y las excepciones en src/excepciones.py.

Las duraciones de agenda y el horario de 08:00 a 18:00 son supuestos didácticos, no reglas médicas ni políticas confirmadas de una clínica real.

## Decisiones de diseño

### Responsabilidades de las clases

Clinica mantiene el registro de pacientes y coordina citas. Responsable almacena nombre y teléfono y permite consultar sus animales. Veterinario representa al profesional y verifica cruces de citas. Cita reúne fecha, estado, duración y referencias al paciente, responsable y veterinario. HistoriaClinica agrega y devuelve notas breves. Estas responsabilidades separan los datos y reglas de cada concepto.

### Abstracción y herencia

Animal es abstracta porque reúne datos comunes, pero no representa un tipo específico que el programa necesite crear directamente. Declara resumen() y duracion_atencion() como operaciones abstractas que cada subtipo concreto implementa.

Perro, Gato y Ave heredan de Animal porque cada uno es un animal. Comparten identificador, nombre, edad, responsable e historial. Perro agrega tamaño; Gato, su entorno interior o exterior; Ave, su tipo. Las tres clases sobrescriben resumen() y duracion_atencion(). Las duraciones varían según el tamaño del perro, el entorno del gato y el tipo de ave; son valores didácticos.

### Polimorfismo

En main.py, la lista pacientes contiene instancias de las tres clases concretas. Un solo ciclo llama a resumen() y duracion_atencion() en cada elemento, sin condicionales que identifiquen el subtipo. Python ejecuta el método correspondiente al objeto.

### Relaciones y composición

Un Responsable puede relacionarse con varios animales. Cada Cita referencia paciente, responsable y veterinario; Clinica registra pacientes y citas, y cada veterinario administra sus citas.

La composición se aplica entre Animal e HistoriaClinica: el constructor del paciente crea su historial. Este objeto forma parte esencial del expediente en el alcance del sistema; no corresponde a herencia porque un historial no es un tipo de animal.

### Excepciones del dominio

PacienteNoRegistradoError se lanza desde Clinica.programar_cita() cuando el animal no está registrado. CitaOcupadaError se lanza desde Veterinario.agendar() si el intervalo se cruza con otra cita. HorarioInvalidoError se lanza al construir Cita si la hora queda fuera del horario ilustrativo. main.py captura las tres excepciones, muestra mensajes y continúa.

## Cambios de diseño durante el desarrollo

Consideré una clínica veterinaria, el control de equipaje en aeropuerto y una agenda genérica de citas. Elegí la clínica y limité el alcance a consola, registro de pacientes, citas e historial breve. La primera salida mostró «1 años»; corregí la presentación de edad para mostrar «1 año».

Definí duraciones de agenda y horario de 08:00 a 18:00 como supuestos de demostración. Además, cambié Gato para que acepte únicamente True o False y añadí validaciones que rechazan campos de texto obligatorios vacíos.

## Uso de herramientas de inteligencia artificial

Utilicé ChatGPT como apoyo para estructurar el código y la documentación. En Gato cambié la conversión automática de valores a booleanos por una validación que exige True o False; también añadí validaciones para rechazar datos obligatorios vacíos.

## Verificación del sistema

La ejecución final de main.py terminó con código 0 usando Python 3.14.4. Mostró seis pacientes, dos citas aceptadas, los tres errores de dominio y el mensaje final, así que el programa continuó después de cada error. La salida completa está guardada en evidencias/ejecucion_programa.txt.

El comando solicitado py main.py no pudo iniciar el lanzador py.exe de WindowsApps en este entorno. Ejecuté el mismo archivo con la ruta absoluta de Python 3.14.4. También comprobé manualmente que Gato acepta booleanos reales y rechaza texto, enteros y None, y que los campos obligatorios de responsable, veterinario y clínica rechazan vacíos. No ejecuté una suite automatizada.

## Conclusiones

La agenda integra las clases del dominio en una demostración: los tipos de paciente comparten una interfaz y la cita y la clínica coordinan sus relaciones y validaciones.

Al desarrollar este sistema comprendí que Perro, Gato y Ave comparten datos y operaciones de Animal, pero cada tipo responde de manera propia en sus métodos. El ciclo único me permitió observar el polimorfismo en funcionamiento y entender cómo evita preguntar qué tipo de paciente se procesa.

## Referencias y herramientas consultadas

- Universidad de Manizales, Actividad colaborativa N.º 3. Proyecto Final, documento suministrado para la actividad.
- Python Software Foundation, documentación del módulo abc de Python 3.12: https://docs.python.org/3.12/library/abc.html
- Python Software Foundation, documentación del módulo datetime de Python 3.12: https://docs.python.org/3.12/library/datetime.html
