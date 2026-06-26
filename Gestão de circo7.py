#Bibliotecas utilizadas:
import os
# Organização da lista de artistas: [nome, telefone e especialidades]
from Def import ReadArt
artistas = ReadArt.readArt()
#Organização dos apresentaçãos: [nome, data, Descrição e id dos artistas participantes]
from Def import ReadApre
apresentacoes = ReadApre.readApre()
#Organização dos sessãos: [Valor, data, hora, lista com id das apresentações]
from Def import ReadSess
sessao = ReadSess.readSess()
#Organização dos ingressos: [idcliente, idsessão, meia/inteira, Cliente ativo/desativo]
from Def import ReadTicket
ingressos = ReadTicket.readTicket()
#Início dos CRUDS
from Def import Main
Main.main(artistas, apresentacoes, sessao, ingressos)
#Gravação dos arquivos após o encerramento do programa.
from Def import WriteArt
WriteArt.writeArt(artistas)
from Def import WriteApre
WriteApre.writeApre(apresentacoes)
from Def import WriteSess
WriteSess.writeSess(sessao)
from Def import WriteTicket
WriteTicket.writeTicket(ingressos)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("XX                     Programa encerrado, até mais!                     XX")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print()
print("Fim do programa.")