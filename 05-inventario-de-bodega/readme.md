# 05 - Inventario en Bodega

Programa para control de ventas y stock de una bodega con 4 productos.

## Que hace
1. Pide al usuario la cantidad vendida de frijoles, arroz, azúcar y jabones.
2. Calcula el importe por producto y la venta total del día.
3. Descuenta del stock inicial y muestra el inventario disponible.

## Funciones
- `pedir_salida()` - Valida que el dato ingresado sea un número.
- `valor_venta()` - Calcula venta * precio.
- `stock_disponible()` - Resta venta del stock.

## Formateo de salida
Uso de f-strings con ancho fijo para crear tabla alineada:
- `:<12` alinea a la izquierda
- `:>12` alinea a la derecha
- `:.2f` muestra 2 decimales