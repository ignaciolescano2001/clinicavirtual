from datetime import datetime

class Consulta:
    def __init__(self, en_linea_o_cita, fecha_solicitud, cadena_sintomas, estado_solicitud):
        self.en_linea_o_cita = en_linea_o_cita
        self.fecha_solicitud = fecha_solicitud
        self.cadena_sintomas = cadena_sintomas
        self.estado_solicitud = estado_solicitud
        self.doctor = None
        self.preinscripcion = None
        self.paciente = None
        self.laboratorio = None


class Paciente:
    def __init__(self, id, nombre, edad, genero, email, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.preinscripciones = []

    def crear_perfil_de_paciente(self):
        pass

    def editar_perfil_de_paciente(self):
        pass

    def eliminar_perfil_de_paciente(self):
        pass

    def solicitud_de_consulta(self):
        pass


class Preinscripcion:
    def __init__(self, id_de_prescripcion, diagnostico, nombre_de_medicina, potencia_medicamento,
                 frecuencia_medicamento, observaciones, prueba_de_laboratorio,
                 laboratorio_de_instrucciones, preinscripcion_entregar,
                 solicitudes_de_laboratorio_realizadas, monto_de_la_factura):
        self.id_de_prescripcion = id_de_prescripcion
        self.diagnostico = diagnostico
        self.nombre_de_medicina = nombre_de_medicina
        self.potencia_medicamento = potencia_medicamento
        self.frecuencia_medicamento = frecuencia_medicamento
        self.observaciones = observaciones
        self.prueba_de_laboratorio = prueba_de_laboratorio
        self.laboratorio_de_instrucciones = laboratorio_de_instrucciones
        self.preinscripcion_entregar = preinscripcion_entregar
        self.solicitudes_de_laboratorio_realizadas = solicitudes_de_laboratorio_realizadas
        self.monto_de_la_factura = monto_de_la_factura
        self.quimico = None

    def generar_factura(self):
        pass


class Doctor:
    def __init__(self, id, nombre, edad, genero, calificacion, experiencia, numero_registro):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.calificacion = calificacion
        self.experiencia = experiencia
        self.numero_registro = numero_registro
        self.especialista = None
        self.pacientes = []

    def añadir_medico(self):
        pass

    def editar_doctor(self):
        pass

    def eliminar_medico(self):
        pass

    def proporcionar_consulta(self):
        pass


class Especialista:
    def __init__(self, ssd, nombre, descripcion):
        self.ssd = ssd
        self.nombre = nombre
        self.descripcion = descripcion

    def agregar_especialidad(self, ssd, nombre, descripcion):
        pass

    def editar_especialidad(self, ssd, nombre, descripcion):
        pass

    def eliminar_especialidad(self, ssd):
        pass


class Laboratorio:
    def __init__(self, id, nombre, direccion, email, telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono

    def añadir_laboratorio(self):
        pass

    def editar_laboratorio(self):
        pass

    def eliminar_laboratorio(self):
        pass

    def realizar_muestra(self):
        pass

    def generar_informe(self):
        pass


class Quimico:
    def __init__(self, id_quimico, nombre, direccion, email, telefono):
        self.id_quimico = id_quimico
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono

    def añadir_quimico(self):
        pass

    def editar_quimico(self):
        pass

    def entrega_de_medicamentos(self):
        pass
