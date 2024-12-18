from processo import Processo
from geradoraDeProcessos import GeradoraDeProcessos
from cpu import Cpu
from despachante import Despachante
#from tabelaDeProcessos import TabelaDeProcessos

t = 0

auxiliarQueue = []
readyQueue = []
newQueue = []
memory = Memory(32768, 128)
cpus = [Cpu(1), Cpu(2), Cpu(3), Cpu(4)]



while(True):
    

    #Geração do Processo #
    GeradoraDeProcessos.generateProcess(newQueue)

    for processo in newQueue:
    #Verificar possibilidade de Alocação na MemóriaPrincipal processo.Aloca #
        #IF processo.Aloca = True 
            #Ocupar espaços do Processo #
            #Gerar Tabela de Páginas do Processo#

            #readyQueue.append(processo)
            #process.newToReady()
            #newQueue.remove(processo)
        pass

    Despachante.despachar(auxiliarQueue, readyQueue, cpus)


    t += 1
    break