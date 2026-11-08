"""Coordinación de registros y citas de la clínica."""

from .excepciones import PacienteNoRegistradoError


class Clinica:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__pacientes = {}
        self.__citas = []

    @property
    def nombre(self):
        return self.__nombre

    def registrar_paciente(self, paciente):
        if paciente.identificador in self.__pacientes:
            raise ValueError(f"Ya existe el paciente {paciente.identificador}.")
        self.__pacientes[paciente.identificador] = paciente

    def buscar_paciente(self, identificador):
        return self.__pacientes.get(identificador)

    def programar_cita(self, paciente, veterinario, fecha_hora):
        from .modelos import Cita
        if self.buscar_paciente(paciente.identificador) is not paciente:
            raise PacienteNoRegistradoError(
                f"El paciente {paciente.nombre} no está registrado en {self.nombre}."
            )
        cita = Cita(paciente, veterinario, fecha_hora)
        veterinario.agendar(cita)
        self.__citas.append(cita)
        return cita

    def listar_citas(self):
        return tuple(self.__citas)
