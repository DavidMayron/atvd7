# 1

número_1 = input('Primeiro número: ')
número_2 = input('Segundo número: ')

if número_1 > número_2:
    print(f'{número_1} é o maior!')
elif número_1 < número_2:
    print(f'{número_2} é o maior!')

# 2
valor = input("digite um valor:")
if valor > "0":
    print("o valor é positivo")
elif valor < "0":
    print("o valor é negativo")
else:
    print("o valor é zero")

#3
sexo = input("digite F ou M:")
if sexo == "F":
    print("feminino")
elif sexo == "M":
    print("masculino")
else:
    print("sexo inválido")

#4
letra = input("digite uma letra:")
if letra in "aeiouAEIOU":
    print("vogal")
else:
    print("consoante")


 #5

nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))

media = (nota1 + nota2
         ) 
if media >= 7:
    print("aprovado")
elif media >= 5:
        print("recuperação")
else:
 print("reprovado")

if media == 10:
    print("aprovado com distinção")
 
 #6

n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))
n3 = float(input("digite o terceiro numero:"))
if n1 > n2 and n1 > n3:
    print("o numero", n1, "é o maior")
elif n2 > n1 and n2 > n3:
        print("o numero", n2, "é o maior")
else:
            print("o numero", n3, "é o maior")

#7
n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))
n3 = float(input("digite o terceiro numero:"))

maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print("o maior numero é:", maior)
print("o menor numero é:", menor)

#8
p1 = input("digite o preco do produto 1:")
p2 = input("digite o preco do produto 2:")
p3 = input("digite o preco do produto 3:")

menor = p1
if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3

print("o menor preco é:", menor)

#9
n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))
n3 = float(input("digite o terceiro numero:"))

lista = [n1, n2, n3]

lista.sort()
print("os numeros em ordem crescente são:", lista)

#10
turno = input("digite M para matutino, V para vespertino ou N para noturno:")
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Turno inválido.")

#11
salario = float(input("digite seu salario:"))
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
elif salario > 1500:
    percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento
print("salario antes do reajuste:R$", salario)
print("percentual de aumento aplicado:R$", percentual, "%")
print("valor do aumento:R$", aumento)
print("novo salario, apos o aumento:R$", novo_salario)

#12
valor_hora = float(input("digite o valor da hora:"))
horas_trabalhadas = float(input("digite o numero de horas trabalhadas:"))
salario_bruto = valor_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto = 0
elif salario_bruto <= 1500:
    desconto = 5
elif salario_bruto <= 2500:
        desconto = 10
else:
   desconto = 20
   valor_desconto = salario_bruto * desconto / 100

   salario_liquido = salario_bruto - valor_desconto
   print("salario bruto:R$", salario_bruto)
   print("desconto aplicado:R$", desconto, "%")

#13

dia = int(input("digite um numero de 1 a 7:"))
if dia == 1:
    print("domingo")
if dia == 2:
    print("segunda")
if dia == 3:
    print("terça")
if dia == 4:
    print("quarta")
if dia == 5:
    print("quinta")
if dia == 6:
    print("sexta")
if dia == 7:
    print("sabado")
else:
    print("valor invalido")

#14
n1 = float(input("digite sua primeira nota"))
n2 = float(input("digite sua segunda nota "))

media = (n1 + n2) 

if media >=5:
     print("aprovado")
if media <=5:
     print("reprovado")

if media >=9.0:
    print("A")
    
if media >=7.5:
    print("B")
    
if media >=6.0:
    print("C")

if media <=6.0:
    print("D")
  
if media <=4.0:
    print("E")

#15

l1 = ("digite o valor do lado:")
l2 = ("digite o valor do outro lado:")
l3 = ("digite o valor do outro lado:")

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):

 print("forma um triangulo")

 if l1 == l2 == l3:
     print("triangulo equilatero")
 if l1 == l2 or l1 == l3 or l2 == l3:
     print("triangulo  Isósceles")
 if l1 != l2 or l3 != l1 or l2 != l3:
     print("triangulo  Escaleno")

    #16 

import math 

a = int(input("digite o valor de a"))

if a == 0:
    print("a equacao nao e de primeiro grau")

else:

 b = int(input("digite o valor de b"))
c = int(input("digite o valor de c"))

delta = (b ** 2) - (4 * a * c)

print ("delta =",delta)

if delta <0:
    print("a equacao nao tem raizes reais")
elif delta ==0:
    raiz = -b / (2 * a)
    print("raiz =", raiz)

else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)

        print("A equação possui duas raízes reais")
        print("Raiz 1 =", raiz1)
        print("Raiz 2 =", raiz2)

#17
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto")

else:
    print("O ano não é bissexto")
