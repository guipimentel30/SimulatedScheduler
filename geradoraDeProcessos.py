import random
from processo import Processo

class GeradoraDeProcessos():
    id = 0

    def generateProcess(self, newQueue):
        numberOfProcesses = random.randint(1, 3)
        for i in range(0, numberOfProcesses):
            cpuPhase1 = random.randint(1, 20)
            cpuIO = random.randint(0, 15)
            cpuPhase2 = random.randint(0, 20)
            size = random.randint(128, 2048)
            processo = Processo(self.id, cpuPhase1, cpuIO, cpuPhase2, size)
            self.id += 1
            newQueue.append(processo)