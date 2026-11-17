print(" -- Cálculos de Física -- ")
U = float(input("Digite o valor da Voltagem em Volts: "))
R = float (input("Digite o valor da Resistência em Ohm: "))
I = float(input("Digite o valor da corrente em Amperes: "))

#URI = U . R = I
if U == R * I:
 print ("Valor está cravado corretamente!")
else:
 print ("Valor não foi cravado corretamente!")