class Cpu():
    def __init__(self, name):
        self.name = name
    
    process = None
    quantum = 0

    def run(self, readyQueue, auxiliarQueue, ioProcesse, memory):
        if (self.process == None):
            return
        self.quantum += 1
        processState = self.process.processRun(auxiliarQueue, ioProcesse, memory)    
        if (self.quantum == 4 or processState == "block" or processState == "ended"):
            if ((processState != "block") and (processState != "ended")):
                self.process.runningToReady()
                readyQueue.append(self.process)
            self.process = None
            self.quantum = 0

