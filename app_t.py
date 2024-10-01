#Lista de frutas
frutas = ["Melacia", "Cajú", "Manga", "Laranja", "Morango"," Uva", "Banana"]

"Exibir a lista"
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}.")

try:
    #Usuário informa o índice
    indice = int(input("Informe o índice da fruta que deseja excluir:"))
    confirmacao = input(f"Deseja excluir a fruta {frutas[indice]}? Digite 'sim' para confirmar. ")

    if confirmacao == "sim":
        del(frutas[indice])
        print("Fruta deletada com sucesso.")
    else:
        ...
except Exception as e:
    print(f"Não foi possível deletar a fruta. {e}.")
finally:
    #Exibe a lista
    for i in range(len(frutas)):
        print(f"Índice {i}: {frutas[i]}.")