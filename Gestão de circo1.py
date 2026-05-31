# Organização da lista de artistas: [Código de identificação (ID), "Nome", "Telefone", "Especialidade 1", "Especialidade 2"]
artistas = [[101, "Looey", "1111-8888", "Truques com balões", "Truques de mágica"], [102, "Yatta", "2222-9999", "Acrobata", "Equílibrista"],
             [103, "Blot", "3333-0000", "Mímico", "Ventriloquita"], [104, "Eclipsa", "4444-7777", "A menina lobo", "Contorcionista"],
               [105, "Shrimpo", "5555-6666", "O menino camarão", "Acrobata"]]
#Organização dos espetáculos: [Código de identificação (ID), Nome, Artistas participantes]
espetaculos = [[201, ]]




inicio = 13
while inicio != 0:
    print()
    print("___________________________________________________________________________")
    print("||                                                                       ||")
    print("|| Bem-vindo ao programa para a gestão do seu circo, totalmente digital. ||")
    print("||                                                                       ||")
    print("||_______________________________________________________________________||")
    print("||                            O que quer ver?                            ||")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~                              1 - Artistas                             ~~")
    print("[[                                                                       ]]")
    print("[[                              2 - Espetáculos                          ]]")
    print("$$                                                                       $$")
    print("$$                              3 - Bilheteria                           $$")
    print("!!                                                                       !!")
    print("!!                              4 - Relatório                            !!")
    print("//                                                                       //")
    print("//                              5 - Sobre o sistema                      //")
    print("XX                                                                       XX")
    print("XX                              0 - Sair                                 XX")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    inicio = int(input("Escolha uma opção: "))
    print()
    if inicio == 1:
        art = 10
        while art != 0:
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
            art = int(input("Escolha uma opção "))
            print()
            if art == 0:
                continue
            elif art == 1:
                idArt = len(artistas) + 1
                newArt = [100 + idArt]
                nome = input("Digite o nome do novo artista: ")
                newArt.append(nome)
                fone = input("Digite o telefone desse artista: ")
                newArt.append(fone)
                exp = input("Digite a 1° especialidade do artista: ")
                newArt.append(exp)
                exp2 = input("Digite aqui a segunda especialidade do artista (Caso não tenha, digite '0'): ")
                if exp2 != '0':
                    newArt.append(exp2)
                artistas.append(newArt)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                       Artista adicionado com sucesso!                 ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                esc = input("Precione <ENTER> para continuar: ")
                print()
            elif art == 2:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                   Qual contato você quer atualizar?                   ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for i in range (len(artistas)):
                    print(f"~~                        {i+1} - {artistas[i][1]}                                    ~~")
                    print("~~                                                                       ~~")
                print("~~                        0 - Voltar                                     ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                upArt = int(input("Escolha uma opção: "))
                if upArt == 0:
                    continue
                if len(artistas[upArt - 1]) == 5:
                    update = 10
                    while update != 0:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(f"~~     O que deseja atualizar de {artistas[upArt-1]}     ~~")
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
                        update = int(input("Escolha uma opção: "))
                        print()
                        if update == 1:
                            artistas[upArt-1][1] = input("Digite aqui o novo nome: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Nome do artista foi atualizado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 2:
                            artistas[upArt-1][2] = input("Digite o novo número: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~             Número de telefone do artista foi atualizado!             ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 3:
                            artistas[upArt-1][3] = input("Digite aqui a nova 1° especialidade: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                1° especialidade do artista atualizada!                ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 4:
                            artistas[upArt-1][4] = input("Digite aqui a nova 2° especialidade: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                2° especialidade do artista atualizada!                ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 0:
                            continue
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                   Opção inválida, tente novamente.                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                else:
                    update = 10
                    while update != 0:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(f"~~     O que deseja atualizar de {artistas[upArt-1]}     ~~")
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
                        update = int(input("Escolha uma opção: "))
                        if update == 1:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Nome do artista foi atualizado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 2:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~             Número de telefone do artista foi atualizado!             ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 3:
                            artistas[upArt-1][3] = input("Digite aqui a nova especialidade: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                1° especialidade do artista atualizada!                ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 0:
                            continue
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                   Opção inválida, tente novamente.                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
            elif art == 3:
                pesc = 10
                while pesc != 0:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                    Como deseja pesquisar o artista?                   ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                         1 - Por ID                                    ~~")
                    print("~~                                                                       ~~")
                    print("~~                         2 - Por Nome                                  ~~")
                    print("~~                                                                       ~~")
                    print("~~                         3 - Por Especialidade                         ~~")
                    print("~~                                                                       ~~")
                    print("~~                         0 - Voltar                                    ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    pesc = int(input("Escolha uma opção: "))
                    if pesc == 1:
                        print()
                        idPesc = int(input("Digite o id do artista, no padrão (1xx): "))
                        achou = False
                        posi = 0
                        totalArt = len(artistas)
                        while posi < totalArt and (not achou):
                            if artistas[posi][0] == idPesc:
                                achou = True
                            else:
                                posi += 1
                        if achou:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Aqui está o contato solicitado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            for i in range (len(artistas[posi])):
                                print(f"~~                            {artistas[posi][i]}                                 ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                        Artista não cadastrado.                        ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                    elif pesc == 2:
                        print()
                        nomePesc = input("Digite o nome do artista: ")
                        achou = False
                        posi = 0
                        totalArt = len(artistas)
                        while posi < totalArt and (not achou):
                            if artistas[posi][1] == nomePesc:
                                achou = True
                            else:
                                posi += 1
                        if achou:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Aqui está o contato solicitado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            for i in range (len(artistas[posi])):
                                print(f"~~                            {artistas[posi][i]}                                 ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                        Artista não cadastrado.                        ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                    elif pesc == 3:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~     Lembre-se, mais de um artista podem ter a mesma especialidade     ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print()
                        espPesc = input("Digite a especialidade do artista: ")
                        print()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                    Aqui está o(s) contato solicitado!                 ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        esc = input("Precione <ENTER> para continuar: ")
                    elif pesc == 0:
                        continue
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                   Opção inválida, tente novamente.                    ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        esc = input("Precione <ENTER> para continuar: ")
            elif art == 4:
                delet = 10
                while delet != 0:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                   Qual artista você deseja deletar?                   ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    for i in range (len(artistas)):
                        print(f"~~                        {i+1} - {artistas[i][1]}                                    ~~")
                        print("~~                                                                       ~~")
                    print("~~                        0 - Voltar                                     ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    delet = int(input("Escolha uma opção: "))
                    if delet != 0:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(f"~~                   Quer mesmo excluir o(a) {artistas[delet-1][1]}                ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                            1 - Sim                                    ~~")
                        print("~~                                                                       ~~")
                        print("~~                            2 - Não                                    ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        mesmo = int(input("Escolha uma opção: "))
                        if mesmo == 1:
                            del artistas[delet-1]
                            totalArt = len(artistas)
                            for i in range (totalArt):
                                if artistas[i][0] >= artistas[delet-1][0]:
                                    artistas[i][0] = artistas[i][0] - 1
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                          Exclusão concluida.                          ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif mesmo == 2:
                            continue
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                   Opção inválida, tente novamente.                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif delet == 0:
                        continue
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~                   Opção inválida, tente novamente.                    ~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        esc = input("Precione <ENTER> para continuar: ")
            elif art == 5:
                totalArt = len(artistas)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~               Aqui estão todos os artistas cadastrados                ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for i in range(totalArt):
                    print(f"~~  {artistas[i]}  ~~")
                    print("~~                                                                       ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                esc = input("Precione <ENTER> para continuar: ")

    elif inicio == 2:
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        print("[[                 Este módulo está em desenvolvimento                   ]]")
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        print("[[                                                                       ]]")
        print("[[                                                                       ]]")
        print("[[                      Retorne ao menu anterior e                       ]]")
        print("[[                          tente outra opção                            ]]")
        print("[[                                                                       ]]")
        print("[[                                                                       ]]")
        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        print()
        esp = input("Precione <ENTER> para continuar: ")
    elif inicio == 3:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("$$                 Este módulo está em desenvolvimento                   $$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("$$                                                                       $$")
        print("$$                                                                       $$")
        print("$$                      Retorne ao menu anterior e                       $$")
        print("$$                          tente outra opção                            $$")
        print("$$                                                                       $$")
        print("$$                                                                       $$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print()
        ticket = input("Precione <ENTER> para continuar: ")
    elif inicio == 4:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!                 Este módulo está em desenvolvimento                   !!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!                                                                       !!")
        print("!!                                                                       !!")
        print("!!                      Retorne ao menu anterior e                       !!")
        print("!!                          tente outra opção                            !!")
        print("!!                                                                       !!")
        print("!!                                                                       !!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()
        rela = input("Precione <ENTER> para continuar: ")
    elif inicio == 5:
        print("///////////////////////////////////////////////////////////////////////////")
        print("//                   Módulo de informações do sistema                    //")
        print("///////////////////////////////////////////////////////////////////////////")
        print("//                                                                       //")
        print("//                   Projeto para a gestão de um circo                   //")
        print("//   Desenvolvido usando apenas a linguagem de programação Python 3.14   //")
        print("//            Desenvolvido por João Manoel Oliveira da Silva             //")
        print("//                    Orientado por Flavius Gorgônio                     //")
        print("//                  O projeto teve início em 27/05/2026                  //")
        print("//                         Concluido: em breve...                        //")
        print("//                                                                       //")
        print("///////////////////////////////////////////////////////////////////////////")
        print()
        info = input("Precione <ENTER> para continuar: ")
    elif inicio == 0:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XX                     Programa encerrado, até mais!                     XX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print()
    else:
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
        erro = input("Precione <ENTER> para continuar: ")

print("Fim do programa.")