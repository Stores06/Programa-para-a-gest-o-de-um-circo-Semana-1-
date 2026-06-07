# Organização da lista de artistas: [nome, telefone, especialidade 1 e especialidade 2]
artistas = {101: ["Looey", "1111-8888", "Truques com balões", "Truques de mágica"],
            102: ["Yatta", "2222-9999", "Acrobata", "Equílibrista"],
            103: ["Blot", "3333-0000", "Mímico", "Ventriloquita"],
            104: ["Eclipsa", "4444-7777", "A menina lobo", "Contorcionista"],
            105: ["Shrimpo", "5555-6666", "O menino camarão", "Acrobata"]}
#Organização dos espetáculos: [nome, data e hora, Descrição e artistas participantes]
espetaculos = {201: ["Show de abertura", "11/07 ás 18:00h",
                    "Os artistas se apresentam e mostram um pouco do que são capazes de fazer", "Looey, Yatta, Blot, Eclipsa e Shrimpo"],
               202: ["Shrimpo e Eclipsa", "11/07 ás 18:45h", 
                     "Gato e rato entre a loba e o camarão", "Shrimpo e Eclipsa"],
               203: ["Balões do Looey", "11/07 ás 19:30h", 
                     "Looey mostra suas habilidades com balões para Blot e Blot Jr.", "Looey e Blot"],
               204: ["Desafios da Yatta", "12/17 ás 18:00h", 
                     "Yatta fará desafios de equilíbrio e de acrobacias perante ao público", "Yatta"],
               205: ["Blot Jr. responde", "12/07 ás 18:45h", 
                     "Yatta e Looey fazem perguntas ao Blot Jr.", "Blot, Yatta e Looey"]}
#Organização dos ingressos: [id do espetáculo e valor]
ingressos = {301: [201, "R$15,00"],
             302: [202, "R$15,00"],
             303: [203, "R$15,00"],
             304: [204, "R$12,00"],
             305: [205, "R$12,00"]}





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
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                           Adicionar artista                           ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                idArt = int(input("Digite aqui o id do novo artista (de preferência, no formato 1xx): "))
                print()
                nome = input("Digite o nome do novo artista: ")
                print()
                fone = input("Digite o telefone desse artista: ")
                print()
                esp = input("Digite a 1° especialidade do artista: ")
                print()
                esp2 = input("Digite aqui a segunda especialidade do artista (Caso não tenha, digite '0'): ")
                if esp2 != '0':
                    artistas[idArt] = [nome, fone, esp, esp2]
                else:
                    artistas[idArt] = [nome, fone, esp]
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                       Artista adicionado com sucesso!                 ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                esc = input("Precione <ENTER> para continuar: ")
                print()
            elif art == 2:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                   Qual contato você quer atualizar?                   ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~                        Digite o id do artista                         ~~")
                print("~~                                                                       ~~")
                print("~~                           0 - Voltar                                  ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                upArt = int(input("Escolha uma opção: "))
                print()
                if upArt == 0:
                    continue
                if len(artistas[upArt]) == 4:
                    update = 10
                    while update != 0:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(f"~~            O que deseja atualizar de {artistas[upArt][0]}                ~~")
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
                            artistas[upArt][0] = input("Digite aqui o novo nome: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Nome do artista foi atualizado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 2:
                            artistas[upArt][1] = input("Digite o novo número: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~             Número de telefone do artista foi atualizado!             ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 3:
                            artistas[upArt][2] = input("Digite aqui a nova 1° especialidade: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                1° especialidade do artista atualizada!                ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 4:
                            artistas[upArt][3] = input("Digite aqui a nova 2° especialidade: ")
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
                        print(f"~~               O que deseja atualizar de {artistas[upArt][0]}?                  ~~")
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
                            artistas[upArt][0] = input("Digite aqui o novo nome: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Nome do artista foi atualizado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 2:
                            artistas[upArt][1] = input("Digite o novo número: ")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~             Número de telefone do artista foi atualizado!             ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif update == 3:
                            artistas[upArt][2] = input("Digite aqui a nova especialidade: ")
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
                idPesc = 10
                while idPesc != 0:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                    Módulo de pesquisa de artista?                     ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~                        Digite o id do artista                         ~~")
                    print("~~                                                                       ~~")
                    print("~~                           0 - Voltar                                  ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    idPesc = int(input("Escolha uma opção: "))
                    if idPesc != 0:
                        print()
                        if idPesc in artistas:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                    Aqui está o contato solicitado!                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            for i in range (len(artistas[idPesc])):
                                print(f"~~                            {artistas[idPesc][i]}                                 ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                        Artista não cadastrado.                        ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print()
                            esc = input("Precione <ENTER> para continuar: ")
                    elif idPesc == 0:
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
                    print("~~                          Exclusão de artista                          ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("~~               Digite o Id do artista que queira escluir               ~~")
                    print("~~                                                                       ~~")
                    print("~~                               0 - Voltar                              ~~")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    delet = int(input("Escolha uma opção: "))
                    if delet != 0:
                        if delet in artistas:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(f"~~                   Quer mesmo excluir o(a) {artistas[delet][0]}                ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                            1 - Sim                                    ~~")
                            print("~~                                                                       ~~")
                            print("~~                            2 - Não                                    ~~")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            mesmo = int(input("Escolha uma opção: "))
                            if mesmo == 1:
                                del artistas[delet]
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("~~                          Exclusão concluida.                          ~~")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif mesmo == 2:
                                continue
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("~~                        Artista não cadastrado                         ~~")
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
                totalArt = len(artistas) + 201
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~               Aqui estão todos os artistas cadastrados                ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                i = 101
                for i in range(totalArt):
                    if i in artistas:
                        print(f"~~  {artistas[i]}     ~~")
                        print("~~                                                                       ~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                esc = input("Precione <ENTER> para continuar: ")

    elif inicio == 2:
        esp = 10
        while esp != 0:
            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("[[                          O que deseja fazer?                          ]]")
            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print("[[                                                                       ]]")
            print("[[                       1 - Adicionar espetáculo                        ]]")
            print("[[                                                                       ]]")
            print("[[                       2 - Atualizar espetáculo                        ]]")
            print("[[                                                                       ]]")
            print("[[                       3 - Pesquisar espetáculo                        ]]")
            print("[[                                                                       ]]")
            print("[[                       4 - Excluir espetáculo                          ]]")
            print("[[                                                                       ]]")
            print("[[                       5 - Mostrar todos                               ]]")
            print("[[                                                                       ]]")
            print("[[                       0 - Voltar                                      ]]")
            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
            print()
            esp = int(input("Escolha uma opção: "))
            if esp == 1:
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[                         Adicionar espetáculo                          ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                idEsp = int(input("Digite aqui o id do novo espetáculo: "))
                print()
                nomeEsp = input("Digite o nome do novo espetáculo: ")
                print()
                dataEsp = input("Digite aqui a data do novo espetáculo: ")
                print()
                descEsp = input("Digite aqui a descrição do novo espetáculo: ")
                print()
                artEsp = input("Digite aqui o(os) artista(s) desse novo espetáculo: ")
                print()
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[                    Novo espetáculo adicionado                         ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print()
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[                                ATENÇÃO                                ]]")
                print("[[                       Isso é apenas uma simulação                     ]]")
                print("[[                essa função ainda está sendo trabalhada.               ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                esc = input("Precine <ENTER> para continuar: ")
            elif esp == 2:
                update = 10
                while update != 0:
                    print()
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                  Qual espetáculo você quer atualizar                  ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                       Digite o id do espetáculo                       ]]")
                    print("[[                                                                       ]]")
                    print("[[                       0 - Voltar                                      ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    update = int(input("Escolha uma opção: "))
                    if update == 0:
                        continue
                    elif update != 0:
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print(f"[[                O que deseja atualizar de {espetaculos[update][0]}?                 ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                           1 - Nome                                    ]]")
                        print("[[                                                                       ]]")
                        print("[[                           2 - Data e hora                             ]]")
                        print("[[                                                                       ]]")
                        print("[[                           3 - Descrição                               ]]")
                        print("[[                                                                       ]]")
                        print("[[                           4 - Artistas                                ]]")
                        print("[[                                                                       ]]")
                        print("[[                           0 - Voltar                                  ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        upEsp = int(input("Escolha uma opção: "))
                        if upEsp == 0:
                            continue
                        elif upEsp == 1:
                            espetaculos[update][0] = input("Digite aqui o novo nome: ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[             Nome do espetáculo foi atualizado com sucesso!            ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif upEsp == 2:
                            espetaculos[update][1] = input("Digite aqui a nova data e hora: ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[      Nova data e hora do espetáculo foi atualizada com sucesso!       ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif upEsp == 3:
                            espetaculos[update][2] = input("Digite aqui a nova descrição: ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[        Nova descrição do espetáculo foi atualizada com sucesso!       ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                        elif upEsp == 4:
                            espetaculos[update][3] = input("Digite aqui os novos artistas participantes: ")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[      Novos artistas do espetáculo foram atualizados com sucesso!      ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                   Opção inválida, tente novamente.                    ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
            elif esp == 3:
                espPesc = 10
                while espPesc != 0:
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                   Módulo de pesquisa de espetáculo                    ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                       Digite o id do espetáculo                       ]]")
                    print("[[                                                                       ]]")
                    print("[[                             0 - Voltar                                ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    espPesc = int(input("Escolha uma opção: "))
                    if espPesc == 0:
                        continue
                    elif espPesc != 0:
                        print()
                        if espPesc in espetaculos:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                   Aqui está o espetáculo solicitado!                  ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            for i in range(len(espetaculos[espPesc])):
                                print(f"[[                      {espetaculos[espPesc][i]}               ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                       Espetáculo não cadastrado.                      ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                   Opção inválida, tente novamente.                    ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        esc = input("Precione <ENTER> para continuar: ")
            elif esp == 4:
                delet = 10
                while delet != 0:
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                        Exclusão de espetáculos                        ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    print("[[                       Digite o id do espetáculo                       ]]")
                    print("[[                                                                       ]]")
                    print("[[                             0 - Voltar                                ]]")
                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                    delet = int(input("Escolha uma opção: "))
                    if delet != 0:
                        print()
                        if delet in espetaculos:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print(f"[[       Quer mesmo excluir o {espetaculos[delet][0]}                 ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                            1 - Sim                                    ]]")
                            print("[[                                                                       ]]")
                            print("[[                            2 - Não                                    ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            mesmo = int(input("Escolha uma opção: "))
                            if mesmo == 1:
                                del espetaculos[delet]
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[                        Exclusão concluida.                            ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif mesmo == 2:
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                print("[[                       Exclusão cancelada                              ]]")
                                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                                esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            print("[[                       Espetáculo não cadastrado.                      ]]")
                            print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif delet == 0:
                        continue
                    else:
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        print("[[                   Opção inválida, tente novamente.                    ]]")
                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                        esc = input("Precione <ENTER> para continuar: ")
            elif esp == 5:
                totalEsp = len(espetaculos) + 301
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                print("[[              Aqui estão todos os espetáculos cadastrados              ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                i = 201
                for i in range(totalEsp):
                    if i in espetaculos:    
                        print(f"[[   {espetaculos[i]}    ]]")
                        print("[[                                                                       ]]")
                print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
                esc = input("Precione <ENTER> para continuar: ")

                
    elif inicio == 3:
        ticket = 10
        while ticket != 0:
            print()
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("$$                          O que deseja fazer?                          $$")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("$$                                                                       $$")
            print("$$                       1 - Adicionar ingresso                          $$")
            print("$$                                                                       $$")
            print("$$                       2 - Atualizar ingresso                          $$")
            print("$$                                                                       $$")
            print("$$                       3 - Pesquisar ingresso                          $$")
            print("$$                                                                       $$")
            print("$$                       4 - Excluir ingresso                            $$")
            print("$$                                                                       $$")
            print("$$                       5 - Mostrar todos                               $$")
            print("$$                                                                       $$")
            print("$$                       0 - Voltar                                      $$")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
            print()
            ticket = int(input("Escolha uma opção: "))
            if ticket == 0:
                continue
            elif ticket == 1:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                           Adicinar ingresso                           $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                idTicket = int(input("Digite aqui o id desse novo ingresso: "))
                print()
                espTiket = int(input("Digite o id do espetáculo desse ingresso: "))
                print()
                valTicket = input("Digite o valor desse ingresso: ")
                print()
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                    Ingresso adicionado com sucesso!                   $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print()
                print()
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                                ATENÇÃO                                $$")
                print("$$                      Isso é apenas uma simulação                      $$")
                print("$$               essa função ainda está sendo trabalhada.                $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                esc = input("Precione <ENTER> para continuar: ")
            elif ticket == 2:
                update = 10
                while update != 0:
                    print()
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                   Qual ingresso você quer atualizar?                  $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                        Digite o id do ingresso                        $$")
                    print("$$                                                                       $$")
                    print("$$                        0 - Voltar                                     $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    update = int(input("Escolha uma opção: "))
                    print()
                    if update == 0:
                        continue
                    elif update != 0:
                        if update in ingressos:
                            print()
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print(f"$$                O que deseja atualizar de {ingressos[update][0]}?             $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                         1 - Id do espetáculo                          $$")
                            print("$$                                                                       $$")
                            print("$$                         2 - Valor                                     $$")
                            print("$$                                                                       $$")
                            print("$$                         0 - Voltar                                    $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            upTicket = int(input("Escolha uma opção: "))
                            if upTicket == 0:
                                continue
                            elif upTicket == 1:
                                ingressos[update][0] = int(input("Digite o id do novo espetáculo desse ingresso (no formato 2XX): "))
                                if ingressos[update][0] != str and ingressos[update][0] in espetaculos:
                                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                    print("$$           Novo id de espetáculo foi atualizado com sucesso!           $$")
                                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                    esc = input("Precione <ENTER> para continuar: ")
                                else:
                                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                    print("$$                    Opção inválida, tente novamente                    $$")
                                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                    esc = input("Precione <ENTER> para continuar: ")
                            elif upTicket == 2:
                                ingressos[update][1] = input("Digite o novo valor desse ingresso: ")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print("$$          Novo valor desse ingresso foi atualizado com sucesso!        $$")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                esc = input("Precione <ENTER> para continuar: ")
                            else:
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print("$$                    Opção inválida, tente novamente                    $$")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                    Opção inválida, tente novamente                    $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            esc = input("Precione <ENTER> para continuar: ")
            elif ticket == 3:
                ticketPesc = 10
                while ticketPesc != 0:
                    print()
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                     Módulo de pesquisa de ingresso                    $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                        Digite o id do ingresso                        $$")
                    print("$$                                                                       $$")
                    print("$$                           0 - Voltar                                  $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    ticketPesc = int(input("Escolha uma opção: "))
                    print()
                    if ticketPesc == 0:
                        continue
                    elif ticketPesc != 0:
                        if ticketPesc in ingressos:
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                    Aqui está o ingresso solicitado                    $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            for i in range (len(ingressos[ticketPesc])):
                                print(f"$$                   {ingressos[ticketPesc][i]}                              $$")
                                print("$$                                                                       $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                        Ingresso não cadastrado.                       $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            esc = input("Precione <ENTER> para continuar: ")
                    else:
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                    Opção inválida, tente novamente                    $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        esc = input("Precione <ENTER> para continuar: ")
            elif ticket == 4:
                delet = 10
                while delet != 0:
                    print()
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                          Exclusão de ingresso                         $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("$$                         Digite o id do ingresso                       $$")
                    print("$$                                                                       $$")
                    print("$$                           0 - Voltar                                  $$")
                    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    delet = int(input("Escolha uma opção: "))
                    print()
                    if delet != 0:
                        print()
                        if delet in ingressos:
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print(f"$$             Quer mesmo excluir o ingresso de {ingressos[delet][0]}?    $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                            1 - Sim                                    $$")
                            print("$$                                                                       $$")
                            print("$$                            2 - Não                                    $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            mesmo = int(input("Escolha uma opção: "))
                            print()
                            if mesmo == 1:
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print("$$                          Exclusão concluida                           $$")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print()
                                print()
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print("$$                                ATENÇÃO                                $$")
                                print("$$                      Isso é apenas uma simulação                      $$")
                                print("$$               essa função ainda está sendo trabalhada.                $$")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                esc = input("Precione <ENTER> para continuar: ")
                            elif mesmo == 2:
                                print()
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                print("$$                          Exclusão cancelada                           $$")
                                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                esc = input("Precione <ENTER> para continuar: ")
                        else:
                            print()
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            print("$$                        Ingresso não cadastrado.                       $$")
                            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            esc = input("Precione <ENTER> para continuar: ")
                    elif delet == 0:
                        continue
                    else: 
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        print("$$                    Opção inválida, tente novamente                    $$")
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                        esc = input("Precione <ENTER> para continuar: ")
            elif ticket == 5:
                totalTicket = len(ingressos)+401
                print()
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$               Aqui estão todos os ingressos cadastrados!              $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                i = 301
                for i in range(totalTicket):
                    if i in ingressos:
                        print(f"$$                   {ingressos[i]}                    $$")
                        print("$$                                                                       $$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                esc = input("Precione <ENTER> para continuar: ")                           
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