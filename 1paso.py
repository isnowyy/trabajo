def saludar(nombre):
    if not nombre.strip():
        return "Hola, usuario"
    return f"Hola, {nombre}"

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    print(saludar(nombre))