print("digite um 0 para parar")
val = int(input("\nInforme um valor: "))
cont_pos = 0
cont_neg = 0
while val > 0 or val < 0:
  val = int(input("\nInforme um valor: "))
  if val > 0:
    cont_pos +=  1
  elif val < 0:
    cont_neg +=  1
else:
  print(f"\nforam informados {cont_pos} número(s) positivo(s) e {cont_neg} número(s) negativo(s).")