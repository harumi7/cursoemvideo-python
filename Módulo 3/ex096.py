def area(largura, comprimento):
    return largura * comprimento


print("*** Controle de terrenos ***")

larg = float(input("Largura do terreno (m): "))
comp = float(input("Comprimento do terreno (m): "))
area_terreno = area(larg, comp)
print(f"A área de um terreno {larg:.2f}x{comp:.2f} é de {area_terreno:.2f}m².")
