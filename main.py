from cpu import Cpu
from process import Process
from despachante import Despachante
from processTable import ProcessTable
from geradoraDeProcessos import GeradoraDeProcessos
from memory import Memory


t = 0   #Representa a unidade de tempo
pageSize = 128
memorySize = 32768

auxiliarQueue = []   #Fila auxiliar com os processs prontos
readyQueue = []   #Fila com os processs prontos
newQueue = []   #Fila com os processs novos
ioProcesses = []   #Vetor com os processs na fase de IO
memory = Memory(memorySize, pageSize)  #Representação da memória principal
cpus = [Cpu(1), Cpu(2), Cpu(3), Cpu(4)]   #Vetor com as 4 CPUs

while(True):
    #   Para todas as CPUs, executamos os processs alocados nelas: cpus[i].run #
    #   Executamos todos os processs na fase de IO: ioProcesses[i].processRun  #         
    for i in cpus:
        i.run(readyQueue)
    for i in ioProcesses:
        i.processRun(auxiliarQueue, ioProcesses)

    #   A thread Geradora de processs gera de zero a três processs aleatórios #
    #   e os aloca na fila de processs novos                                   #
    GeradoraDeProcessos.generateProcess(newQueue) 

    #   Para cada process na fila de processs novos                           #
    for process in newQueue:
    #   Verifica  possibilidade de alocação na memória: process.aloca(memory)  #
        if memory.verifySpace(process):
            processTable = memory.processAlocation(process) # 
            readyQueue.append(process)  # Insere o processo na fila de prontos #                                   
            process.newToReady()    # Processo muda de estado #                                        
            newQueue.remove(process)                                       

    #   A thread despachante escalona os processs na fila de pronto p/ as CPUs #
    Despachante.despachar(auxiliarQueue, readyQueue, cpus)

    #Atualizamos a unidade de tempo                                             #
    t += 1
    
    #Imprimimos as informações atuais                                           #
    
    break