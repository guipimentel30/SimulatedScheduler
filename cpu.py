class Cpu():
    def __init__(self, name):
        self.name = name
    
    processo = None
    quantum = 0

    def run(self, readyQueue):
        if self.processo == None:
            return
        
        self.quantum += 1
        self.processo.processoRun()    
            #ISSO DAQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII#
        if self.quantum == 4:
            self.processo.runningToReady()
            readyQueue.append(self.processo)
            self.processo = None
            self.quantum = 0

