print("-" * 70)
print("Programa de Inventario y Ventas".center(65))
print("-" * 70)

# precios y pesos
PR_CELULAR, PR_LAPTOP = 320, 1400
PS_CELULAR, PS_LAPTOP = 204, 2300  # en gramos

def pedir_dato(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("--- Valor no valido, ingrese un numero entero ---")

celulares = pedir_dato("Ingrese la cantidad de Celulares que se envian: ")
laptops = pedir_dato("Ingrese la cantidad de Laptops que se envian: ")

# Cálculos
precio_celulares = celulares * PR_CELULAR
precio_laptops = laptops * PR_LAPTOP

peso_celulares = celulares * PS_CELULAR
peso_laptops = laptops * PS_LAPTOP

total_articulos = celulares + laptops
valor_total = precio_celulares + precio_laptops
peso_total_kg = (peso_celulares + peso_laptops) / 1000

print("=" * 70)
print("--- Desglose del Envio ---".center(70))
print("=" * 70)
print(f"{'Cantidad de Celulares enviados:':<31} {f'{celulares} Celulares':<15}{f'${precio_celulares:>10,.2f}':>12} dolares.")
print(f"{'Cantidad de Laptops enviadas:':<31} {f'{laptops} Laptops':<15}{f'${precio_laptops:>10,.2f}':>12} dolares.")
print(f"{'Total:':<31} {f'{total_articulos} articulos':<15}{f'${valor_total:>10,.2f}':>12} dolares.")
print(f"{'Peso total del envio:':<31}{peso_total_kg:>15.2f} Kg")
print("-" * 70)
print("Distribuidora Reyes. Un placer atenderle".center(65))
print("-" * 70)