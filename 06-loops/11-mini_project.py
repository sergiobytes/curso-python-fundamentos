inventory = {
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galleta": 12
}

cart = []

opcion = ""

print("¡Bienvenido a la tienda de dulces, DevCandy!")

print("Inventario (Precios):")

while opcion != 'salir':
    for item, price in inventory.items():
        print(f"{item.capitalize()}: ${price}")
    opcion = input(
        "¿Qué dulce deseas agregar a tu carrito? (Escribe 'Salir' para terminar): ").lower()

    if opcion in inventory:
        cart.append({"producto": opcion, "precio": inventory[opcion]})
        print(f"Agregando => {opcion.capitalize()}")
    elif opcion != 'salir':
        print("Lo siento, no tenemos ese dulce.")

print("\nGracias por tu compra. Estos son los dulces en tu carrito:")
total = 0
for item in cart:
    print(f"- {item['producto'].capitalize()} - ${item['precio']}")
    total += item['precio']

print(f"\nTotal a pagar: ${total}")