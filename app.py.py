########## Pesquisa de satisfação #############
###### valor inicial de cada avaliação, mostrando o total da pesquisa no final #######
excelente = 0
bom = 0
ruim = 0

###_Pergunta quantas pessoas iram ser entrevistadas_####
while True:
    pessoas = int(input(f"\n Quantas pessoas serão entrevistadas? "))

    ### "range" é definido pela pergunta de quantas pesssoa serão entrevistadas ###
    for i in range(1, pessoas + 1):
        print(f"\n--- Entrevistado {i} ---")

        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        print("\nOpções de atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")

        opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))

    ####### Verifica a opinião do Usuário ###########
        if opiniao == 1:
            excelente += 1
        elif opiniao == 2:
            bom += 1
        elif opiniao == 3:
            ruim += 1
        else:
            print("Opção inválida!")

######### ##### Resultado final ##### ##################

    print("\n========== RESULTADO DA PESQUISA ==========")
    print(f"Quantidade de respostas Excelentes: {excelente}")
    print(f"Quantidade de respostas Boas: {bom}")
    print(f"Quantidade de respostas Ruins: {ruim}")
    

####### Pergunta se ira continuar apos o total X de pesssoas ########

    continuar = input("\nDeseja realizar uma nova pesquisa? (S/N): ").strip().lower()

    if continuar == "n":
        print("Pesquisa finalizada!")
        break


