def ler_entrada_de_usuario():
    temp = input("Diga sua temperatura: ")
    umd = input("Diga sua umidade: ")
    return temp, umd



if __name__ == "__main__":
    tmp, umd = ler_entrada_de_usuario()
    print(tmp, umd)