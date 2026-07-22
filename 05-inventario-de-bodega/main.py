#programa de inventario en bodega'

#desglose de inventario inicial
STOCK_FRIJOLES=500 #libras
STOCK_ARROZ=750    #libras
STOCK_AZUCAR=672   #libras
STOCK_JABONES=425  #paquetes

#precios de productos
FRIJOLES=1.80 #por cada libra
ARROZ=1.30    #por cada libra
AZUCAR=0.50   #por cada libra
JABON=1.50    #paquete de 3

def pedir_salida(texto):
    while True:
        try:
            return float(input(texto))
        
        except ValueError:
            print("❌ !ERROR!❌ el valor ingresado no es valido")

def valor_venta(venta,valor_producto):
    calculo_de_venta=venta * valor_producto
    return calculo_de_venta

def stock_disponible(stock,venta):
    inventario=stock - venta
    return inventario

#ingresar datos de la venta
salida_frijoles=pedir_salida("Ingrese la cantidad de frijoles vendidos (libras): ")
salida_arroz=pedir_salida("Ingrese la cantidad de arroz vendido (libras): ")
salida_azucar=pedir_salida("Ingrese la cantidad de azucar vendida (libras): ")
salida_jabones=pedir_salida("Ingrese la cantidad de jabones vendidos (paquetes): ")

#venta segun producto
frijoles_vendidos=valor_venta(salida_frijoles,FRIJOLES)
arroz_vendido=valor_venta(salida_arroz,ARROZ)
azucar_vendida=valor_venta(salida_azucar,AZUCAR)
jabones_vendidos=valor_venta(salida_jabones,JABON)

venta_del_dia=(frijoles_vendidos + arroz_vendido + azucar_vendida + jabones_vendidos)

#calculo de stock disponoble
frijoles_en_stock=stock_disponible(STOCK_FRIJOLES,salida_frijoles)
arroz_en_stock=stock_disponible(STOCK_ARROZ,salida_arroz)
azucar_en_stock=stock_disponible(STOCK_AZUCAR,salida_azucar)
jabones_en_stock=stock_disponible(STOCK_JABONES,salida_jabones)

#salida de datos formateada
print("-" * 48)
print("---Desglose de venta---".center(48))
print("-" * 48)
# Encabezado
print(f"{'Producto':<12} {'Cant.':<12} {'Importe':>12}")
print("-" * 48)
# Filas con ancho fijo para que quede en tabla
print(f"{'Frijoles:':<12} {f'{salida_frijoles:.0f}lbs':<12} {f'${frijoles_vendidos:.2f}':>12}")
print(f"{'Arroz:':<12} {f'{salida_arroz:.0f}lbs':<12} {f'${arroz_vendido:.2f}':>12}")
print(f"{'Azucar:':<12} {f'{salida_azucar:.0f}lbs':<12} {f'${azucar_vendida:.2f}':>12}")
print(f"{'Jabón:':<12} {f'{salida_jabones:.0f} paq':<12} {f'${jabones_vendidos:.2f}':>12}")
print("-" * 48)
print(f" La venta total del día es de: ${venta_del_dia:.2f} dolares.")
print("=" * 48)
print("Inventario Disponible".center(48))
print("-" * 48)
print(f"Frijoles: {frijoles_en_stock:.0f} lbs | Arroz: {arroz_en_stock:.0f} lbs")
print(f"Azucar: {azucar_en_stock:.0f} lbs | Jabones: {jabones_en_stock:.0f} paq")
print("=" * 48)
