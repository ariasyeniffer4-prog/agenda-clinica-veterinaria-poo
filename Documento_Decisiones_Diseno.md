# Documento de Decisiones de Diseño

## Portada

**Proyecto:** Agenda de una clínica veterinaria  
**Asignatura:** Programación I  
**Integrante:** Yeniffer Fernanda Arias Ordoñez  
**Docente:** Natalia Marcela Castellanos Gomez  
**Fecha de entrega:** 08/11/2026  
**Repositorio público:** https://github.com/ariasyeniffer4-prog/agenda-clinica-veterinaria-poo

## Introducción

Este documento explica el diseño de mi programa de consola para organizar el registro de pacientes animales y la programación de citas en una clínica veterinaria. Su alcance es acotado: registra animales y responsables, relaciona cada cita con un veterinario y permite guardar notas breves en el historial de cada paciente. No diagnostica, recomienda tratamientos ni conserva información entre ejecuciones.

Elegí la clínica veterinaria después de descartar el contexto de gestión académica trabajado previamente. El sistema ofrece un escenario concreto para explicar abstracción, herencia, encapsulamiento, polimorfismo, composición y excepciones propias del dominio.

## Descripción general

El punto de entrada es main.py. Allí creo los datos de demostración, registro pacientes en una instancia de Clinica, recorro una colección heterogénea y presento casos normales y excepcionales. Las entidades están en src/modelos.py, el servicio que coordina registros y citas está en src/clinica.py y las excepciones se definen en src/excepciones.py.

La agenda asigna una duración ilustrativa a cada paciente según datos de su tipo. Los minutos y el horario de 08:00 a 18:00 son supuestos de demostración, no reglas médicas ni políticas confirmadas de una clínica real.

## Decisiones de diseño

### Responsabilidades de las clases

Clinica mantiene el registro de pacientes y coordina la creación de citas. Responsable almacena nombre y teléfono, y permite consultar sus animales. Veterinario representa al profesional y verifica que sus citas no se crucen. Cita mantiene la fecha, el estado, la duración y las referencias al paciente, al responsable y al veterinario. HistoriaClinica agrega y devuelve notas breves. Estas responsabilidades separan la información y las reglas que pertenecen a cada concepto.

### Abstracción y herencia

Animal es abstracta porque expresa datos compartidos por los pacientes, pero no representa un tipo específico que el programa deba crear directamente. Declara resumen() y duracion_atencion() como operaciones abstractas: cada tipo concreto debe implementarlas.

Perro, Gato y Ave heredan de Animal porque cada uno es un animal. Comparten identificador, nombre, edad, responsable e historial. Cada clase hija agrega información propia: tamaño para Perro, entorno interior/exterior para Gato y tipo de ave para Ave. Las tres sobrescriben resumen() y duracion_atencion(). La duración del perro depende del tamaño, la del gato de su entorno declarado y la del ave de su tipo. Son valores didácticos para mostrar variación de comportamiento.

### Polimorfismo

En main.py, la lista pacientes contiene instancias de las tres clases concretas. Un único ciclo llama a resumen() y duracion_atencion() en cada elemento, sin condicionales que identifiquen el subtipo. Python ejecuta la implementación correspondiente al objeto.

### Relaciones y composición

Un Responsable puede estar relacionado con varios animales. Cada Cita hace referencia a un paciente, a su responsable y a un veterinario; la clínica registra pacientes y citas, y cada veterinario administra sus citas.

La composición se aplica entre Animal e HistoriaClinica: el constructor de Animal crea un historial propio y el paciente lo expone para agregar o consultar entradas. El historial forma parte del expediente del paciente dentro del alcance del modelo. No uso herencia porque un historial no es un tipo de animal; es un objeto que el paciente contiene.

### Excepciones del dominio

PacienteNoRegistradoError se lanza desde Clinica.programar_cita() cuando el animal no pertenece al registro de la clínica. CitaOcupadaError se lanza desde Veterinario.agendar() cuando el intervalo se cruza con otra cita del profesional. HorarioInvalidoError se lanza al construir Cita cuando su hora de inicio queda fuera del horario ilustrativo. En main.py capturo las tres excepciones, muestro mensajes y continúo con las siguientes demostraciones.

## Cambios de diseño durante el desarrollo

Al inicio consideré una clínica veterinaria, el control de equipaje en aeropuerto y una agenda genérica de citas. Elegí la clínica veterinaria y limité el alcance a consola, registro de pacientes, citas e historial breve. Al revisar la primera salida encontré «1 años» para un paciente de un año. Añadí la propiedad común edad_texto en Animal para mostrar «año» o «años» correctamente en los resúmenes.

También definí duraciones de agenda por tipo de paciente y el horario de 08:00 a 18:00 como supuestos demostrativos. No representan políticas confirmadas de una clínica real ni recomendaciones médicas.

## Uso de herramientas de inteligencia artificial

Utilicé ChatGPT como apoyo para proponer y revisar borradores de código y documentación. Revisé y ajusté el resultado para esta actividad; debo comprender y poder explicar lo que entregue.

## Verificación del sistema

main.py se ejecutó tres veces en el entorno de trabajo con Python 3.12.14. Las ejecuciones iniciales permitieron detectar el plural «1 años»; después de corregirlo, la ejecución final terminó con código 0 y mostró «1 año». La salida incluyó dos citas aceptadas, un rechazo de paciente no registrado, un cruce de agenda, un horario inválido y el mensaje de finalización; el flujo continuó después de cada excepción.

Al revisar el código confirmé que la colección de las tres subclases se recorre con un ciclo que llama a los mismos métodos, que el historial se compone dentro de cada paciente y que las tres excepciones se lanzan desde los métodos responsables. No creé ni ejecuté una suite de pruebas automatizadas. Esta evidencia corresponde a una ejecución asistida; debo revisar el código y puedo repetir la ejecución en mi entorno antes de entregar.

## Conclusiones

La versión implementada integra las clases del dominio en una demostración ejecutable: cada paciente especializado comparte una interfaz, mientras que la cita y la clínica coordinan relaciones y validaciones. La ejecución de referencia permitió corregir un detalle de presentación de edad y comprobar que los errores de dominio no detienen las demostraciones posteriores. Los minutos de agenda y el horario se mantienen como supuestos didácticos que ajustaría si usara información real de una clínica.

**Reflexión individual para revisar antes de entregar:** «Al revisar este proyecto, relacioné la herencia con los tipos de pacientes que comparten datos y el polimorfismo con el ciclo que llama a los mismos métodos para perros, gatos y aves. También observé que la composición representa el historial que pertenece a cada paciente. La corrección de “1 años” me mostró la importancia de revisar la salida del programa además de su lógica. Antes de entregar, debo poder explicar cada clase y validación con mis propias palabras.»

Mantendré esta reflexión solo si coincide con lo que comprendí al revisar el programa; la ajustaré para describir mi experiencia real.

## Referencias y herramientas consultadas

- Universidad de Manizales, Actividad colaborativa N.º 3. Proyecto Final, documento suministrado para la actividad.
- Python Software Foundation, documentación del módulo abc de Python 3.12: https://docs.python.org/3.12/library/abc.html
- Python Software Foundation, documentación del módulo datetime de Python 3.12: https://docs.python.org/3.12/library/datetime.html
