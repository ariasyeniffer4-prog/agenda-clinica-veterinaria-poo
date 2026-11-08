"""Excepciones del dominio de la clínica veterinaria."""


class ErrorClinica(Exception):
    """Clase base para errores controlados del sistema."""


class PacienteNoRegistradoError(ErrorClinica):
    """Se intentó programar una cita para un paciente no registrado."""


class CitaOcupadaError(ErrorClinica):
    """El veterinario ya tiene una cita en la fecha y hora solicitadas."""


class HorarioInvalidoError(ErrorClinica):
    """La cita está fuera del horario de atención configurado."""
