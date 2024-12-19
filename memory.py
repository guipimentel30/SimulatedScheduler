from processTable import ProcessTable
from math import ceil

class Memory():
    #   O método construtor recebe o tamanho da memória e da página             #
    def __init__(self, memorySize, pageSize):
        self.pageSize = pageSize    #Guarda o tamanho das páginas
        self.memorySize = memorySize    #Guarda o tamanho da memória
        self.freePages = ceil(memorySize / pageSize)    #Guarda o número de páginas livres
        #   memoryVector guarda as páginas da memória, que são vetores          #
        #   de inteiros, onde 0 representa um MB livre e 1 um MB ocupado        #
        self.memoryVector = [[0*pageSize]* self.pageSize for _ in range(self.freePages)]

    #   O método verifySpace recebe um processo e retorna uma booleana que      #
    #   indica se há ou não espaço na memória para aloca-lo                     #                 
    def verifySpace(self, process):
        #   Calculamos o número de páginas necessárias para o processo          #
        numberOfPages = ceil(process.size / self.pageSize)
        #   Retornamos se o número de páginas livre comporta o processo         #          
        if self.freePages >= numberOfPages:
            return True
        else:
            return False

    #   O método processAlocation simula a alocação de um processo na memória   #
    def processAlocation(self, process):
        processSize  = process.size #Guarda  
        allocatedBytes = 0  #Guarda o número de MB alocados
        addresses = []  #Guarda o índice das páginas usadas
        #   Andamos pelo memoryVector verificando se a página está ocupada      #
        for i in range(len(self.memoryVector)):
            #   Caso a página esteja livre:                                     #
            if (self.memoryVector[i][0] == 0):
                #   Anexamos o índice da página a lista addresses               #
                addresses.append(i)
                #   Diminuimos o número de páginas livres na memória            #
                self.freePages -= 1
                #   Percorremos o vetor (página):                               # 
                for j in self.memoryVector[i]:
                    #   Simulamos um MB ocupado substituindo o 0 por 1          #
                    j = 1   
                    #   Aumentamos o número de MB alocados                      #
                    allocatedBytes += 1
                    #   Ao alocar MB equivalentes ao tamanho do processo, saimos#
                    if (allocatedBytes == processSize):
                        break
            #   Ao alocar MB equivalentes ao tamanho do processo, saimos        #
            if (allocatedBytes == processSize):
                break
        #   Geramos uma tabela do processo alocado com as informações adquiridas#
        processTable = ProcessTable(process, self.pageSize, addresses)
        #   Retornamos a tabela                                                 #
        return processTable

    #   O método processDeallocation retira processos terminados da memória     #
    def processDeallocation(self, process):
        #   Passamos pelos índices guardados na tabela do processo              #
        for i in process.table.table:
            #   Simulamos o espaço livre na memória substituindo o 1 por 0      #
            self.memoryVector[i] = [0*self.pageSize]* self.pageSize
            #   Incrementamos o número de páginas livres                        #
            self.freePages += 1

