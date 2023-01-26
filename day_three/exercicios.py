#/usr/bin/env python

# 1- Numeros pares
print(f"{' exercicio número 1 ':-^30}")
for i in range(1,201):
    if i%2 == 0:
        print(i)


# 2 - Alerta de temperatura
print(f"{' exercicio número 2 ':-^30}")
temp = int(input("Insira a temperatura: \n"))
umd = int(input("Insira a umidade: \n"))
if temp >= 45:
    print("ALERTA!!! Perigo de calor extremo")
elif temp >= 10 and temp < 30:
    print("Normal")
elif temp < 10 and temp > 0:
    print("Frio")
elif temp <= 0:
    print("ALERTA !! Frio Extremo")

if temp*3 >= umd:
    print("ALERTA!! Perigo de calor úmido")

# 3 - Repete vogal
print(f"{' exercicio número 3 ':-^30}")
VOGAIS = "aeiouAEIOU"
word = None
while word != "":
    word = input("Digite uma palavra(ou enter pra sair): ")
    new_word = ""
    for i in word:
        if i in VOGAIS:
            new_word += i*2
        else:
            new_word += i 
    print(''.join(new_word))

