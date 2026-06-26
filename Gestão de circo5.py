#Bibliotecas utilizadas:
import pickle
import os
# Organização da lista de artistas: [nome, telefone e especialidades]
artistas = {}
try:
    arqArt = open('artistas.txt', 'rt', encoding='utf-8')
    for linha in arqArt:
        linha = linha.strip()
        if linha:
            campos = linha.split(',')
            idArt = campos[0]
            nome = campos[1]
            telefone = campos[2]
            tamanho = len(campos) - 3
            especialidades = []
            for i in range(tamanho):
                especialidades.append(campos[i+3]) 
            artistas[idArt] = [nome, telefone, especialidades]
    arqArt.close()
except:
    artistas = {'1': ["Looey", "1111-8888", ["Truque com balões", "Truques de mágica"]],
                '2': ["Yatta", "2222-9999", ["Acrobata", "Equilibrista"]],
                '3': ["Blot", "3333-0000", ["Mímico", "Ventriloquista"]],
                '4': ["Eclipsa", "4444-7777", ["A menina lobo", "Contorcionista"]],
                '5': ["Shrimpo", "5555-6666", ["O menino camarão", "Acrobata"]]}
    arqArt = open('artistas.txt', 'wt', encoding='utf-8')
    for idArt, dados in artistas.items():    
        arqArt.write(f"{idArt},{dados[0]},{dados[1]},{dados[2]}\n")
    arqArt.close()
#Organização dos apresentaçãos: [nome, data, Descrição e id dos artistas participantes]
apresentacoes = {}
try:
    arqApre = open('apresentações.txt', 'rt', encoding='utf-8')
    for linha in arqApre:
        linha = linha.strip()
        if linha: 
            campos = linha.split(',')
            idApre = campos[0]
            nome = campos[1]
            descricao = campos[2]
            tamanho = len(campos) - 3
            artists = []
            for i in range(tamanho):
                artists.append(campos[i+3])
            apresentacoes[idApre] = [nome, descricao, artists]
    arqApre.close()
    
except:
    apresentacoes = {'1':["Show de abertura",
             "Os artistas se apresentam e mostram um pouco do que sabem fazer", ["1", "2", "3", "4", "5"]],
                     '2': ["Shrimpo e Eclipsa",
             "Gato e rato entre Eclipsa e Shrimpo", ["5", "4"]],
                     '3': ["Balões do Looey",
             "Looey mostra suas habilidades com balões para Blot e Blot Jr", ["1", "3"]],
                     '4': ["Desafios da Yatta",
             "Yatta faz desafios de equilíbrio e de acrobacias em frete ao público", ["2"]],
                     '5': ["Blot Jr responde",
             "Yatta e Looey fazem perguntas ao Blot Jr", ["3", "2", "1"]]}
    arqApre = open('apresentações.txt', 'wt', encoding='utf-8')
    for idApre, dados in apresentacoes.items():  
        arqApre.write(f"{idApre},{dados[0]},{dados[1]},{dados[2]}\n")
    arqApre.close()
#Organização dos sessãos: [Valor, data, hora, lista com id das apresentações]
sessao = {}
try:
    arqSessao = open('sessões.txt', 'rt', encoding='utf-8')
    for linha in arqSessao:
        linha = linha.strip()
        if linha:
            campos = linha.split(',')
            idSessao = campos[0]
            valor = int(campos[1])
            data = campos[2]
            tamanho = len(campos) -3
            nomeShow = []
            for i in range(tamanho):
                nomeShow.append(campos[i+3])
            sessao[idSessao] = [valor, data, nomeShow]
    arqSessao.close()
except:
    sessao = {'1': [15.00, "11/07", "16:00", ['1', '2', '3']],
              '2': [12.00, "11/07", "18:00", ['4', '5']],
              '3': [15.00, "11/07", "19:30", ['2', '3', '5']]}
    arqSessao = open('sessões.txt', 'wt', encoding='utf-8')
    for idSessao, dados in sessao.items():
        arqSessao.write(f"{idSessao},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
    arqSessao.close()
#Organização dos ingressos: [idcliente, idsessão, meia/inteira, Cliente ativo/desativo]
ingressos = {}
try:
    arqTicket = open('ingressos.txt', 'rt', encoding='utf-8')
    for linha in arqTicket:
        linha = linha.strip()
        if linha:
            campos = linha.split(',')
            idTicket = campos[0]
            idCliente = campos[1]
            idSessao = campos[2]
            meiaInt = campos[3]
            ClientStats = campos[4]
            ingressos[idTicket] = [idCliente, idSessao, meiaInt, ClientStats]
    arqTicket.close()
except:
    ingressos = {'1': ['1', '1', '0', '0'],
                 '2': ['2', '2', '1', '0'],
                 '3': ['3', '3', '0', '1']}
    arqTicket = open('ingressos.txt', 'wt', encoding='utf-8')
    for idTicket, dados in ingressos.items():
        arqTicket.write(f"{idTicket},{dados[0],dados[1],dados[2], dados[3]}\n")
    arqTicket.close()
#Início dos CRUDS
inicio = " "
while inicio != "0":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("___________________________________________________________________________")
    print("||                                                                       ||")
    print("|| Bem-vindo ao programa para a gestão do seu circo, totalmente digital. ||")
    print("||                                                                       ||")
    print("||_______________________________________________________________________||")
    print("||                            O que quer ver?                            ||")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~                              1 - Artistas                             ~~")
    print("[[                                                                       ]]")
    print("[[                              2 - Apresentações                        ]]")
    print("§§                                                                       §§")
    print("§§                              3 - Sessões                              §§")
    print("$$                                                                       $$")
    print("$$                              4 - Bilheteria                           $$")
    print("!!                                                                       !!")
    print("!!                              5 - Relatório                            !!")
    print("//                                                                       //")
    print("//                              6 - Sobre o sistema                      //")
    print("XX                                                                       XX")
    print("XX                              0 - Sair                                 XX")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()
    inicio = input("Escolha uma opção: ")
    if inicio == "1":
        art = "10"
        while art != "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~                          O que deseja fazer                           ~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~                         1 - Adicionar artista                         ~~")
            print("~~                                                                       ~~")
            print("~~                         2 - Atualizar artista                         ~~")
            print("~~                                                                       ~~")
            print("~~                         3 - Pesquisar artista                         ~~")
            print("~~                                                                       ~~")
            print("~~                         4 - Excluir artista                           ~~")
            print("~~                                                                       ~~")
            print("~~                         5 - Mostrar todos                             ~~")
            print("~~                                                                       ~~")
            print("~~                         0 - Voltar                                    ~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            art = input("Escolha uma opção ")
            if art == "0":
                continue
            elif art == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                           Adicionar artista                           ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                idArt = input("Digite aqui o id do novo artista: ")
                if idArt in artistas:
                    subs = False
                    while subs == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~              Esse id já está cadastrdo em outro artista.              ~~")
                        print("~~                          Deseja subscrever?                           ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                           1 - Sim                                     ~~")
                        print("~~                                                                       ~~")
                        print("~~                           2 - Não                                     ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print()
                        subsArt = input("Escolha uma opção: ")
                        if subsArt == '1':
                            subs = True
                        elif subsArt == '2':
                            idArt = input("Digite aqui o id do novo artista: ")
                            if idArt in artistas:
                                continue
                            else:
                                subs = True
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                   Opção inválida, tente novamente.                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                print()
                nome = input("Digite o nome do novo artista: ")
                print()
                fone = input("Digite o telefone desse artista (Apenas números): ")
                print()
                esp = input("Digite a 1° especialidade do artista: ")
                print()
                esp2 = input("Digite aqui a segunda especialidade do artista (Caso não tenha, digite '0'): ")
                if esp2 != '0':
                    listaEsp = [esp, esp2]
                else:
                    listaEsp = [esp]
                artistas[idArt] = [nome, fone, [listaEsp]]
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                       Artista adicionado com sucesso!                 ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                esc = input("Precione <ENTER> para continuar: ")
                print()
            elif art == "2":
                upArt = '10'
                while upArt != '0': 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                   Qual artista você quer atualizar?                   ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                        Digite o id do artista                         ~~")
                    print("~~                                                                       ~~")
                    print("~~                           0 - Voltar                                  ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    upArt = input("Escolha uma opção: ")
                    print()
                    if upArt == '0':
                        continue
                    elif upArt in artistas:
                        if len(artistas[upArt][2]) == 2:
                            update = "10"
                            while update != "0":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                #os.system("cls || clear") == testa ambos e exibe o que funcionar
                                print()
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print(f"~~                O que deseja atualizar de {artistas[upArt][0]}?         ")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("~~                                                                       ~~")
                                print("~~                           1 - Nome                                    ~~")
                                print("~~                                                                       ~~")
                                print("~~                           2 - Telefone                                ~~")
                                print("~~                                                                       ~~")
                                print("~~                           3 - 1° Especialidade                        ~~")
                                print("~~                                                                       ~~")
                                print("~~                           4 - 2° Especialidade                        ~~")
                                print("~~                                                                       ~~")
                                print("~~                           0 - Voltar                                  ~~")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print()
                                update = input("Escolha uma opção: ")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                if update == "1":
                                    artistas[upArt][0] = input("Digite aqui o novo nome: ")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                    Nome do artista foi atualizado!                    ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                                elif update == "2":
                                    fone = input("Digite o novo telefone (Apenas números): ")
                                    artistas[upArt][1] = fone
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~             Número de telefone do artista foi atualizado!             ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                                elif update == "3":
                                    artistas[upArt][2][0] = input("Digite aqui a nova 1° especialidade: ")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                1° especialidade do artista atualizada!                ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                                elif update == "4":
                                    artistas[upArt][2][1] = input("Digite aqui a nova 2° especialidade: ")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                2° especialidade do artista atualizada!                ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                                elif update == "0":
                                    continue
                                else:
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                   Opção inválida, tente novamente.                    ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                        elif len(artistas[upArt][2]) == 1:
                            update = "10"
                            while update != "0":
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print(f"~~                O que deseja atualizar de {artistas[upArt][0]}?         ")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("~~                                                                       ~~")
                                print("~~                           1 - Nome                                    ~~")
                                print("~~                                                                       ~~")
                                print("~~                           2 - Telefone                                ~~")
                                print("~~                                                                       ~~")
                                print("~~                           3 - Especialidade                           ~~")
                                print("~~                                                                       ~~")
                                print("~~                           0 - Voltar                                  ~~")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print()
                                update = input("Escolha uma opção: ")
                                if update == "1":
                                    artistas[upArt][0] = input("Digite aqui o novo nome: ")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                    Nome do artista foi atualizado!                    ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                                elif update == "2":
                                    artNumb = False
                                    while artNumb == False:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        fone = input("Digite o novo telefone (Apenas números): ")
                                        if fone.isdigit():
                                            
                                            #Adicionar '-' antes dos 4 últimos dígitos.
                                            
                                            artNumb = True
                                            artistas[upArt][1] = fone
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("~~             Número de telefone do artista foi atualizado!             ~~")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        else:
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("~~               Inválido, digite apenas números.                        ~~")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            esc = input("Precione <ENTER> para continuar: ")
                                elif update == "3":
                                    artistas[upArt][2] = input("Digite aqui a nova especialidade: ")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                1° especialidade do artista atualizada!                ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                                elif update == "0":
                                    continue
                                else:
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("~~                   Opção inválida, tente novamente.                    ~~")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                   Opção inválida, tente novamente.                    ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        esc = input("Precione <ENTER> para continuar: ")
            elif art == "3":
                idPesc = '10'
                while idPesc != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                    Módulo de pesquisa de artista?                     ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                        Digite o id do artista                         ~~")
                    print("~~                                                                       ~~")
                    print("~~                           0 - Voltar                                  ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    idPesc = input("Escolha uma opção: ")
                    if idPesc != '0':
                        if idPesc in artistas:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Aqui está o contato solicitado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            if len(artistas[idPesc][2]) == 2:
                                print(f"~~                        {artistas[idPesc][0]}                       ")
                                print(f"~~                        {artistas[idPesc][1]}                       ")
                                print(f"~~                        {artistas[idPesc][2][0]}                    ")
                                print(f"~~                        {artistas[idPesc][2][1]}                    ")
                                print("~~                                                                     ")
                            elif len(artistas[idPesc][2]) == 1:
                                print(f"~~                        {artistas[idPesc][0]}                       ")
                                print(f"~~                        {artistas[idPesc][1]}                       ")
                                print(f"~~                        {artistas[idPesc][2]}                       ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                        Artista não cadastrado.                        ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif idPesc == '0':
                        continue
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                   Opção inválida, tente novamente.                    ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        esc = input("Precione <ENTER> para continuar: ")
            elif art == "4":
                delet = '10'
                while delet != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                          Exclusão de artista                          ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~               Digite o Id do artista que queira escluir               ~~")
                    print("~~                                                                       ~~")
                    print("~~                               0 - Voltar                              ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    delet = input("Escolha uma opção: ")
                    if delet != '0':
                        if delet in artistas:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(f"~~                   Quer mesmo excluir {artistas[delet][0]}              ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                            1 - Sim                                    ~~")
                            print("~~                                                                       ~~")
                            print("~~                            2 - Não                                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            mesmo = input("Escolha uma opção: ")
                            if mesmo == "1":
                                del artistas[delet]
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("~~                          Exclusão concluida.                          ~~")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif mesmo == "2":
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("~~                          Exclusão cancelada.                          ~~")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                esc = input("Precione <ENTER> para continuar: ")
                                continue
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                        Artista não cadastrado                         ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif delet == '0':
                        continue
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                   Opção inválida, tente novamente.                    ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        esc = input("Precione <ENTER> para continuar: ")
            elif art == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~               Aqui estão todos os artistas cadastrados                ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for artista in artistas:
                    print(f"~~       {artistas[artista]}          ")
                    print("~~                                                                         ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                esc = input("Precione <ENTER> para continuar: ")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                   Opção inválida, tente novamente.                    ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                esc = input("Precione <ENTER> para continuar: ")
    elif inicio == '2':
        esp = "10"
        while esp != "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("[[                          O que deseja fazer?                          ]]")
            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("[[                                                                       ]]")
            print("[[                       1 - Adicionar apresentação                      ]]")
            print("[[                                                                       ]]")
            print("[[                       2 - Atualizar apresentação                      ]]")
            print("[[                                                                       ]]")
            print("[[                       3 - Pesquisar apresentação                      ]]")
            print("[[                                                                       ]]")
            print("[[                       4 - Excluir apresentação                        ]]")
            print("[[                                                                       ]]")
            print("[[                       5 - Mostrar todos                               ]]")
            print("[[                                                                       ]]")
            print("[[                       0 - Voltar                                      ]]")
            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print()
            esp = input("Escolha uma opção: ")
            if esp == '0':
                continue
            elif esp == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[                         Adicionar apresentação                        ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print()
                idEsp = input("Digite aqui o id da nova apresentação: ")
                if idEsp in apresentacoes:
                    subs = False
                    while subs == False:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[           Esse id já está cadastrado em outra apresentação.           ]]")
                        print("[[                          Deseja subscrever?                           ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                               1 - Sim                                 ]]")
                        print("[[                                                                       ]]")
                        print("[[                               2 - Não                                 ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print()
                        subEsp = input("Escolha uma opção: ")
                        if subEsp == '1':
                            subs = True
                        elif subEsp == '2':
                            idEsp = input("Digite aqui o id da nova apresentação: ")
                            if idEsp in apresentacoes:
                                continue
                            else:
                                subs = True
                        else:
                            print()
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                   Opção inválida, tente novamente.                    ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                nomeEsp = input("Digite o nome da nova apresentação: ")
                print()
                descEsp = input("Digite aqui a descrição da nova apresentação: ")
                print()
                artQuant = False
                while artQuant == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    quantArt = int(input(f"Digite aqui a quantidade de artistas dessa apresentação (Máximo de {len(artistas)}): "))
                    print()
                    if quantArt <= len(artistas) and quantArt > 0:
                        listArt = []
                        while len(listArt) != quantArt:
                            artEsp = input("Digite o id do artista da nova apresentação: ")
                            print()
                            if artEsp in artistas:
                                listArt.append(artEsp)
                            else:
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[                artista não cadastrado, tente novamente                ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precine <ENTER> para continuar: ")
                        artQuant = True
                    else:
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                 Quantidade inválida, tente novamente.                 ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        esc = input("Precione <ENTER> para continuar: ")
                apresentacoes[idEsp] = [nomeEsp, descEsp, listArt]
                print()
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[                     Nova apresentação adicionado.                     ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                esc = input("Precine <ENTER> para continuar: ")
            elif esp == '2':
                update = '10'
                while update != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                Qual apresentação você quer atualizar?                 ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                      Digite o id da apresentação                      ]]")
                    print("[[                                                                       ]]")
                    print("[[                         0 - Voltar                                    ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print()
                    update = input("Escolha uma opção: ")
                    if update == '0':
                        continue
                    elif update != '0':
                        if update in apresentacoes:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print(f"[[          O que deseja atualizar de {apresentacoes[update][0]}?         ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                           1 - Nome                                    ]]")
                            print("[[                                                                       ]]")
                            print("[[                           2 - Descrição                               ]]")
                            print("[[                                                                       ]]")
                            print("[[                           3 - Artistas                                ]]")
                            print("[[                                                                       ]]")
                            print("[[                           0 - Voltar                                  ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print()
                            upEsp = input("Escolha uma opção: ")
                            if upEsp == '0':
                                continue
                            elif upEsp == '1':
                                apresentacoes[update][0] = input("Digite aqui o novo nome: ")
                                print()
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[            Nome da apresentação foi atualizado com sucesso!           ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif upEsp == '2':
                                apresentacoes[update][1] = input("Digite aqui a nova descrição: ")
                                print()
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[       Nova descrição da apresentação foi atualizada com sucesso!      ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif upEsp == '3':
                                artQuant = False
                                while artQuant == False:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    quantArt = int(input(f"Digite aqui a quantidade de artistas dessa apresentação (Máximo de {len(artistas)}): "))
                                    if quantArt <= len(artistas) and quantArt > 0:
                                        listArt = []
                                        while len(listArt) != quantArt:
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            artEsp = input("Digite o id do artista da nova apresentação: ")
                                            if artEsp in artistas:
                                                listArt.append(artEsp)
                                            else:
                                                print()
                                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                                print("[[                artista não cadastrado, tente novamente                ]]")
                                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                                esc = input("Precine <ENTER> para continuar: ")
                                        artQuant = True
                                    else:
                                        print()
                                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                        print("[[                  Quantidade inválida, tente novamente.                ]]")
                                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                apresentacoes[update][2] = listArt
                                print()
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[     Os artistas dessa apresentação foram atualizados com sucesso!     ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                            else:
                                print()
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[                   Opção inválida, tente novamente.                    ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
            elif esp == '3':
                espPesc = '10'
                while espPesc != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                  Módulo de pesquisa de apresentações                  ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                       Digite o id da apresentação                     ]]")
                    print("[[                                                                       ]]")
                    print("[[                             0 - Voltar                                ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print()
                    espPesc = input("Escolha uma opção: ")
                    if espPesc == '0':
                        continue
                    elif espPesc != '0':
                        if espPesc in apresentacoes:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                  Aqui está a apresentação solicitada!                 ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print(f"[[                  {apresentacoes[espPesc][0]}                           ")
                            print("[[                                                                         ")
                            print(f"[[                  {apresentacoes[espPesc][1]}                           ")
                            print("[[                                                                         ")
                            tamanho = len(apresentacoes[espPesc][2])
                            for i in range(tamanho):
                                print(f"[[                  {artistas[apresentacoes[espPesc][2][i]][0]}              ")
                                print("[[                                                                         ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                      apresentação não cadastrada.                     ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                   Opção inválida, tente novamente.                    ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        esc = input("Precione <ENTER> para continuar: ")
            elif esp == '4':
                delet = '10'
                while delet != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                       Exclusão de apresentações                       ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                      Digite o id da apresentação                      ]]")
                    print("[[                                                                       ]]")
                    print("[[                             0 - Voltar                                ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    delet = input("Escolha uma opção: ")
                    if delet != '0':
                        if delet in apresentacoes:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print(f"[[         Quer mesmo excluir o {apresentacoes[delet][0]}                 ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                            1 - Sim                                    ]]")
                            print("[[                                                                       ]]")
                            print("[[                            2 - Não                                    ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            mesmo = input("Escolha uma opção: ")
                            if mesmo == '1':
                                del apresentacoes[delet]
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[                        Exclusão concluida.                            ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif mesmo == '2':
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[                       Exclusão cancelada                              ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                       apresentação não cadastrada.                    ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif delet == '0':
                        continue
                    else:
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                   Opção inválida, tente novamente.                    ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        esc = input("Precione <ENTER> para continuar: ")
            elif esp == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[             Aqui estão todas as apresentaçãos cadastradas             ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                for apresentacao in apresentacoes:    
                    print(f"[[           {apresentacoes[apresentacao]}                                ")
                    print("[[                                                                         ")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                esc = input("Precione <ENTER> para continuar: ")
            else:
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[                   Opção inválida, tente novamente.                    ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                esc = input("Precione <ENTER> para continuar: ")
    elif inicio == '3':
        sess = '10'
        while sess != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            print("§§                          O que deseja fazer?                          §§")
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            print("§§                                                                       §§")
            print("§§                       1 - Adicionar sessão                            §§")
            print("§§                                                                       §§")
            print("§§                       2 - Atualizar sessão                            §§")
            print("§§                                                                       §§")
            print("§§                       3 - Pesquisar sessão                            §§")
            print("§§                                                                       §§")
            print("§§                       4 - Excluir sessões                             §§")
            print("§§                                                                       §§")
            print("§§                       5 - Mostrar todas                               §§")
            print("§§                                                                       §§")
            print("§§                       0 - Voltar                                      §§")
            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
            print()
            sess = input("Escolha uma opção: ")
            if sess == '0':
                continue
            elif sess == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                print("§§                           Adicionar sessão                            §§")
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                print()
                idSessao = input("Digite aqui o id dessa nova sessão: ")
                if idSessao in sessao:
                    subs = False
                    while subs == False:
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        print("§§              Esse id já está cadastrado em poutra sessão.             §§")
                        print("§§                        Deseja subscraver?                             §§")
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        print("§§                             1 - Sim                                   §§")
                        print("§§                                                                       §§")
                        print("§§                             2 - Não                                   §§")
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        print()
                        subSess = input("Escolha uma opção: ")
                        if subSess == '1':
                            subs = True
                        elif subSess == '2':
                            idSessao = input("Digite aqui o id dessa nova sessão: ")
                            if idSessao in sessao:
                                continue
                            else:
                                subs = True
                        else:
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                    Opção inválida, tente novamente                    §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            esc = input("Precione <ENTER> para continuar: ")
                valSessao = int(input("Digite o valor dessa sessão (Apenas números): "))
                print()
                sessDate = False    
                dataSessao = input("Digite a data para essa sessão (No formato xxyy, apenas com números): ")
                print()
                horaSessao = input("Digite a hora dessa sessão (No formato xxyy, apenas números): ")
                print()
                apreQuant = False
                while apreQuant == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    quantApre = int(input(f"Digite aqui a quantidade de apresentações dessa sessão (Máximo de 3): "))
                    print()
                    if quantApre <= 3 and quantApre > 0:
                        listApre = []
                        while len(listApre) != quantApre:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            espSess = input("Digite o id da apresentação dessa sessão: ")
                            print()
                            if espSess in apresentacoes:
                                listApre.append(espSess)
                            else:
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§             apresentação não cadastrada, tente novamente.             §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precine <ENTER> para continuar: ")
                        apreQuant = True
                    else:
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        print("§§                  Quantidade inválida, tente novamente.                §§")
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        esc = input("Precine <ENTER> para continuar: ")
                sessao[idSessao] = [valSessao, dataSessao, horaSessao, listApre]
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                print("§§                     sessão adicionada com sucesso!                    §§")
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                esc = input("Precine <ENTER> para continuar: ")
            elif sess == '2':
                update = '10'
                while update != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print("§§                    Qual sessão você quer atualizar?                   §§")
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print("§§                        Digite o id do sessão                          §§")
                    print("§§                                                                       §§")
                    print("§§                        0 - Voltar                                     §§")
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print()
                    update = input("Escolha uma opção: ")
                    print()
                    if update == '0':
                        continue
                    elif update != '0':
                        if update in sessao:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                 O que deseja atualizar dessa sessão?                  §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                       1 - Valor                                       §§")
                            print("§§                                                                       §§")
                            print("§§                       2 - Data da sessão                              §§")
                            print("§§                                                                       §§")
                            print("§§                       3 - Hora da sessão                              §§")
                            print("§§                                                                       §§")
                            print("§§                       4 - Apresentações da sessão                     §§")
                            print("§§                                                                       §§")
                            print("§§                       0 - Voltar                                      §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print()
                            upSessao = input("Escolha uma opção: ")
                            if upSessao == '0':
                                continue
                            elif upSessao == '1':
                                sessao[(update)][0] = int(input("Digite o novo valor dessa sessão (Apenas números): "))
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§             Valor dessa sessão foi atualizado com sucesso!            §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif upSessao == '2':
                                sessao[(update)][1] = input("Digite a nova data desse sessão (xx/yy): ")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§            A data dessa sessão foi atualizada com sucesso!            §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif upSessao == '3':
                                sessao[(update)][2] = input("Digite a nova hora dessa sessão (xx:xx horas): ")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§            A hora dessa sessão foi atualizada com sucesso!            §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precine <ENTER> para continuar: ")
                            elif upSessao == '4':
                                apreQuant = False
                                while apreQuant == False:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    quantApre = int(input(f"Digite aqui a quantidade de apresentações dessa sessão (Máximo de 3): "))
                                    print()
                                    if quantApre <= 3:
                                        listApre = []
                                        while len(listApre) != quantApre:
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            espSess = input("Digite o id da apresentação dessa sessão: ")
                                            print()
                                            if espSess in apresentacoes:
                                                listApre.append(espSess)
                                            else:
                                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                                print("§§             apresentação não cadastrada, tente novamente.             §§")
                                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                                esc = input("Precine <ENTER> para continuar: ")
                                        apreQuant = True
                                    else:
                                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                        print("§§                Quantidade extrapolada, tente novamente.               §§")
                                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                        esc = input("Precine <ENTER> para continuar: ")
                                sessao[update][3] = listApre
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§      As apresentações dessa sessão foram atualizadas com sucesso.     §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precine <ENTER> para continuar: ")
                        else:
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                Sessão não cadastrada, tente novamente.                §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            esc = input("Precione <ENTER> para continuar: ")
            elif sess == '3':
                sessaoPesc = '10'
                while sessaoPesc != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print("§§                      Módulo de pesquisa de sessão                     §§")
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print("§§                         Digite o id do sessão                         §§")
                    print("§§                                                                       §§")
                    print("§§                           0 - Voltar                                  §§")
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    sessaoPesc = input("Escolha uma opção: ")
                    if sessaoPesc == '0':
                        continue
                    elif sessaoPesc != '0':
                        if sessaoPesc in sessao:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                     Aqui está a sessão solicitada                     §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print(f"§§                    Valor:R${sessao[sessaoPesc][0]}                       ")
                            print("§§                                                                         ")
                            print(f"§§          Data:{sessao[sessaoPesc][1]}     Hora:{sessao[sessaoPesc][2]} ")
                            print("§§                                                                         ")
                            tamanho = len(sessao[sessaoPesc][3])
                            for i in range(tamanho):
                                print(f"§§          {i+1}° apresentação: {apresentacoes[sessao[sessaoPesc][3][i]][0]}")
                                print("§§                                                                     ")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                         Sessão não cadastrada.                        §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        print("§§                    Opção inválida, tente novamente                    §§")
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        esc = input("Precione <ENTER> para continuar: ")
            elif sess == '4':
                delet = '10'
                while delet != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print("§§                           Exclusão de sessão.                         §§")
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print("§§                          Digite o id da sessão                        §§")
                    print("§§                                                                       §§")
                    print("§§                           0 - Voltar                                  §§")
                    print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                    print()
                    delet = input("Escolha uma opção: ")
                    print()
                    if delet != '0':
                        if delet in sessao:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                    Quer mesmo excluir essa sessão?                    §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                            1 - Sim                                    §§")
                            print("§§                                                                       §§")
                            print("§§                            2 - Não                                    §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print()
                            mesmo = input("Escolha uma opção: ")
                            if mesmo == '1':
                                del sessao[delet]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§                          Exclusão concluida                           §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif mesmo == '2':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§                          Exclusão cancelada                           §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precione <ENTER> para continuar: ")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                print("§§                    Opção inválida, tente novamente                    §§")
                                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                                esc = input("Precione <ENTER> para continuar: ")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            print("§§                         Sessão não cadastrada.                        §§")
                            print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif delet == '0':
                        continue
                    else: 
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        print("§§                    Opção inválida, tente novamente                    §§")
                        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                        esc = input("Precione <ENTER> para continuar: ")
            elif sess == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                print("§§                Aqui estão todas as sessões cadastradas!               §§")
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                for sessoes in sessao:
                    print(f"§§                     Valor:R${sessao[sessoes][0]}                     ")
                    print(f"§§          Data:{sessao[sessoes][1]}     Hora:{sessao[sessoes][2]}   ")
                    tamanho = len(sessao[sessoes][3])
                    for i in range(tamanho):
                        print(f"§§          {i+1}° apresentação: {apresentacoes[sessao[sessoes][3][i]][0]}")
                    print("§§                                                                     ")
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                esc = input("Precione <ENTER> para continuar: ")
            else:
                print()
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                print("§§                    Opção inválida, tente novamente                    §§")
                print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
                esc = input("Precione <ENTER> para continuar: ")         
    elif inicio == '4':
        ticket = ''
        while ticket != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("$$                          O que deseja fazer?                          $$")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("$$                                                                       $$")
            print("$$                       1 - Vendas de ingressos                         $$")
            print("$$                                                                       $$")
            print("$$                       2 - Atualizar vendas                            $$")
            print("$$                                                                       $$")
            print("$$                       3 - Pesquisar vendas                            $$")
            print("$$                                                                       $$")
            print("$$                       4 - Mostrar todas                               $$")
            print("$$                                                                       $$")
            print("$$                       0 - Voltar                                      $$")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print()
            ticket = input("Escolha uma opção: ")
            if ticket == '0':
                continue
            elif ticket == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                          Adicionar venda                              $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print()
                idTicket = input("Digite o id do novo ingresso: ")
                if idTicket in ingressos:
                    subs = False
                    while subs == False:
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$             Esse id já está cadastrado em outro ingresso.             $$")
                        print("$$                       Deseja subscrever?                              $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                           1 - Sim                                     $$")
                        print("$$                                                                       $$")
                        print("$$                           2 - Não                                     $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print()
                        subTicket = input("Escolha uma opção: ")
                        if subTicket == '1':
                            subs = True
                        elif subTicket == '2':
                            idTicket = input("Digite o id do novo ingresso: ")
                            if idTicket in ingressos:
                                continue
                            else:
                                subs = True
                        else:
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                   Opção inválida, tente novamente.                    $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                print()
                idCliente = input("Digite o id do cliente: ")
                print()
                achou = False
                while achou == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    idSessao = input("Digite o id da sessão: ")
                    if idSessao in sessao:
                        achou = True
                    else:
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                Sessão não cadastrada, tente novamente.                $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        esc = input("Digite <ENTER> para continuar: ")
                print()
                meiaInt = "10"
                while meiaInt != '1' or meiaInt != '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    meiaInt = input("Digite se foi meia ou inteira ((1) inteira (2) meia): ")
                    if meiaInt == "1":
                        meiaInt = '1'
                    elif meiaInt == "2":
                        meiaInt = '0'
                    else:
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                   Opção inválida, tente novamente.                    $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        esc = input("Precione <ENTER> para continuar: ")
                ClientStats = "10"
                while ClientStats != '1' or ClientStats != '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ClientStats = input("Digite o Status do Cliente ((1) ativo (2) desativo): ")
                    if ClientStats == "1":
                        ClientStats = '1'
                    elif ClientStats == "2":
                        ClientStats = '0'
                    else:
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                   Opção inválida, tente novamente.                    $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        esc = input("Precione <ENTER> para continuar: ")
                ingressos[idTicket] = [idCliente, idSessao, meiaInt, ClientStats]
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                    Ingresso adicionado com sucesso!                   $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                esc = input("Precione <ENTER> para continuar: ")
                print()
            elif ticket == '2':
                upTicket = '10'
                while upTicket != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                         Atualização de vendas                         $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                          Digite o id da venda                         $$")
                    print("$$                                                                       $$")
                    print("$$                            0 - Voltar                                 $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print()
                    upTicket = input("Escolha uma opção: ")
                    if upTicket == '0':
                        continue
                    elif upTicket != '0':
                        if upTicket in ingressos:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                 O que você quer atualizar dessa venda                 $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                        1 - Id da sessão                               $$")
                            print("$$                                                                       $$")
                            print("$$                        2 - Meia ou inteira                            $$")
                            print("$$                                                                       $$")
                            print("$$                        3 - Status do cliente                          $$")
                            print("$$                                                                       $$")
                            print("$$                        0 - Voltar                                     $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print()
                            update = input("Escolha uma opção: ")
                            if update == '0':
                                continue
                            elif update == '1':
                                achou = False
                                while achou == False:
                                    idSess = input("Digite o id da sessão desse ingresso: ")
                                    if idSess in sessao:
                                        ingressos[upTicket][1] = idSess
                                        achou = True
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$               Id da sessão foi atualizado com sucesso!                $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        esc = input("Precione <ENTER> para continuar: ")
                                    else:
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$                Sessão não cadastrada, tente novamente!                $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        esc = input("Precione <ENTER> para continuar: ")
                            elif update == '2':
                                mesmo = '10'
                                while mesmo != '1' or mesmo != '2':
                                    if ingressos[upTicket][2] == '1':
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$               Quer mudar o valor de inteira parta meia?               $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$                          1 - Sim                                      $$")
                                        print("$$                                                                       $$")
                                        print("$$                          2 - Não                                      $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print()
                                        mesmo = input("Escolha uma opção: ")
                                        if mesmo == '1':
                                            ingressos[upTicket][2] = '0'
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$                      Valor alterado com sucesso!                      $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        elif mesmo == '2':
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$               Alteração de valor cancelada com sucesso!               $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        else:
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$                   Opção inválida, tente novamente.                    $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                    else:
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$               Quer mudar o valor de meia parta inteira?               $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$                          1 - Sim                                      $$")
                                        print("$$                                                                       $$")
                                        print("$$                          2 - Não                                      $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        mesmo = input("Escolha uma opção: ")
                                        if mesmo == '1':
                                            ingressos[upTicket][2] = '1'
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$                      Valor alterado com sucesso!                      $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        elif mesmo == '2':
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$               Alteração de valor cancelada com sucesso!               $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        else:
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$                   Opção inválida, tente novamente.                    $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                            elif update == '3':
                                mesmo = '10'
                                while mesmo != '1' or mesmo != '2':
                                    if ingressos[upTicket][3] == '1':
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$            Quer mudar o status do cliente para desativado?            $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print("$$                            1 - Sim                                    $$")
                                        print("$$                                                                       $$")
                                        print("$$                            2 - Não                                    $$")
                                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        print()
                                        mesmo = input("Escolha uma opção: ")
                                        if mesmo == '1':
                                            ingressos[upTicket][3] = '0'
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$              Status do cliente foi alterado com sucesso!              $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        elif mesmo == '2':
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$       Alteração do status do cliente foi cancelada com sucesso!       $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            esc = input("Precione <ENTER> para continuar: ")
                                        else:
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$                   Opção inválida, tente novamente.                    $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                        esc = input("Precione <ENTER> para continuar: ")
                                    else:
                                        upClient = False
                                        while upClient == False:
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$             Quer mudar o status do cliente para ativado?              $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print("$$                            1 - Sim                                    $$")
                                            print("$$                                                                       $$")
                                            print("$$                            2 - Não                                    $$")
                                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                            print()
                                            mesmo = input("Escolha uma opção: ")
                                            if mesmo == '1':
                                                ingressos[upTicket][3] = '1'
                                                upClient = True
                                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                                print("$$              Status do cliente foi alterado com sucesso!              $$")
                                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                                esc = input("Precione <ENTER> para continuar: ")
                                            elif mesmo == '2':
                                                upClient = True
                                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                                print("$$       Alteração do status do cliente foi cancelada com sucesso!       $$")
                                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                                esc = input("Precione <ENTER> para continuar: ")
                                            else:
                                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                                print("$$                   Opção inválida, tente novamente.                    $$")
                                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                                esc = input("Precione <ENTER> para continuar: ")
                            else:
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print("$$                   Opção inválida, tente novamente.                    $$")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                esc = input("Precione <ENTER> para continuar: ")
            elif ticket == '3':
                ticketPesc = '10'
                while ticketPesc != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                      Módulo de pesquisa de venda                      $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                         Digite o id da venda                          $$")
                    print("$$                                                                       $$")
                    print("$$                           0 - Voltar                                  $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print()
                    ticketPesc = input("Escolha uma opção: ")
                    if ticketPesc == '0':
                        continue
                    elif ticketPesc != '0':
                        if ticketPesc in ingressos:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                   Aqui está a venda solicitada                        $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print(f"$$                    Id do cliente: {ingressos[ticketPesc][0]}           ")
                            print("$$                                                                         ")
                            print(f"$$                    Id da sessão: {ingressos[ticketPesc][1]}            ")
                            print("$$                                                                         ")
                            if ingressos[ticketPesc][2] == '1':
                                print(f"$$                    Inteira                                         ")
                                print("$$                                                                     ")
                            else:
                                print(f"$$                    Meia                                            ")
                                print("$$                                                                     ")
                            if ingressos[ticketPesc][3] == '1':
                                print(f"$$                    Cliente ativado                                 ")
                            else:
                                print(f"$$                    Cliente desativado                              ")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                Venda não cadastrada, tente novamente.                 $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        esc = input("Precione <ENTER> para continuar: ")
            elif ticket == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                 Aqui estão todas as vendas cadastradas                $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                for ingresso in ingressos:
                    print(f"$$                    Id do cliente: {ingressos[ingresso][0]}     ")
                    print(f"$$                    Id da sessão: {ingressos[ingresso][1]}      ")
                    if ingressos[ingresso][2] == '1':
                        print("$$                    Inteira                                  ")
                    else:
                        print("$$                    Meia                                     ")
                    if ingressos[ingresso][3] == '1':
                        print("$$                    Cliente ativo                            ")
                    else:
                        print("$$                    Cliente inativo                          ")
                    print("$$                                                                 ")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print()
                esc = input("Precione <ENTER> para continuar: ")
    elif inicio == '5':
        rela ='10'
        while rela != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!                              Relatórios                               !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!            1 - Lista de artistas por apresentação                     !!")
            print("!!                                                                       !!")
            print("!!            2 - Lista de apresentação por sessão                       !!")
            print("!!                                                                       !!")
            print("!!            3 - Lista de sessão por valor                              !!")
            print("!!                                                                       !!")
            print("!!            4 - Lista de artistas por sessão                           !!")
            print("!!                                                                       !!")
            print("!!            0 - Voltar                                                 !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print()
            rela = input("Escolha uma opção: ")
            if rela == '0':
                continue
            elif rela == '1':
                idApre = '10'
                while idApre != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!            Módulo de pesquisa de artistas por apresentação            !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!                      Digite o id da apresentação                      !!")
                    print("!!                                                                       !!")
                    print("!!                           0 - Voltar                                  !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print()
                    idApre = input("Escolha uma opção: ")
                    if idApre == '0':
                        continue
                    elif idApre != '0':
                        if idApre in apresentacoes:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!                Aqui estão os artistas dessa apresentação              !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            tamanho = len(apresentacoes[idApre][2])
                            for i in range(tamanho):
                                print(f"!!                   {artistas[apresentacoes[idApre][2][i]][0]}     ")
                                print("!!                                                                     ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!                Sessão não cadastrada, tente novamente                 !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("!!                    Opção inválida, tente novamente                    !!") 
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        esc = input("Precione <ENTER> para continuar: ")       
            elif rela == '2':
                idSess = '10'
                while idSess != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!            Módulo de pesquisa de apresentações por sessão             !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!                       Digite o id da sessão                           !!")
                    print("!!                                                                       !!")
                    print("!!                           0 - Voltar                                  !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print()
                    idSess = input("Escolha uma opção: ")
                    if idSess == '0':
                        continue
                    elif idSess != '0':
                        if idSess in sessao:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!                Aqui estão as apresentações dessa sessão               !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            tamanho = len(sessao[idSess][3])
                            for i in range(tamanho):
                                print(f"!!                  {apresentacoes[sessao[idSess][3][i]][0]}          ")
                                print("!!                                                                     ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!                Sessão não cadastrada, tente novamente                 !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("!!                    Opção inválida, tente novamente                    !!") 
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        esc = input("Precione <ENTER> para continuar: ")
            elif rela == '3':
                valSess = '10'
                while valSess != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!                Módulo de pesquisa de sessões por valor                !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!                Digite o valor da(s) apresentação(ões)                 !!")
                    print("!!                                                                       !!")
                    print("!!                       0 - Voltar                                      !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print()
                    valSess = input("Escolha uma opção: ")
                    if valSess == '0':
                        continue
                    elif valSess != '0':
                        listSess = []
                        valSess = float(valSess)
                        for i in sessao:
                            if valSess in sessao[i]:
                                listSess.append(sessao[i])
                        if len(listSess) != 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!                 Aqui estão as sessões com esse valor                  !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            tamanho = len(listSess)
                            for j in range(tamanho):
                                print(f"!!          Valor: {listSess[j][0]}          Data: {listSess[j][1]}   ")
                                print(f"!!                    Hora: {listSess[j][2]}                          ")
                                for k in range(len(listSess[j][3])):
                                    print(f"!!     {k+1}° apresentação dessa sessão: {apresentacoes[listSess[j][3][k]][0]}")
                                print("!!                                                                     ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif len(listSess) == 0:    
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!                     Não há sessões com esse valor                     !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
            elif rela == '4':
                idSess = '10'
                while idSess != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!               Módulo de pesquisa de artistas por sessão               !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("!!                         Digite o id da sessão                         !!")
                    print("!!                                                                       !!")
                    print("!!                               0 - Voltar                              !!")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print()
                    idSess = input("Escolha uma opção: ")
                    if idSess == '0':
                        continue
                    elif idSess != '0':
                        if idSess in sessao:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!!               Aqui estão todos os artistas dessa sessão               !!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            tamanho1 = len(sessao[idSess][3])
                            for i in range(tamanho1):
                                print(f"!!                          {i+1}° Sessão:                            ")
                                tamanho2 = len(apresentacoes[sessao[idSess][3][i]][2])
                                for j in range(tamanho2):
                                    print(f"!!     {artistas[apresentacoes[sessao[idSess][3][i]][2][j]][0]}   ")
                                    print("!!                                                                 ")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            esc = input("Precione <ENTER> para continuar: ")
    elif inicio == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("///////////////////////////////////////////////////////////////////////////")
        print("//                   Módulo de informações do sistema                    //")
        print("///////////////////////////////////////////////////////////////////////////")
        print("//                                                                       //")
        print("//                   Projeto para a gestão de um circo                   //")
        print("//       Desenvolvido usando a linguagem de programação Python 3.14      //")
        print("//            Desenvolvido por João Manoel Oliveira da Silva             //")
        print("//                    Orientado por Flavius Gorgônio                     //")
        print("//                  O projeto teve início em 27/05/2026                  //")
        print("//                         Concluido: em breve...                        //")
        print("//                                                                       //")
        print("///////////////////////////////////////////////////////////////////////////")
        print()
        info = input("Precione <ENTER> para continuar: ")
    elif inicio == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XX                     Programa encerrado, até mais!                     XX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("???????????????????????????????????????????????????????????????????????????")
        print("??                            Opção inválida.                            ??")
        print("???????????????????????????????????????????????????????????????????????????")
        print("??                                                                       ??")
        print("??                                                                       ??")
        print("??                      Retorne ao menu anterior e                       ??")
        print("??                          tente outra opção                            ??")
        print("??                                                                       ??")
        print("??                                                                       ??")
        print("???????????????????????????????????????????????????????????????????????????")
        print()
        erro = input("Precione <ENTER> para continuar: ")

#Gravação dos arquivos após o encerramento do programa.

arqArt = open('artistas.txt', 'wt', encoding='utf-8')
for idArt, dados in artistas.items():
        arqArt.write(f"{idArt},{dados[0]},{dados[1]}")
        for x in dados[2]:
            arqArt.write(f",{x}")
        arqArt.write("\n")
arqArt.close()

arqApre = open('apresentações.txt', 'wt', encoding='utf-8')
for idApre, dados in apresentacoes.items():  
    arqApre.write(f"{idApre},{dados[0]},{dados[1]}")
    for x in dados[2]:
        arqApre.write(f",{x}")
    arqApre.write("\n")
arqApre.close()

arqSessao = open('sessões.txt', 'wt', encoding='utf-8')
for idSessao, dados in sessao.items():
    arqSessao.write(f"{idSessao},{dados[0]},{dados[1]},{dados[2]}")
    for x in dados[3]:
        arqSessao.write(f",{x}")
    arqSessao.write("\n")
arqSessao.close()

arqTicket = open('ingressos.txt', 'wt', encoding='utf-8')
for idTicket, dados in ingressos.items():
    arqTicket.write(f"{idTicket},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
arqTicket.close()
print("Fim do programa.")