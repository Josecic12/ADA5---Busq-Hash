def gestion_inventario():
    inventario = {
        "manzana": 0.5,
        "pera": 0.75,
        "naranja": 0.65,
        "plátano": 0.3,
        "uva": 1.2
    }

    print("\n--- Gestión de Inventario ---")
    print("Productos disponibles: ")
    for producto, precio in inventario.items():
        print(f"  - {producto.capitalize()}: ${precio:.2f}")

    producto = input("\nIngresa el nombre del producto para buscar su precio: ").strip().lower()
    if producto in inventario:
        print(f"\nEl precio de {producto.capitalize()} es: ${inventario[producto]:.2f}")
    else:
        print(f"\nEl producto '{producto}' no está en el inventario.")

gestion_inventario()
