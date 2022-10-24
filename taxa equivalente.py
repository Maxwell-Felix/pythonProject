# como fazer taxa equivalente
# a formula segue por [(1 + taxa)elevado a: prazo que quero/prazo que tenho - 1] x 100
def main():

    int taxa,
taxa = input("Digite a taxa: ")
prazo_quero = input("Digite o prazo que deseja")
prazo_tenho = input("Digite o prazo que possui")
resultado = [(1 + taxa) ** prazo_quero / prazo_tenho - 1] * 100
print("Resultado é: ", resultado)

main()
