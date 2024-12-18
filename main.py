from cpu import Cpu
from processo import Processo
from despachante import Despachante
#from tabelaDeProcessos import TabelaDeProcessos
from geradoraDeProcessos import GeradoraDeProcessos

t = 0   #Representa a unidade de tempo

auxiliarQueue = []   #Fila auxiliar com os processos prontos
readyQueue = []   #Fila com os processos prontos
newQueue = []   #Fila com os processos novos
ioProcesses = []   #Vetor com os processos na fase de IO
memory = [0] * 32768   #Representação da memória principal
cpus = [Cpu(1), Cpu(2), Cpu(3), Cpu(4)]   #Vetor com as 4 CPUs

while(True):
    #   Para todas as CPUs, executamos os processos alocados nelas: cpus[i].run #
    #   Executamos todos os processos na fase de IO: ioProcesses[i].processRun  #         
    
    #   A thread Geradora de processos gera de zero a três processos aleatórios #
    #   e os aloca na fila de processos novos                                   #
    GeradoraDeProcessos.generateProcess(newQueue)

    #   Para cada processo na fila de processos novos                           #
    for processo in newQueue:
    #   Verifica  possibilidade de alocação na memória: processo.aloca(memory)  #
        #   IF processo.aloca(memory) == True:                                  #
            #   Alocamos o processo na memória                                  #
            #   Gera a tabela de páginas do processo                            #

            #   readyQueue.append(processo)                                     #
            #   process.newToReady()                                            #
            #   newQueue.remove(processo)                                       #
        pass

    #   A thread despachante escalona os processos na fila de pronto p/ as CPUs #
    Despachante.despachar(auxiliarQueue, readyQueue, cpus)

    #Atualizamos a unidade de tempo                                             #
    t += 1
    
    #Imprimimos as informações atuais                                           #
    
    break