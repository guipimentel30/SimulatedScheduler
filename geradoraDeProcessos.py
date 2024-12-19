import random
from process import Process

class GeradoraDeProcessos():
    #   O método generateProcess recebe como parâmetros a fila de prontos e o ID do último processo + 1#
    def generateProcess(newQueue, id):
        #   Existe uma chance de 60% do método generateProcess não gerar processos.                     #
        chance = random.randint(1, 5)
        if ((chance >= 4) or (id == 0)):
            #   O método gera de 1 a 3 processos.                                                       #
            numberOfProcesses = random.randint(1, 3)
            #   Para cada processo gerado, se cria informações aleatórias.                              #
            for i in range(0, numberOfProcesses):
                cpuPhase1 = random.randint(1, 20)
                cpuIO = random.randint(0, 15)
                cpuPhase2 = random.randint(0, 20)
                size = random.randint(128, 2048)
                #   Instânciamos um processo com as informações geradas.                                #
                process = Process(id, cpuPhase1, cpuIO, cpuPhase2, size)
                #   Atualizamos o valor de ID.                                                          #
                id += 1
                #   Anexamos o novo processo a fila de processos novos.                                #
                newQueue.append(process)
        #   Retornamos o novo valor para IDs futuros.                                                   #
        return id