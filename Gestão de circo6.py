#Bibliotecas utilizadas:
import os
# Organização da lista de artistas: [nome, telefone e especialidades]
from Read import ReadArt
artistas = ReadArt.readArt()
#Organização dos apresentaçãos: [nome, data, Descrição e id dos artistas participantes]
from Read import ReadApre
apresentacoes = ReadApre.readApre()
#Organização dos sessãos: [Valor, data, hora, lista com id das apresentações]
from Read import ReadSess
sessao = ReadSess.readSess()
#Organização dos ingressos: [idcliente, idsessão, meia/inteira, Cliente ativo/desativo]
from Read import ReadTicket
ingressos = ReadTicket.readTicket()
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
                from Add import AddArt
                AddArt.addArt(artistas)
            elif art == "2":
                from Update import UpArt
                UpArt.upArt(artistas)
            elif art == "3":
                from Pesc import PescArt
                PescArt.pescArt(artistas)
            elif art == "4":
                from Delet import DeletArt
                DeletArt.deletArt(artistas)
            elif art == "5":
                from All import AllArt
                AllArt.allArt(artistas)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
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
                from Add import AddApre
                AddApre.addApre(apresentacoes, artistas)
            elif esp == '2':
                from Update import UpApre
                UpApre.upApre(apresentacoes, artistas)
            elif esp == '3':
                from Pesc import PescApre
                PescApre.pescApre(apresentacoes, artistas)
            elif esp == '4':
                from Delet import DeletApre
                DeletApre.deletApre(apresentacoes)
            elif esp == '5':
                from All import AllApre
                AllApre.allApre(apresentacoes)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
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
                from Add import AddSess
                AddSess.addSess(sessao, apresentacoes)
            elif sess == '2':
                from Update import UpSess
                UpSess.upSess(sessao, apresentacoes)
            elif sess == '3':
                from Pesc import PescSess
                PescSess.pescSess(sessao, apresentacoes)
            elif sess == '4':
                from Delet import DeletSess
                DeletSess.deletSess(sessao)
            elif sess == '5':
                from All import AllSess
                AllSess.allSess(sessao, apresentacoes)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
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
                from Add import AddTicket
                AddTicket.addTicket(ingressos, sessao)
            elif ticket == '2':
                from Update import UpTicket
                UpTicket.upTicket(ingressos, sessao)
            elif ticket == '3':
                from Pesc import PescTicket
                PescTicket.pescTicket(ingressos)
            elif ticket == '4':
                from All import AllTicket
                AllTicket.allTicket(ingressos)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$$                   Opção inválida, tente novamente                     $$")
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

#Arrumar isso aqui

from Write import WriteArt
WriteArt.writeArt(artistas)

from Write import WriteApre
WriteApre.writeApre(apresentacoes)

from Write import WriteSess
WriteSess.writeSess(sessao)

from Write import WriteTicket
WriteTicket.writeTicket(ingressos)

print("Fim do programa.")