from random import random #Gerar N RANDOM
from processo import Processo #Puxar clsse Processo

#ATIVIDADE Aula N4 (SO)

#Somente um processo por vez pode estar no estado de EXECUTANDO. O SO definiu um Quantum de execução para cada
# processo de 1000 ciclos. Em cada ciclo o processo tem 5% de chances de realizar uma operação de E/S, ficando então
# bloqueado. Uma vez que ele realizar uma operação de E/S, na sua próxima vez,
# ele terá 30% de chances para sair do estado de Bloqueado e ir para o estado de Pronto.
def chance(): #GERAR NUM 0 - 1
    return random() #RETORNANDO GERADOR
processos = [Processo(0, 10000), #N processos
             Processo(1, 5000),
             Processo(2, 7000),
             Processo(3, 3000),
             Processo(4, 3000),
             Processo(5, 8000),
             Processo(6, 2000),
             Processo(7, 5000),
             Processo(8, 4000),
             Processo(9, 10000)] #VAL RETIRADOS DA ATIVIDADE N4
quantum = 1000 #
finalizados = 0

while finalizados < 10: #ENQUANTO FOR MENOR QUE 10
    if finalizados == 10: #SE FOR IGUAL A 10 ENCERRAR
        break

    for processo in processos: #PEGANDO UM ENTRE VÁRIOS PROCESSOS
        if processo.ep == 'PRONTO': #DEFINIÇÃO DE PRONTO
            processo.executando()
            processo.add_ncpu()  #ADICIONANDO N DE VEZES QUE USOU A CPU
            realizou = False

            for i in range(1, quantum + 1): #REMOVENDO PROCESSO
                if processo.tp == processo.te:
                    finalizados += 1
                    processo.finalizado()
                    processo.print() #APÓS O PRINT
                    processos.remove(processo) #REMOVER PROCESSO
                    break

                processo.add__tp() #ADICIONANDO TEMPO DE PROCESSO
                processo.set_cp() #PEGANDO O CONTADOR

                print(f'PID: {processo.pid}') #IDENTIFICADOR DE PROCESSO
                print(f'CP: {processo.cp}') #CONTADOR

                #DEFININDO %   (5%)
                if chance() <= 0.05: #CASO SEJA MENOR IGUAL 0.05 ENTRAR EM ESTADO DE BLOQUEIO
                    realizou = True
                    processo.add__nes()
                    processo.bloqueado()
                    break

            if not realizou:
                processo.pronto()
                processo.print()

        #DEFININDO %   (30%)
        else: #CASO SEJA 0.3 DEVE ENTRAR EM ESTADO DE PRONTO
            if chance() <= 0.3:
                processo.pronto()
