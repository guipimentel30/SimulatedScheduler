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

    def processRun(self, auxiliarQueue, ioProcesses):
        #  Se a fase 1 não foi terminada:   # 
        if self.phase1Remaining != 0:
            self.phase1Remaining -= 1
            if self.phase1Remaining == 0:
                #  Se possui uma fase IO:   # 
                if self.ioRemaining != 0:
                    self.state = self.states[4]
                    ioProcesses.append(self)
                    ##  Retorna?            ## 
                #  Se não possui mais fases: #    
                elif self.phase2Remaining == 0:
                    self.state = self.states[3]
                    ##  Termina o processo  ##
                    ##  Retorna?            ## 
                    pass
        
        #  Se a fase IO não foi terminada:  # 
        elif self.ioRemaining != 0:
            self.ioRemaining -= 1
            if self.ioRemaining == 0:
                #  Se possui uma fase 2:     #
                if self.phase2Remaining != 0:
                    self.state = self.states[1]
                    ioProcesses.remove(self) #?
                    auxiliarQueue.append(self)
                    ##  Retorna?            ## 
                #  Se não possui uma fase 2: #
                else:
                    self.state = self.states[3]
                    ##  Termina o processo  ##
                    ##  Retorna?            ## 
                    pass
            
        #  Se a fase 2 não foi terminada:   #
        else:
            self.phase2Remaining -= 1
            if self.phase2Remaining == 0:
                self.state = self.states[3]
                ##  Termina o processo  ##
                ##  Retorna?            ## 
                pass
            
        #Verifica em qual estado está
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