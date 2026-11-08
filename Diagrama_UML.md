# Diagrama UML de clases

El diagrama corresponde a la implementación de `src/modelos.py`, `src/clinica.py` y `src/excepciones.py`.

```mermaid
classDiagram
    class Animal {
        <<abstract>>
        -str identificador
        -str nombre
        -int edad
        -Responsable responsable
        -HistoriaClinica historia
        +resumen()* str
        +duracion_atencion()* int
    }
    class Perro {
        -str tamano
        +resumen() str
        +duracion_atencion() int
    }
    class Gato {
        -bool vive_en_interior
        +resumen() str
        +duracion_atencion() int
    }
    class Ave {
        -str tipo_ave
        +resumen() str
        +duracion_atencion() int
    }
    class Responsable {
        -str nombre
        -str telefono
        -list animales
        +agregar_animal(Animal)
        +listar_animales() tuple
    }
    class Veterinario {
        -str identificador
        -str nombre
        -str especialidad
        -list citas
        +agendar(Cita)
        +listar_citas() tuple
    }
    class Cita {
        -Animal paciente
        -Responsable responsable
        -Veterinario veterinario
        -datetime fecha_hora
        -int duracion
        -str estado
        +cancelar()
        +descripcion() str
    }
    class HistoriaClinica {
        -list entradas
        +agregar_entrada(str)
        +consultar_entradas() tuple
    }
    class Clinica {
        -str nombre
        -dict pacientes
        -list citas
        +registrar_paciente(Animal)
        +buscar_paciente(str) Animal
        +programar_cita(Animal, Veterinario, datetime) Cita
        +listar_citas() tuple
    }
    class ErrorClinica {
        <<exception>>
    }
    class PacienteNoRegistradoError {
        <<exception>>
    }
    class CitaOcupadaError {
        <<exception>>
    }
    class HorarioInvalidoError {
        <<exception>>
    }

    Animal <|-- Perro
    Animal <|-- Gato
    Animal <|-- Ave
    Animal *-- HistoriaClinica : contiene esencialmente
    Responsable "1" o-- "0..*" Animal : responsable de
    Cita --> "1" Animal : paciente
    Cita --> "1" Responsable : contacto
    Cita --> "1" Veterinario : profesional
    Clinica o-- "0..*" Animal : registra
    Clinica o-- "0..*" Cita : agenda
    Veterinario o-- "0..*" Cita : asigna
    ErrorClinica <|-- PacienteNoRegistradoError
    ErrorClinica <|-- CitaOcupadaError
    ErrorClinica <|-- HorarioInvalidoError
```

La composición se usa entre `Animal` e `HistoriaClinica`: el historial se crea dentro del constructor del paciente y se consulta desde ese paciente. Responsable, clínica, veterinario y cita se vinculan mediante asociaciones porque existen como entidades relacionadas con responsabilidades propias.
