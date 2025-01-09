from cpu import Cpu
from process import Process
from despachante import Despachante
from processTable import ProcessTable
from geradoraDeProcessos import GeradoraDeProcessos
from memory import Memory
import threading

id = 0  #Variável que controla o identificador dos processos
t = 0   #Representa a unidade de tempo
pageSize = 128   #Constante do tamanho da página
memorySize = 32768   #Constante do tamanho da memória

auxiliarQueue = []   #Fila auxiliar com os processs prontos
readyQueue = []   #Fila com os processos prontos
newQueue = []   #Fila com os processos novos
ioProcesses = []   #Vetor com os processos na fase de IO
memory = Memory(memorySize, pageSize)  #Representação da memória principal
cpus = [Cpu(1), Cpu(2), Cpu(3), Cpu(4)]   #Vetor com as 4 CPUs

threadGeradoraDeProcessos = threading.Thread(target=GeradoraDeProcessos.generateProcess, args=(newQueue, id)) #Thread que gera processos
threadGeradoraDeProcessos.start() #Inicia a thread

threadDespachante = threading.Thread(target=Despachante.despachar, args=(auxiliarQueue, readyQueue, cpus)) #Thread que despacha processos
threadDespachante.start() #Inicia a thread

while(True):
    print(f'-------------------- T = {t} --------------------\n') 
    
    #   Para todas as CPUs, executamos os processs alocados nelas: cpus[i].run #
    #   Executamos todos os processs na fase de IO: ioProcesses[i].processRun  #    
    for i in ioProcesses:
        i.processRun(auxiliarQueue, ioProcesses, memory)    
    for i in cpus:
        i.run(readyQueue, auxiliarQueue, ioProcesses, memory)

    #   A thread Geradora de processs gera de zero a três processs aleatórios #
    #   e os aloca na fila de processs novos                                   #

    if t<45:
        id = GeradoraDeProcessos.generateProcess(newQueue, id) 

    #   Para cada process na fila de processs novos                           #
    for process in newQueue[:]:
    #   Verifica  possibilidade de alocação na memória: process.aloca(memory)  #
        if memory.verifySpace(process):
            process.table = memory.processAlocation(process)
            readyQueue.append(process)  # Insere o processo na fila de prontos #                                   
            process.newToReady()    # Processo muda de estado #                                        
            newQueue.remove(process)     

    #   A thread despachante escalona os processs na fila de pronto p/ as CPUs #
    Despachante.despachar(auxiliarQueue, readyQueue, cpus)

    #Atualizamos a unidade de tempo                                             #
    t += 1
    
    #Imprimimos as informações atuais                                           #
    print(f'Memória: {memory.freePages} páginas livres\n')
    
    for cpu in cpus:
        if cpu.process:
            print(f'CPU {cpu.name}: executando processo {cpu.process.id}')
        else:
            print(f'CPU {cpu.name}: vazia')
    
    print(f'\nFila de novos: ', end="")
    for n in range(len(newQueue)):
        if n != (len(newQueue)-1):
            print(f'Processo {newQueue[n].id}', end=", ")
        else:
            print(f'Processo {newQueue[n].id}', end="")
    print("\n")
    
    print(f'Fila de prontos: ', end="")
    for r in range(len(readyQueue)):
        if r != (len(readyQueue)-1):
            print(f'Processo {readyQueue[r].id}', end=", ")
        else:
            print(f'Processo {readyQueue[r].id}', end="")
    print("\n")
    
    print(f'Fila auxiliar: ', end="")
    for a in range(len(auxiliarQueue)):
        if a != (len(auxiliarQueue)-1):
            print(f'Processo {auxiliarQueue[a].id}', end=", ")
        else:
            print(f'Processo {auxiliarQueue[a].id}', end="")
    print("\n")
    
    print(f'Processos bloqueados: ', end="")
    for i in range(len(ioProcesses)):
        if i != (len(ioProcesses)-1):
            print(f'Processo {ioProcesses[i].id}', end=", ")
        else:
            print(f'Processo {ioProcesses[i].id}', end="")
    print("\n")
    
    if t == 200:
        print("-------------------------------------------------\n") 
        break

threadDespachante.join() #Espera a thread despachante terminar
threadGeradoraDeProcessos.join() #Espera a thread geradora de processos terminar
