def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


monto1 = float(input("Por favor ingrese el monto total de la compra: "))
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"\nMonto total ingresado: ${monto1:.2f}")
print(f"Descuento aplicado (10% por defecto): ${descuento1:.2f}")
print(f"Monto final a pagar calculado: ${monto_final1:.2f}\n")


monto2 = float(input("Por favor ingrese el monto total de la segunda compra: "))
porcentaje2 = float(input("Por favor ingrese el porcentaje de descuento: "))
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2
print(f"\nMonto total ingresado: ${monto2:.2f}")
print(f"Descuento ingresado a aplicar ({porcentaje2}%): ${descuento2:.2f}")
print(f"Monto final a pagar calculado: ${monto_final2:.2f}")
