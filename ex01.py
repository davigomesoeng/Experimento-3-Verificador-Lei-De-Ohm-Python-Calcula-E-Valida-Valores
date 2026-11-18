print("=" * 45)
print("⚡ VERIFICADOR — LEI DE OHM")
print("=" * 45)
print("Digite 0 no valor que você quer CALCULAR.\n")

# Entrada dos valores
tensao = float(input("Digite a TENSÃO em Volts (V): "))
resistencia = float(input("Digite a RESISTÊNCIA em Ohms (Ω): "))
corrente = float(input("Digite a CORRENTE em Amperes (A): "))

print("-" * 45)

# Lógica: se um valor for 0, calcula ele
if tensao == 0 and resistencia > 0 and corrente > 0:
    tensao = resistencia * corrente
    print(f"✅ Tensão calculada: V = {tensao:.4f} V")

elif resistencia == 0 and tensao > 0 and corrente > 0:
    resistencia = tensao / corrente
    print(f"✅ Resistência calculada: R = {resistencia:.2f} Ω")

elif corrente == 0 and tensao > 0 and resistencia > 0:
    corrente = tensao / resistencia
    print(f"✅ Corrente calculada: I = {corrente:.6f} A  ({corrente * 1000:.2f} mA)")

# Se os três valores foram dados, verifica se estão corretos
elif tensao > 0 and resistencia > 0 and corrente > 0:
    calculado = resistencia * corrente
    diferenca = abs(tensao - calculado)
    
    print(f"Você informou:")
    print(f"  V = {tensao} V  |  R × I = {calculado:.4f} V")
    
    if diferenca < 0.001:  # pequena tolerância por causa de números decimais
        print("✅ Os valores estão CORRETOS! Lei de Ohm confirmada: V = R × I")
    else:
        print(f"⚠️ Inconsistência! A diferença é de {diferenca:.4f} V")
        print(f"   Para R = {resistencia} Ω e I = {corrente} A,")
        print(f"   o valor esperado de V é: {calculado:.4f} V")

else:
    print("❌ Erro: valores insuficientes. Pelo menos 2 valores devem ser maiores que zero.")

print("\n💡 Lei de Ohm: V = R × I")
print("-" * 45)