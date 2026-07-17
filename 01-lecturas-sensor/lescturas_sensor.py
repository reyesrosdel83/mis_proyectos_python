# 1. Definimos la función generadora
def filtrar_alertas(lecturas):
    for temp in lecturas:
        if temp >= 22:
            # Encontramos un valor peligroso: pausamos la función y lo entregamos
            yield temp
            # Cuando el programa nos pida el siguiente, la función continuará desde aquí

# 2. Una lista de datos simulados (el "historial" del sensor)
datos_sensor = [23.5, 18.2, 16.5, 24.1, 27.8, 15.1, 19.4, 22.1, 26.3, 17.0,
 21.8, 25.4, 18.9, 16.1, 23.9, 28.0, 14.8, 20.2, 22.7, 25.1,
 17.6, 19.1, 24.5, 26.8, 15.9, 21.3, 22.0, 23.1, 18.4, 27.2,
 16.7, 24.9, 25.8, 19.5, 15.3, 21.0, 23.4, 26.1, 17.3, 18.7,
 22.4, 24.2, 27.5, 16.0, 19.8, 21.5, 23.0, 25.6, 18.1, 14.9,
 26.7, 22.3, 17.5, 20.4, 24.0, 27.9, 15.6, 19.0, 21.2, 23.6,
 25.0, 18.6, 16.3, 24.4, 26.9, 15.0, 20.8, 22.2, 23.3, 17.9,
 27.1, 16.8, 24.8, 25.5, 19.3, 15.5, 21.1, 23.7, 26.4, 17.2,
 18.8, 22.6, 24.3, 27.4, 16.2, 19.7, 21.6, 23.2, 25.9, 18.0,
 15.2, 26.6, 22.5, 17.4, 20.5, 21.7, 27.7, 15.8, 19.2, 22]

# 3. Creamos el objeto generador llamando a la función
alertas_generador = filtrar_alertas(datos_sensor)
total_alertas=0

# 4. Consumimos el generador usando un bucle 'for'
print("-" *40) 
print("--- Iniciando monitoreo de alertas ---")
print("-" *40) 

for alerta in alertas_generador:
    print(f"¡ALERTA! Temperatura crítica detectada: {alerta}°C")
    total_alertas +=1

print()
print("--- Monitoreo finalizado ---".center(40))
print("-" *40)
print(f"Total de alertas detectadas {total_alertas}".center(40))
print("-" *40)