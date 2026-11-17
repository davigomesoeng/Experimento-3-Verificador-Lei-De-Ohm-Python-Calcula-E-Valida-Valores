# Experimento-3-Verificador-Lei-De-Ohm-Python-Calcula-E-Valida-Valores

## 📝 Sobre o Projeto

Este é o Experimento 3 da minha jornada de estudos. Após montar e medir circuitos no Tinkercad, agora desenvolvi um programa em Python para **verificar se os valores de Tensão, Resistência e Corrente estão corretos de acordo com a Lei de Ohm**. Usei o meu próprio código simples — vou melhorá-lo aos poucos conforme avanço nos estudos!

---

## 🧠 Conceito Utilizado

> **Lei de Ohm: U = R × I**
> - U = Tensão (Volts)
> - R = Resistência (Ohms)
> - I = Corrente (Amperes)

O programa pede os três valores ao usuário e confere se U é realmente igual ao produto de R por I. Se bater, confirma que os valores estão certos; senão, avisa que há inconsistência.

---

## 💻 Código Fonte

print(" -- Cálculos de Física -- ")
U = float(input("Digite o valor da Voltagem em Volts: "))
R = float (input("Digite o valor da Resistência em Ohm: "))
I = float(input("Digite o valor da corrente em Amperes: "))

#URI = U . R = I
if U == R * I:
 print ("Valor está cravado corretamente!")
else:
 print ("Valor não foi cravado corretamente!")

