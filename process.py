class Process():                                                                                     
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
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')
        
    def readyToRunning(self):
        self.state = self.states[2]
        print(f'Processo {self.id}: de pronto para executando')
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')

    def runningToBlocked(self):
        self.state = self.states[4]
        print(f'Processo {self.id}: de executando para bloqueado')
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')

    def runningToReady(self):
        self.state = self.states[1]
        print(f'Processo {self.id}: de executando para pronto')
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')

    def blockedToReady(self):
        self.state = self.states[1]
        print(f'Processo {self.id}: de bloqueado para pronto')
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')
        
    def blockedToEnd(self):
        self.state = self.states[1]
        print(f'Processo {self.id}: de bloqueado para terminado')
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')

    def runningToEnd(self):
        self.state = self.states[3]
        print(f'Processo {self.id}: de executando para terminado')
        print(f'Fase1 = {self.phase1Remaining}\nFaseIO = {self.ioRemaining}\nFase2 = {self.phase2Remaining}')

    def processRun(self, auxiliarQueue, ioProcesses):
        #  Se a fase 1 não foi terminada:   # 
        if self.phase1Remaining != 0:
            self.phase1Remaining -= 1
            if self.phase1Remaining == 0:
                #  Se possui uma fase IO:   # 
                if self.ioRemaining != 0:
                    self.runningToBlocked()
                    ioProcesses.append(self)
                    return "block"
                    ##  Retorna?            ## 
                #  Se não possui mais fases: #    
                elif self.phase2Remaining == 0:
                    self.runningToEnd()
                    return "ended"
                    ##  Termina o process  ##
            return "execute"

        #  Se a fase IO não foi terminada:  # 
        elif self.ioRemaining != 0:
            self.ioRemaining -= 1
            if self.ioRemaining == 0:
                #  Se possui uma fase 2:     #
                if self.phase2Remaining != 0:
                    self.blockedToReady()
                    ioProcesses.remove(self) #?
                    auxiliarQueue.append(self)
                    return "execute"
                #  Se não possui uma fase 2: #
                else:
                    self.blockedToEnd()
                    ##  Termina o process  ##
                    return "ended"
            return "blocked"
        #  Se a fase 2 não foi terminada:   #
        else:
            self.phase2Remaining -= 1
            if self.phase2Remaining == 0:
                self.runningToEnd()
                return "ended"
            return "execute"
                ##  Termina o process  ##
