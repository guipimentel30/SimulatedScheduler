class Cpu():
    #   O método construtor recebe como parâmetro o nome da CPU.                        #
    def __init__(self, name):
        self.name = name

    process = None  #Guarda o processo alocado na CPU
    quantum = 0     #Medição utilizada para controlar a troca de processos.             #

    #   O método run executa o processo alocado na CPU e trata suas mudanças de estado. #
    def run(self, readyQueue, auxiliarQueue, ioProcesse, memory):
        #   Caso não a CPU não tenha processos alocados, abandonamos o método.          #
        if (self.process == None):
            return
        #   Caso contrário, atualizamos nosso quantum
        self.quantum += 1
        #   Chamamos o método processRun para atualizar o estado do processo            #
        processState = self.process.processRun(auxiliarQueue, ioProcesse, memory)    
        #   Tratamos a possibilidade do processo ser retirado da CPU:                   #
        if (self.quantum == 4 or processState == "block" or processState == "ended"):
            #   Caso ele saia por conta da variável quantum, mudamos seu estado para    #
            #   pronto e o anexamos na fila de processos prontos.                       #
            if ((processState != "block") and (processState != "ended")):
                self.process.runningToReady()
                readyQueue.append(self.process)
            #   Em todo caso, liberamos a CPU e reiniciamos o contador.                 #
            self.process = None
            self.quantum = 0

