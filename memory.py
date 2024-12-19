from processTable import ProcessTable
from math import ceil

class Memory():
    def __init__(self, memorySize, pageSize):
        self.pageSize = pageSize
        self.memorySize = memorySize
        self.freePages = ceil(memorySize / pageSize)
        self.memoryVector = [[0*pageSize]* self.pageSize for _ in range(self.freePages)]

    # Verifica se há páginas vazias na memória #
    def verifySpace(self, process):
        numberOfPages = ceil(process.size / self.pageSize)
        if self.freePages >= numberOfPages:
            return True
        else:
            return False

    # Cria a tabela de processos e preenche a matriz de memória #

    def processAlocation(self, process):
        processSize  = process.size 
        allocatedBytes = 0
        addresses = []
        for i in range(len(self.memoryVector)):
            if (self.memoryVector[i][0] == 0):
                addresses.append(i)
                self.freePages -= 1
                for j in self.memoryVector[i]:
                    j = 1
                    allocatedBytes += 1
                    if (allocatedBytes == processSize):
                        break
            if (allocatedBytes == processSize):
                break
        
        processTable = ProcessTable(process, self.pageSize, addresses)
        return processTable

    def processDeallocation(self, process):
        for i in process.table.table:
            self.memoryVector[i] = [0*self.pageSize]* self.pageSize
            self.freePages += 1

