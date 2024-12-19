from cpu import Cpu
from process import Process
from despachante import Despachante
from processTable import ProcessTable
from geradoraDeProcessos import GeradoraDeProcessos
from memory import Memory

id = 0
t = 0   #Representa a unidade de tempo
pageSize = 128   #Constante do tamanho da página
memorySize = 32768   #Constante do tamanho da memória

auxiliarQueue = []   #Fila auxiliar com os processs prontos
readyQueue = []   #Fila com os processos prontos
newQueue = []   #Fila com os processos novos
ioProcesses = []   #Vetor com os processos na fase de IO
memory = Memory(memorySize, pageSize)  #Representação da memória principal
cpus = [Cpu(1), Cpu(2), Cpu(3), Cpu(4)]   #Vetor com as 4 CPUs

while(True):
    print(f'T = {t}') 
    
    #   Para todas as CPUs, executamos os processs alocados nelas: cpus[i].run #
    #   Executamos todos os processs na fase de IO: ioProcesses[i].processRun  #    
    for i in ioProcesses:
        i.processRun(auxiliarQueue, ioProcesses)    
    for i in cpus:
        i.run(readyQueue, auxiliarQueue, ioProcesses)

    #   A thread Geradora de processs gera de zero a três processs aleatórios #
    #   e os aloca na fila de processs novos                                   #
    if t ==0: 
        id = GeradoraDeProcessos.generateProcess(newQueue, id) 

    #   Para cada process na fila de processs novos                           #
    for process in newQueue[:]:
    #   Verifica  possibilidade de alocação na memória: process.aloca(memory)  #
        if memory.verifySpace(process):
            processTable = memory.processAlocation(process) # FALTA USAR PROCESS TABLE!!!!!!!!!! #
            readyQueue.append(process)  # Insere o processo na fila de prontos #                                   
            process.newToReady()    # Processo muda de estado #                                        
            newQueue.remove(process)     

    #   A thread despachante escalona os processs na fila de pronto p/ as CPUs #
    Despachante.despachar(auxiliarQueue, readyQueue, cpus)

    #Atualizamos a unidade de tempo                                             #
    t += 1
    
    #Imprimimos as informações atuais                                           #
    
    print("\n")
    if t == 30:
        break