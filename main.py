print("Olá,")
print("Esse é um programa que criptografa mensagens.")
print("Você deve digitar a mensagem que quer que seja criptografada ou descriptografada")
print("Observação: Acentos, números ou caracteres especiais não serão criptografados, somente letras de A a Z")

#Utilizado tabela de cores ANSI nativa do Python para mudar algumas cores afim de deixar o programa visualmente mais legível.
def criptography(): #Função criptografia
    while True: #Loop infinito

        try: #Tenta executar o menu
            menu = int(input("\n\nMenu:\n" #Menu de opções
                "O que deseja fazer ?\n"
                "1. Digitar a sua mensagem para criptografar/descriptografar \n"
                "2. Visualizar autoria\n"
                "3. Sair do programa\n"
                "Digite o número da opção que deseja: "))

        except ValueError: #Tratamento de erro, se apresentar o erro de ValueError (Digitar uma letra no input "int" por exemplo.
            print(f"\n\033[1;31mOpção inválida, reiniciando o menu...\033[0;0m")
            continue #Reinicia a inserção de dados

        if menu == 1: #Se opção = digitar a mensagem para criptogragar/descriptografar
            #inputs
            try:
                text = input('Digite a mensagem que deseja: ')
                turnover = int(input('Digite o número correspondente as rotações: '))
                option = input('Escolha D para decriptografar ou C para criptografar o texto: ')
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #alfabeto
                result = '' #Variável vazia para salvar o texto
                text = text.upper() #Converte todo o texto em letras maíusculas
                for letter in text: #Para cara letra do texto
                    if letter in alphabet: #Se a letra no alfabeto
                        i = alphabet.find(letter) #obtem o numero criptofrafado/descriptografado da letra
                        if option == 'D': #Se opção for Descriptografar
                            i = i + turnover
                        elif option == 'C': #Se opção for Criptografar
                            i = i - turnover
                    if i >= len(alphabet): #Se o valor de i for maior do que o alfabeto
                        i = i - len(alphabet)
                    elif i < 0: #Se o valor de i for menor do que 0
                        i = i + len(alphabet)
                        #Concatena a letra correspondente a I, convertido
                        result = result + alphabet[i]
                    else:
                        result = result + letter #Não efetua criptografia

                #Resultados
                if option == 'D': #Se inicialmente a opção é descriptografar
                    print('O texto criptografado é ', result)
                elif option == 'C': #Se inicialmente a opção é criptografar
                    print('O texto decriptado é ', result)
                else: #Se não for nenhuma das opções, reinicia a inserção de dados
                    print("\n\033[1;31mOpção inválida, reiniciando inserção de dados...\033[0;0m")
                continue
            except UnboundLocalError: #Quando digitado caracteres diferentes do previsto no input text o "Nome local é referenciado, mas não vinculado a um valor."
                print(f"\n\033[1;31mNão digite caracteres especiais como {text}, reiniciando a inserção de dados\033[0;0m")
                continue #Reinicia a inserção de dados
            except ValueError: #Digitar algo diferente de numero em um campo inteiro (int)
                print(f"\n\033[1;31mNão digite letras no número de rotações, reiniciando inserção de dados\033[0;0m")
                continue #Reinicia a inserção de dados

        elif menu == 2: #Se opção do menu for 2, mostra os créditos, apenas para popular o menu
            print("Desenvolvedor: Victor Hugo Bier Silva")
            print("GitHub: https://github.com/bierTI-dev")
            print("LinkedIn: https://www.linkedin.com/in/victor-bier/")
            continue

        elif menu == 3: #Se opção do menu for 3, encerra o programa
            print("Encerrando o programa...")
            break

        else: #Se opção diferente de 1, 2 ou 3, reinicia o menu
            print(f"\n\033[1;31mOpção inválida, reiniciando o menu...\033[0;0m")
            continue

#Programa principal
criptography()