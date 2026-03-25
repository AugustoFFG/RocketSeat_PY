# Agenda de contatos


#Adiciona contatos na agenda
def adicionarContato(contatos, nomeContato, telefone, email):
    contato = {"contato": nomeContato, "telefone": telefone, "email": email , "favorito": False}

    contatos.append(contato)

    print("Contato adicionado com sucesso!\n")

    return


#Printa os contatos existentes na tela
def printContatos(contatos):
    print("\nSeus contatos são:")
    for indice, contato in enumerate (contatos, start=1):
        status = "*" if contato["favorito"] else " "
        nomeContato = contato["contato"]
        email = contato["email"]
        telefone = contato["telefone"]
        print(f"{indice}. [{status}] {nomeContato}, {telefone}, {email}")

    return


#Edita contatos existentes
def editaContato(contatos, indice, novoNome, telefone, email):
    contatos[indice - 1]["contato"] = novoNome
    contatos[indice - 1]["telefone"] = telefone
    contatos[indice - 1]["email"] = email
    print(f"Contato {indice} alterado para {novoNome}, {telefone}, {email} com sucesso!\n")

    return


#Exclui contatos exitentes
def excluiContato(contatos, indice):
    if 0 < indice <= len(contatos):
        contato = contatos[indice - 1]
        contatos.remove(contato)
        print(f"Contato {indice} excluido com sucesso!\n")
    else:       
        print(f"Contato inexistente\n")

    return


#Favorita contatos existentes
def favoritaContato(contatos, indice):
    contatos[indice - 1]["favorito"] = True
    print(f"Contato {indice} favoritado!\n")

    return


#Lista de contatos, inicialmente vazia
contatos = []

while True:
    print("\n+=+=+=+=+=+=+=+=+=+\nAgenda de codntatos\n+=+=+=+=+=+=+=+=+=+\n")
    print("1. Salvar contato\n2. Editar contato\n3. Excluir contato\n4. Favoritar contato\n5. Ver contatos\n6. Sair")

    try:    
        selecao = int(input("Digite a opção desejada: "))

    except Exception as e:
        print(f"Erro {e}")


    #Opção 1, adiciona contatos
    if selecao == 1:
        nomeContato = input("\nNome do contato a adicionar: ")
        telefone = input("Telefone do contato a adicioar: ")
        email = input("E-mail do contato a adicionar: ")
        adicionarContato(contatos, nomeContato, telefone, email)


    #Opção 2, edita contatos
    if selecao == 2:
        if not contatos:
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n Você ainda não tem contatos salvos\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
            continue

        printContatos(contatos)

        try:
            indice = int(input("Escolha o índice do contato que deseja editar: "))
            
        except Exception as e:
            print(f"Erro {e}")
            continue

        if 0 < indice <= len(contatos):
            novoNome = input("Digite o novo nome do contato: ")
            novoTelefone = input("Digite o novo telefone do contato: ")
            novoEmail = input("Digite o novo e-mail do contato: ")

            editaContato(contatos, indice, novoNome, novoTelefone, novoEmail)  

        else:
            print(f"Contato inexistente\n")
        

    #Opção 3, exclui contatos
    if selecao == 3:
        if not contatos:
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n Você ainda não tem contatos salvos\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
            continue

        printContatos(contatos)

        try:
            indice = int(input("Escolha o indice do contato que deseja excluir: "))
        except Exception as e:
            print(f"Erro {e}")
            continue
        if 0 < indice <= len(contatos):        
            excluiContato(contatos, indice)

        else:
            print(f"Contato inexistente\n")


    #Opção 4, favorita contatos
    if selecao == 4:
        if not contatos:
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n Você ainda não tem contatos salvos\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
            continue

        printContatos(contatos)

        try:
            indice = int(input("Digite o índice do contato que deseja favoritar: "))
        except Exception as e:
            print(f"Erro {e}")
            continue
        if 0 < indice <= len(contatos): 
            favoritaContato(contatos, indice)

        else:
            print(f"Contato inexistente\n")


    #Opção 5, printa contatos
    if selecao == 5:
        if not contatos:
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n Você ainda não tem contatos salvos\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
            continue

        printContatos(contatos)


    #Opção 6, finalizar a agenda de contatos
    if selecao == 6:
        print("\nPrograma finalizado!\n")
        break