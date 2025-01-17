from cpu import Cpu
from process import Process
from despachante import Despachante
from processTable import ProcessTable
from geradoraDeProcessos import GeradoraDeProcessos
from memory import Memory
import threading
import time

id = 1  #Variável que controla o identificador dos processos

t = 0   #Representa a unidade de tempo
parada = 0 #Representa quantas unidades de tempo serão representadas
alt = 0 #Representa até quando processos aleatórios devem ser gerados

pageSize = 128   #Constante do tamanho da página
memorySize = 32768   #Constante do tamanho da memória

auxiliarQueue = []   #Fila auxiliar com os processs prontos
readyQueue = []   #Fila com os processos prontos
newQueue = []   #Fila com os processos novos
ioProcesses = []   #Vetor com os processos na fase de IO
memory = Memory(memorySize, pageSize)  #Representação da memória principal
cpus = [Cpu(1), Cpu(2), Cpu(3), Cpu(4)]   #Vetor com as 4 CPUs

parada = int(input("Insira quantas unidades de tempo vocês deseja simular: "))
alt = int(input("Insira até que unidade de tempo serão gerados processos aleatórios: "))

#Eventos que controlam o fluxo de execução da thread geradora 
geradoraGo = threading.Event()
geradoraOk = threading.Event() 

#Eventos que controlam o fluxo de execução da thread despachante
despachanteGo = threading.Event()
despachanteOk = threading.Event() 

#Controla a execução do programa principal
executaPrincipal = threading.Event() 
executaPrincipal.set() 

lock = threading.Lock() 


def thread_geradora():
    global id, t, alt
    while executaPrincipal.is_set(): # Roda enquanto o programa não é encerrado pelo usuário
        geradoraGo.wait() # Espera sinal para começar sua função
        with lock: # Garante o acesso exclusivo às variáveis globais e listas, evitando condição de corrida e imprevisibilidades
            if t <= alt: # Gera processos aleatórios apenas até o tempo limite
                id = GeradoraDeProcessos.generateProcess(newQueue, id) # Gera processos aleatórios e os aloca na fila de processos novos

                #Funcionamento decente depende desse timeSleep

                time.sleep(1.5) # Espera para gerar novo processo

        geradoraOk.set() # Indica para a principal que ação foi concluída, e ela pode voltar à sua função


def thread_despachante():
    global t
    while executaPrincipal.is_set(): # Roda enquanto o programa não é encerrado pelo usuário
        despachanteGo.wait() # Garante o acesso exclusivo às variáveis globais e listas, evitando condição de corrida e imprevisibilidades
        with lock: # O lock garante que não ocorram inconsistências no acesso de leitura e escrita das variáveis globais e listas
            Despachante.despachar(auxiliarQueue, readyQueue, cpus)
        despachanteOk.set() #Indica que o despachante já concluiu sua ação


def principal():
    global t, parada, alt
    while executaPrincipal.is_set():

        geradoraGo.set() #Sinaliza que o gerador pode iniciar o próximo ciclo de criação de processos.
        geradoraOk.wait() #Principal espera o OK da geradora para continuar.
        geradoraGo.clear() #Reseta o sinal, preparando para o próximo ciclo de execução.
        geradoraOk.clear() #Reseta o sinal, preparando para o próximo ciclo de execução.

        for process in newQueue[:]:
            #   Verifica  possibilidade de alocação na memória: process.aloca(memory)  #
                if memory.verifySpace(process):
                    process.table = memory.processAlocation(process)
                    readyQueue.append(process)  # Insere o processo na fila de prontos #                                   
                    process.newToReady()    # Processo muda de estado #                                        
                    newQueue.remove(process) 

        despachanteGo.set() #Sinaliza que o despachante pode despachar os processos.
        despachanteOk.wait() #Principal espera o OK da geradora para continuar.
        despachanteGo.clear() #Reseta o sinal, preparando para o próximo ciclo de execução.
        despachanteOk.clear() #Reseta o sinal, preparando para o próximo ciclo de execução.
        
        with lock:
            print(f'-------------------- T = {t} --------------------\n') 
            print(f'Memória: {memory.freePages} páginas livres\n')
            #   Para todas as CPUs, executamos os processs alocados nelas: cpus[i].run #
            #   Executamos todos os processs na fase de IO: ioProcesses[i].processRun  #    
            for i in ioProcesses:
                i.processRun(auxiliarQueue, ioProcesses, memory)    
            for i in cpus:
                i.run(readyQueue, auxiliarQueue, ioProcesses, memory)

        #Imprimimos as informações atuais                                           #
        with lock:
            for cpu in cpus:
                if cpu.process:
                    print(f'CPU {cpu.name}: executando processo {cpu.process.id}')
                else:
                    print(f'CPU {cpu.name}: vazia')
        
        with lock:

            print(f'\nFila de novos: ', end="")
            for n in range(len(newQueue)):
                if n != (len(newQueue)-1):
                    print(f'Processo {newQueue[n].id}', end=", ")
                else:
                    print(f'Processo {newQueue[n].id}', end="")
            print("\n")
        
        with lock:
            print(f'Fila de prontos: ', end="")
            for r in range(len(readyQueue)):
                if r != (len(readyQueue)-1):
                    print(f'Processo {readyQueue[r].id}', end=", ")
                else:
                    print(f'Processo {readyQueue[r].id}', end="")
            print("\n")
        
        with lock:
            print(f'Fila auxiliar: ', end="")
            for a in range(len(auxiliarQueue)):
                if a != (len(auxiliarQueue)-1):
                    print(f'Processo {auxiliarQueue[a].id}', end=", ")
                else:
                    print(f'Processo {auxiliarQueue[a].id}', end="")
            print("\n")
        
        with lock:
            print(f'Processos bloqueados: ', end="")
            for i in range(len(ioProcesses)):
                if i != (len(ioProcesses)-1):
                    print(f'Processo {ioProcesses[i].id}', end=", ")
                else:
                    print(f'Processo {ioProcesses[i].id}', end="")
            print("\n")
        
        with lock: 
            t += 1
        
        if t > parada:
            print("-------------------------------------------------\n") 
            parada += int(input("Insira quantas unidades de tempo vocês deseja simular: "))
            print("\n")
            
        if t > parada: 
            executaPrincipal.clear() # Seta o evento para 0
            print("Finalizando programa.")
            break





threadDespachante = threading.Thread(target=thread_despachante, name="Despachante", daemon=True)
threadDespachante.start()


threadGeradora = threading.Thread(target=thread_geradora, name="Geradora", daemon=True)
threadGeradora.start()


threadPrincipal = threading.Thread(target=principal, name="Principal", daemon=False)
threadPrincipal.start()

threadDespachante.join() 
threadPrincipal.join() 
threadGeradora.join()
print("Programa encerrado.")