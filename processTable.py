from math import ceil

class ProcessTable():
    #   O método construtor recebe como parâmetro um processo,                   #
    #   o tamanho da página e os índices dos páginas usadas                      #
    def __init__(self, process, pageSize, addresses):
        self.process = process  #Guarda o processo que essa tabela representa
        self.numberOfPages = ceil(process.size / pageSize)  #Guarda o número de páginas ocupadas
        self.table = addresses    #Lista de índices das páginas