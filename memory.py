class Memory():
    def __init__(self, memorySize, pageSize):
        self.pageSize = pageSize
        self.memorySize = memorySize
        self.freePages = memorySize / pageSize
        self.memoryVector = memorySize * [] 