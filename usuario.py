class Usuario:

    def __init__(self, nombre: str, apellido: str, cedula: str):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.compras = []

    def registar_usuario(nombre, apellido, cedula):
        nombre = input("Por favor ingrese su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        cedula = input("Por favor ingrese su cedula: ")

while True: 
    print(""" Bievenido a la plataforma de compras, por favor selecciona una opcion:
    1. Registrar Usuario

""")
    option = input()
    if option == 1:
        registrar_usuario()
    break