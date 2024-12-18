
class TabelaDeProcessos():
    def __init__(self, processo, memory):
        self.memoryVector = memory.memoryVector
        self.processo = processo
        self.numberOfPages = processo.size / memory.pageSize
        self.tableVector = [] * self.numberOfPages

    #Função de Verificar se memória está cheia
        #Itera na memória e aumentar variável sentinela
    def verifyTabel(self):
        if self.memory.freePages <= self.numberOfPages:
            return True
        else:
            return False

    #Função montar tabela
    
