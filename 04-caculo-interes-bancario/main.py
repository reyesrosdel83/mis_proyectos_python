#cálculo de interes ganado según inversión y tiempo
print("=" * 58)
print("Programa de Obtencion de Capital Segun Inversion.")
print("=" * 58)

#entrada de datos
inversion=int(input("Digite el valor de su inversion: "))
interes_anual=float(input("Ingrese el interes anual ofrecido: "))
tiempo_inversion=int(input("Por favor digite el tiempo programado para su inversion: "))

#conversion del porcentaje del interes a decimal
def calculo_intereses(interes):
    valor_intereses=interes /100
    return valor_intereses

#Calcular ganancias correpondientes a un año
def calcular_ganancia(inversion, interes):
    ganancia_anual=inversion * interes
    return ganancia_anual

#calculo de ganancia en el tiempo de la inversion
def ganancia_final(ganancia_anual,tiempo,inversion_inicial):
    ganancia_total=ganancia_anual * tiempo + inversion_inicial
    return ganancia_total

interes_convertid0=calculo_intereses(interes_anual)
ganancia_un_ano=calcular_ganancia(inversion,interes_convertid0)
resultado_final=ganancia_final(ganancia_un_ano,tiempo_inversion,inversion)

#salida de datos formateada
print("=" * 63)
print("---Desglose al termino del plazo de su inversion---".center(58))
print("=" * 63)
print(f"{'Inversion Inicial:':<40} → $ {inversion:>10.2f} dolares")
print(f"{'Tasa de interes anual:':<40} → % {interes_anual:>10.2f} %")
print(f"{'Intereses anuales adquiridos:':<40} → $ {ganancia_un_ano:>10.2f} dolares")
print(f"{'Capital total adquirido:':<40} → $ {resultado_final:>10.2f} dolares")
print("-" * 63)
