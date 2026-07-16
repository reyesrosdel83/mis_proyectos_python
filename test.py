print("-" * 70)
print("Programa de Inventario y Ventas".center(65))
print("-" * 70)

#precio de los productos
PRCELULARES=320 #dolares
PRLAPTOPS=1400  #dolares

#peso de los productos
PSCELULARES=204 #g
PSLAPTOPS=2300   #2,3 Kg

def pedir_dato(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("--- Valor no valido, ingrese un numero entero ---")

celulares_enviados=pedir_dato("Ingrese la cantidad de Celulares que se envian: ")
laptops_enviadas=pedir_dato("Ingrese la cantidad de Laptops que se envian: ")

def precio_de_cada_articulo(articulo,precio):
    precio_equipos=articulo * precio
    return precio_equipos


def peso_de_cada_articulo(articulo,peso):
    peso_equipos=articulo * peso
    return peso_equipos

def peso_total(celulares,laptops):
    peso_neto=(celulares + laptops) / 1000 
    return peso_neto

def total(articulo1,articulo2):
    total_equipos_vendidos=articulo1 + articulo2
    return total_equipos_vendidos

total_equipos_vendidos=total(celulares_enviados,laptops_enviadas)#total de equipos vendidos entre ambos articulos
peso_celulares=peso_de_cada_articulo(celulares_enviados,PSCELULARES)
peso_laptops=peso_de_cada_articulo(celulares_enviados,PSLAPTOPS)
peso_del_envio=peso_total(peso_celulares,peso_laptops)
precio_celulares=precio_de_cada_articulo(celulares_enviados,PRCELULARES)
precio_laptops=precio_de_cada_articulo(celulares_enviados,PRLAPTOPS)
valor_total_del_envio=total(precio_celulares,precio_laptops)


print("=" * 70)
print("--- Desglose del Envio ---".center(70))
print("=" * 70)
print(F"{'Cantidad de Celulaes enviados:':<31} {f'{celulares_enviados} Celulares':<15}{f'${precio_celulares:>10,.2f}':>12} dolares.")
print(F"{'Cantidad de Laptops enviadas:':<22}   {f'{laptops_enviadas} Laptops':<15}{f'${precio_laptops:>10,.2f}':>12} dolares.")
print(f"{'Total:':<29} {f'{total_equipos_vendidos} articulos':>14}{f'${valor_total_del_envio:>8,.2f}':>14} dolares.")
print(f"{'Peso total del envio:':<22}{peso_del_envio:>15} Kg")
print("-" * 70)
print("Distribuidora Reyes. Un placer atenderle".center(65))
print("-" * 70)