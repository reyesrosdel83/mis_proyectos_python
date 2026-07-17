#programa calculo de pago por horas
print("=" * 40)
print("--- ingreses su datos para el calculo---".center(40))
print("=" * 40)

VALOR_HORAS=12.50


while True:
    try:
        horas_trabajadas=float(input("ingrese la cantidad de horas trabajadas: "))
        if horas_trabajadas < 0:
            raise ValueError("La cantidad de horas no puede ser negativa.")


    except ValueError as e: 
        if "La cantidad de horas no puede ser negativa." in str(e):
        # Aquí atrapamos tanto el error de texto ("hola") como nuestras validaciones lógicas
          print(f"Error: {e}\n")
        else:
          print("Error: Has ingresado letras o caracteres no válidos. Por favor, ingresa solo números (ej: 40 o 35.5).\n")

    else:
        break

pago=horas_trabajadas * VALOR_HORAS

print()
print("=" * 40)
print("--- desglose de pago ---".center(40))
print("=" * 40)
print(f"valor por cada hora:  ${VALOR_HORAS:.2f} dolares.")
print(f"Horas trabajadas:     {horas_trabajadas} horas.")
print("-" * 40)
print(f"Usted debe cobrar:    ${pago:,.2f} dolares.")
print("-" * 40)
