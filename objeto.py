class Propiedad:
    def __init__(self, id, tipo, valor):
        self.nombre = id
        self.tipo = tipo
        self.valor = valor
    
    def __str__(self):
        return f"{self.nombre}: ({self.tipo}, {self.valor})"
        
class Objeto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = {}

    @staticmethod
    def agregar_propiedad(self, propiedad: Propiedad):
        self.propiedades[propiedad.nombre] = (propiedad.tipo, propiedad.valor)

        tipos = {
            int: "int",
            float: "float",
            str: "character",
            bool: "boolean"
        }
        if propiedad.valor != None and (type(propiedad.valor) == str and len(propiedad.valor) < 1):
            if propiedad.tipo != tipos[type(propiedad.valor)]:
                print(f"Error: La propiedad {propiedad.nombre} no es del tipo {type(propiedad.valor)}.")
                return

    def obtener_propiedad(self, nombre):
        return self.propiedades.get(nombre)
    
    def __str__(self):
        return f"{self.nombre}: {self.propiedades}"