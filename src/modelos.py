"""Entidades del dominio. Los atributos se mantienen encapsulados."""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from .excepciones import CitaOcupadaError, HorarioInvalidoError


class HistoriaClinica:
    """Registro breve de observaciones asociadas a un paciente."""

    def __init__(self):
        self.__entradas = []

    def agregar_entrada(self, texto):
        texto = texto.strip()
        if not texto:
            raise ValueError("La entrada de la historia no puede estar vacía.")
        self.__entradas.append(texto)

    def consultar_entradas(self):
        return tuple(self.__entradas)


class Responsable:
    """Persona de contacto responsable de uno o varios pacientes."""

    def __init__(self, nombre, telefono):
        self.__nombre = nombre.strip()
        self.__telefono = telefono.strip()
        self.__animales = []
        if not self.__nombre or not self.__telefono:
            raise ValueError("El responsable requiere nombre y teléfono.")

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
        if not identificador or not nombre.strip():
            raise ValueError("El paciente requiere identificador y nombre.")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__identificador = identificador
        self.__nombre = nombre.strip()
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
        super().__init__(identificador, nombre, edad, responsable)
        self.__vive_en_interior = bool(vive_en_interior)

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
        if not tipo_ave.strip():
            raise ValueError("Debe indicarse el tipo de ave.")
        super().__init__(identificador, nombre, edad, responsable)
        self.__tipo_ave = tipo_ave.strip()

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
        self.__identificador = identificador
        self.__nombre = nombre.strip()
        self.__especialidad = especialidad.strip()
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
