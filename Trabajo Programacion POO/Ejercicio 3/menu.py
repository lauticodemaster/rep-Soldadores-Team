from platos import Plato
from ingredientes import Ingrediente

class MenuRestaurant: 
    def main():
        platos_menu = []

        print("CARGA DE PLATOS DEL MENÚ")

        while True:
            nombre_plato = input("ingrese el nombre del plato: ")
            precio = float(input("ingrese el precio del plato: "))
            es_bebida = input("Es bebida? (s/n): ").lower() == "s"

            ingredientes = []

            if not es_bebida:
                cantidad = int(input("ingrese la cantidad de ingredientes: "))
                for i in range(cantidad):
                    print(f"\ningrediente {i+1}:")
                    nombre_ing = input("nombre: ")
                    cantidad_ing = float(input("cantidad: "))
                    unidad = input("unidad de medida: ")
                    nuevo_ing = Ingrediente(nombre_ing, cantidad_ing, unidad)
                    ingredientes.append(nuevo_ing)

            plato = Plato(nombre_plato, precio, es_bebida, ingredientes)
            platos_menu.append(plato)

            continuar = input("\ndesea agregar otro plato? (s/n): ").lower()
            if continuar != "s":
                break

        print("\n----------- MENÚ ----------------")
        for plato in platos_menu:
            plato.mostrar_info()

# Esto hace que se ejecute solo si abrís este archivo directamente:
if __name__ == "__main__":
    MenuRestaurant.main()
