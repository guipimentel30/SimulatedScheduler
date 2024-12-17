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

    def readyToRunning(self):
        self.state = self.states[2]

    def runningToBlocked(self):
        self.state = self.states[4]

    def runningToReady(self):
        self.state = self.states[1]
    
    def blockedToReady(self):
        self.state = self.states[1]
    
    def runningToEnd(self):
        self.state = self.states[3]