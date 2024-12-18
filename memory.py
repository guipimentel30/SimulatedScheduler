from processTable import ProcessTable
class Memory():
    def __init__(self, memorySize, pageSize):
        self.pageSize = pageSize
        self.memorySize = memorySize
        self.freePages = memorySize / pageSize
        self.memoryVector = [[]* self.pageSize for _ in range(self.freePages)]


    # Verifica se há páginas vazias na memória #
    def verifySpace(self, numberOfPages):
        if self.freePages <= numberOfPages:
            return True
        else:
            return False

    # Cria a tabela de processos e preenche a matriz de memória #

    def processAlocation(self, process):
        processSize  = process.size 
        allocatedBytes = 0
        addresses = []

        for i in range(i, len(self.memoryVector)):
            if (self.memoryVector[i][0] == 0):
                addresses.append(i)
                self.freePages -= 1
                for j in i:
                    j = 1
                    allocatedBytes += 1
                    if (allocatedBytes == processSize):
                        break
            if (allocatedBytes == processSize):
                break
        
        processTable = ProcessTable(process, self.pageSize, addresses)
        return processTable


