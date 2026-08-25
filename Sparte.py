print(f"Días de viaje: {dias}")
print(f"Personas: {personas}")
print(f"Comida disponible: {comida_disponible} unidades")
print(f"Comida necesaria: {comida_necesaria} unidades")

if diferencia >= 0:
    print(f"Los suministros son suficientes.")
    print(f"Comida restante: {diferencia} unidades")
else:
    print(f"Los suministros no son suficientes.")
    print(f"Faltan: {abs(diferencia)} unidades")