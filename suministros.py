dias = int(input("¿Cuántos días durará el viaje?: "))
personas = int(input("¿Cuántas personas viajarán?: "))
comida_disponible = int(input("¿Cuántas unidades de comida tienen?: "))

consumo_diario_p = 3

comida_necesaria = dias * personas * consumo_diario_p

diferencia = comida_disponible - comida_necesaria

