class Processo():
    def __init__(self, id, cpuPhase1, io, cpuPhase2):
        self.id = id
        self.cpuPhase1 = cpuPhase1
        self.io = io
        self.cpuPhase2 = cpuPhase2
        self.state = self.states[0]
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
    
    def 