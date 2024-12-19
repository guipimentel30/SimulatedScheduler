class Process():   
    #   O método construtor:                                                    #
    def __init__(self, id, cpuPhase1, io, cpuPhase2, size):
        self.id = id    #Guarda o identificador do processo,
        self.size = size    #Guarda o tamanho do processo
        #   Todo processo é inicializado no estado novo.                        #
        self.state = self.states[0] #Guarda o estado atual do processo

        self.cpuPhase1 = cpuPhase1  #Guarda a duração da primeira fase de CPU
        self.io = io    #Guarda a duração da fase de IO
        self.cpuPhase2 = cpuPhase2  #Guarda a duração da segunda fase de CPU

        self.phase1Remaining = cpuPhase1    #Guarda quanto tempo falta para finalizar a Fase 1
        self.ioRemaining = io   #Guarda quanto tempo falta para finalizar a Fase IO
        self.phase2Remaining = cpuPhase2    #Guarda quanto tempo falta para finalizar a Fase 2
        
    table = None    #Variável que guarda o objeto processTable de um processo.
    #   Lista de possíveis estados.                                             #
    states = ["novo", "pronto", "executando", "terminado", "bloqueado"]

    #   Métodos responsáveis por apontar a mudança de estado de um processo.    #
    def newToReady(self):
        #   Atualizamos a variável de estado.                                   #
        self.state = self.states[1]
        #   Imprimimos um aviso da mudança.                                     #
        print(f'Processo {self.id}: de novo para pronto')
        #   Imprimimos o tempo restante das fases do processo.                  #
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

    #   O método processRun atualiza os valores de um processo para simular     # 
    #   a passagem de tempo. Ele recebe como parâmetro a memória,               #
    #   a fila de prontos auxiliar e a lista de processos em IO.                #
    def processRun(self, auxiliarQueue, ioProcesses, memory):
        #  Se o processo ainda está na Fase 1:                                  # 
        if self.phase1Remaining != 0:
            #   Decrementamos o tempo restante da fase.                         #
            self.phase1Remaining -= 1
            #   Caso a fase acabe:                                              #
            if self.phase1Remaining == 0:
                #   Verificamos se o processo possui fase de IO                 # 
                if self.ioRemaining != 0:
                    #   Alteramos o estado de executando para bloqueado         #
                    self.runningToBlocked()
                    #   Anexamos o processo na lista de processos em IO         #
                    ioProcesses.append(self)
                    return "block"
                #  Caso o processo não possua nem fase de IO nem fase 2:        #    
                elif self.phase2Remaining == 0:
                    #   Alteramos o estado de executando para terminado         #
                    self.runningToEnd()
                    # Chamamos um método para desalocar a memória do processo   #
                    memory.processDeallocation(self)
                    return "ended"
            #   Caso o processo ainda possua fases de CPU, seguimos.            #
            return "execute"

        #  Se o processo está na Fase IO:                                       # 
        elif self.ioRemaining != 0:
            #   Decrementamos o tempo restante da fase.                         #
            self.ioRemaining -= 1
            #   Caso a fase acabe:                                              #
            if self.ioRemaining == 0:
                #   Verificamos se o processo possui fase 2.                    # 
                if self.phase2Remaining != 0:
                    #   Alteramos o estado de bloqueado para pronto             #
                    self.blockedToReady()
                    #   Removemos o processo da lista de processos em IO        #
                    ioProcesses.remove(self)
                    #   Anexamos o processo a fila auxiliar de prontos          # 
                    auxiliarQueue.append(self)
                    return "ready"
                #  Caso o processo não possua mais fases:                       #
                else:
                    #   Alteramos o estado de bloqueado para terminado          #
                    self.blockedToEnd()
                    # Chamamos um método para desalocar a memória do processo   #
                    memory.processDeallocation(self)
                    return "ended"
            return "blocked"
            
        #  Se o processo está na Fase 2:                                        #
        else:
            #   Decrementamos o tempo restante da fase.                         #
            self.phase2Remaining -= 1
            #   Caso a fase acabe:                                              #
            if self.phase2Remaining == 0:
                #   Alteramos o estado de executando para terminado             #
                self.runningToEnd()
                # Chamamos um método para desalocar a memória do processo       #
                memory.processDeallocation(self)
                return "ended"
            #   Caso o processo ainda possua fases de CPU, seguimos.            #
            return "execute"