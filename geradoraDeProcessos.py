import random
from process import Process

class GeradoraDeProcessos():
    def generateProcess(newQueue, id):
        numberOfProcesses = random.randint(1, 3)
        for i in range(0, numberOfProcesses):
            cpuPhase1 = random.randint(1, 20)
            cpuIO = random.randint(0, 15)
            cpuPhase2 = random.randint(0, 20)
            size = random.randint(128, 2048)
            process = Process(id, cpuPhase1, cpuIO, cpuPhase2, size)
            id += 1
            newQueue.append(process)
        return id