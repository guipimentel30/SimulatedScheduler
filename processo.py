class Processo():
    def __init__(self, id, cpuPhase1, io, cpuPhase2, size):
        self.id = id
        self.size = size
        self.state = self.states[0]

        self.cpuPhase1 = cpuPhase1
        self.io = io
        self.cpuPhase2 = cpuPhase2

        self.phase1Remaining = cpuPhase1
        self.ioRemaining = io
        self.phase2Remaining = cpuPhase2
        
    states = ["novo", "pronto", "executando", "terminado", "bloqueado"]

    def newToReady(self):
        self.state = self.states[1]
        print(f'Processo {self.id}: de novo para pronto')
              
    def readyToRunning(self):
        self.state = self.states[2]
        print(f'Processo {self.id}: de pronto para executando')


    def runningToBlocked(self):
        self.state = self.states[4]
        print(f'Processo {self.id}: de executando para bloqueado')


    def runningToReady(self):
        self.state = self.states[1]
        print(f'Processo {self.id}: de executando para pronto')

    def blockedToReady(self):
        self.state = self.states[1]
        print(f'Processo {self.id}: de bloqueado para pronto')

    
    def runningToEnd(self):
        self.state = self.states[3]
        print(f'Processo {self.id}: de executando para terminado')

    def processoRun(self):
        #Verifica em qual está
            #Subtrai o estado que esta
        #Se o processo estava em phase1 e igualou a zero
            #Bloqueia o processo
            #Coloca em Vetor de IO
        #Se o processo estava em io e igualou a zero
            #Desbloqueia o processo
                #Tira do Vetor de IO
            #Coloca em auxiliarQueue
        #Se o processo estava em phase2 e igualou a zero
            #Muda estado para terminado
