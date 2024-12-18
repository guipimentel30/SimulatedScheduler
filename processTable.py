from math import ceil

class ProcessTable():
    def __init__(self, process, pageSize, addresses):
        self.process = process
        self.numberOfPages = ceil(process.size / pageSize)
        self.table = addresses    
