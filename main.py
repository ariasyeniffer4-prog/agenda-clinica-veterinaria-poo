"""Demostración en consola de la agenda de la clínica veterinaria."""

from datetime import datetime

from src.clinica import Clinica
from src.excepciones import (
    CitaOcupadaError,
    HorarioInvalidoError,
    PacienteNoRegistradoError,
)
from src.modelos import Ave, Gato, Perro, Responsable, Veterinario


def intentar_programar(clinica, paciente, veterinario, fecha_hora):
    """Muestra errores previstos sin detener el resto de la demostración."""
    try:
        cita = clinica.programar_cita(paciente, veterinario, fecha_hora)
        print("Cita creada:", cita.descripcion())
    except PacienteNoRegistradoError as error:
        print("No se pudo programar la cita:", error)
    except CitaOcupadaError as error:
        print("No se pudo programar la cita:", error)
    except HorarioInvalidoError as error:
        print("No se pudo programar la cita:", error)


def main():
    clinica = Clinica("Clínica Huellas y Alas")
    resp1 = Responsable("Ana Torres", "3001112233")
    resp2 = Responsable("Luis Gómez", "3002223344")
    resp3 = Responsable("Marta Ríos", "3003334455")
    vet1 = Veterinario("V01", "Camila Pérez", "medicina general")
    vet2 = Veterinario("V02", "Diego Salas", "animales de compañía")

    pacientes = [
        Perro("P01", "Luna", 4, resp1, "pequeño"),
        Gato("P02", "Nube", 2, resp2, True),
        Ave("P03", "Paco", 5, resp3, "loro"),
        Perro("P04", "Toby", 7, resp2, "grande"),
        Gato("P05", "Mora", 1, resp1, False),
        Ave("P06", "Kiwi", 3, resp3, "periquito"),
    ]
    for paciente in pacientes:
        clinica.registrar_paciente(paciente)

    print(f"Agenda de {clinica.nombre}")
    print("Pacientes y estimaciones (una colección, un ciclo, mismas operaciones):")
    for paciente in pacientes:
        print(f"- {paciente.resumen()} Atención estimada: {paciente.duracion_atencion()} min.")

    pacientes[0].historia.agregar_entrada("Consulta inicial; observación general registrada.")
    print("Entrada de historia:", pacientes[0].historia.consultar_entradas()[0])

    print("\nCasos normales:")
    intentar_programar(clinica, pacientes[0], vet1, datetime(2026, 11, 10, 9, 0))
    intentar_programar(clinica, pacientes[1], vet1, datetime(2026, 11, 10, 10, 0))

    print("\nCasos excepcionales (el programa continúa después de cada uno):")
    paciente_no_registrado = Gato("PX", "Michi", 3, resp1, True)
    intentar_programar(clinica, paciente_no_registrado, vet2, datetime(2026, 11, 10, 11, 0))
    intentar_programar(clinica, pacientes[2], vet1, datetime(2026, 11, 10, 9, 15))
    intentar_programar(clinica, pacientes[3], vet2, datetime(2026, 11, 10, 7, 30))

    print("\nCitas que quedaron registradas:")
    for cita in clinica.listar_citas():
        print("-", cita.descripcion())
    print("Demostración finalizada.")


if __name__ == "__main__":
    main()
