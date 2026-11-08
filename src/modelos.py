"""Entidades del dominio. Los atributos se mantienen encapsulados."""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from .excepciones import CitaOcupadaError, HorarioInvalidoError


def _texto_requerido(valor, campo):
    """Valida y normaliza un dato de texto obligatorio."""
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} es obligatorio y no puede estar vacío.")
    return valor.strip()


class HistoriaClinica:
    """Registro breve de observaciones asociadas a un paciente."""

    def __init__(self):
        self.__entradas = []

    def agregar_entrada(self, texto):
        texto = _texto_requerido(texto, "La entrada de la historia")
        self.__entradas.append(texto)

    def consultar_entradas(self):
        return tuple(self.__entradas)


class Responsable:
    """Persona de contacto responsable de uno o varios pacientes."""

    def __init__(self, nombre, telefono):
        self.__nombre = _texto_requerido(nombre, "El nombre del responsable")
        self.__telefono = _texto_requerido(telefono, "El teléfono del responsable")
        self.__animales = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono

    def agregar_animal(self, animal):
        if animal not in self.__animales:
            self.__animales.append(animal)

    def listar_animales(self):
        return tuple(self.__animales)


class Animal(ABC):
    """Concepto general no instanciable de paciente animal."""

    def __init__(self, identificador, nombre, edad, responsable):
        self.__identificador = _texto_requerido(identificador, "El identificador del paciente")
        self.__nombre = _texto_requerido(nombre, "El nombre del paciente")
        if not isinstance(edad, int) or isinstance(edad, bool) or edad < 0:
            raise ValueError("La edad debe ser un número entero no negativo.")
        if not isinstance(responsable, Responsable):
            raise ValueError("El paciente requiere un responsable válido.")
        self.__edad = edad
        self.__responsable = responsable
        # El historial es una parte esencial del expediente de este paciente.
        self.__historia = HistoriaClinica()
        responsable.agregar_animal(self)

    @property
    def identificador(self):
        return self.__identificador

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def edad_texto(self):
        unidad = "año" if self.__edad == 1 else "años"
        return f"{self.__edad} {unidad}"

    @property
    def responsable(self):
        return self.__responsable

    @property
    def historia(self):
        return self.__historia

    @abstractmethod
    def resumen(self):
        """Devuelve una descripción según los datos de la especie."""

    @abstractmethod
    def duracion_atencion(self):
        """Estima minutos de agenda para organizar la cita."""


class Perro(Animal):
    def __init__(self, identificador, nombre, edad, responsable, tamano):
        tamano = _texto_requerido(tamano, "El tamaño del perro").lower()
        if tamano not in {"pequeño", "mediano", "grande"}:
            raise ValueError("El tamaño debe ser pequeño, mediano o grande.")
        super().__init__(identificador, nombre, edad, responsable)
        self.__tamano = tamano

    @property
    def tamano(self):
        return self.__tamano

    def resumen(self):
        return f"Perro: {self.nombre}, {self.edad_texto}, tamaño {self.tamano}."

    def duracion_atencion(self):
        return {"pequeño": 30, "mediano": 40, "grande": 50}[self.tamano]


class Gato(Animal):
    def __init__(self, identificador, nombre, edad, responsable, vive_en_interior):
        if not isinstance(vive_en_interior, bool):
            raise ValueError("vive_en_interior debe ser True o False.")
        super().__init__(identificador, nombre, edad, responsable)
        self.__vive_en_interior = vive_en_interior

    @property
    def vive_en_interior(self):
        return self.__vive_en_interior

    def resumen(self):
        entorno = "interior" if self.vive_en_interior else "exterior"
        return f"Gato: {self.nombre}, {self.edad_texto}, vive en {entorno}."

    def duracion_atencion(self):
        return 30 if self.vive_en_interior else 40


class Ave(Animal):
    def __init__(self, identificador, nombre, edad, responsable, tipo_ave):
        tipo_ave = _texto_requerido(tipo_ave, "El tipo de ave")
        super().__init__(identificador, nombre, edad, responsable)
        self.__tipo_ave = tipo_ave

    @property
    def tipo_ave(self):
        return self.__tipo_ave

    def resumen(self):
        return f"Ave ({self.tipo_ave}): {self.nombre}, {self.edad_texto}."

    def duracion_atencion(self):
        return 35 if self.tipo_ave.lower() in {"loro", "guacamaya"} else 25


class Veterinario:
    """Profesional y conjunto de citas asignadas."""

    def __init__(self, identificador, nombre, especialidad):
        self.__identificador = _texto_requerido(identificador, "El identificador del veterinario")
        self.__nombre = _texto_requerido(nombre, "El nombre del veterinario")
        self.__especialidad = _texto_requerido(especialidad, "La especialidad del veterinario")
        self.__citas = []

    @property
    def identificador(self):
        return self.__identificador

    @property
    def nombre(self):
        return self.__nombre

    @property
    def especialidad(self):
        return self.__especialidad

    def agendar(self, cita):
        inicio = cita.fecha_hora
        fin = cita.fin
        for existente in self.__citas:
            if inicio < existente.fin and existente.fecha_hora < fin:
                raise CitaOcupadaError(
                    f"{self.nombre} ya tiene una cita que se cruza con {inicio:%d/%m/%Y %H:%M}."
                )
        self.__citas.append(cita)

    def listar_citas(self):
        return tuple(self.__citas)


class Cita:
    """Reserva que relaciona paciente, responsable y veterinario."""

    HORA_APERTURA = 8
    HORA_CIERRE = 18

    def __init__(self, paciente, veterinario, fecha_hora):
        if not isinstance(fecha_hora, datetime):
            raise TypeError("La fecha de la cita debe ser datetime.")
        minutos = fecha_hora.hour * 60 + fecha_hora.minute
        cierre = self.HORA_CIERRE * 60
        duracion = paciente.duracion_atencion()
        fin_minutos = minutos + duracion
        if fecha_hora.hour < self.HORA_APERTURA or minutos >= cierre or fin_minutos > cierre:
            raise HorarioInvalidoError(
                f"La cita debe transcurrir dentro del horario de {self.HORA_APERTURA:02d}:00 a {self.HORA_CIERRE:02d}:00."
            )
        self.__paciente = paciente
        self.__responsable = paciente.responsable
        self.__veterinario = veterinario
        self.__fecha_hora = fecha_hora
        self.__duracion = duracion
        self.__estado = "pendiente"

    @property
    def paciente(self):
        return self.__paciente

    @property
    def responsable(self):
        return self.__responsable

    @property
    def veterinario(self):
        return self.__veterinario

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @property
    def duracion(self):
        return self.__duracion

    @property
    def fin(self):
        return self.__fecha_hora + timedelta(minutes=self.__duracion)

    @property
    def estado(self):
        return self.__estado

    def cancelar(self):
        self.__estado = "cancelada"

    def descripcion(self):
        return (
            f"{self.__fecha_hora:%d/%m/%Y %H:%M} | {self.__paciente.nombre} | "
            f"Dra./Dr. {self.__veterinario.nombre} | {self.__duracion} min | {self.__estado}"
        )
