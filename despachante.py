class Despachante():
    #   O método despachar recebe como parâmetro a fila de prontos (com e sem prioridade) e a lista de CPUs.        #
    def despachar(auxiliarQueue, readyQueue, cpus):
        #   Para cada CPU verificamos se há um processo alocado.                                                    #
        for cpu in cpus:
            #   Se não há um processo alocado na CPU:                                                               #
            if cpu.process == None:
                #   Buscamos um processo da fila de prontos auxiliar (que contém os aqueles que estavam bloqueados) #
                if len(auxiliarQueue) > 0:
                    process = auxiliarQueue.pop(0)
                #   Caso não existam processos na fila de prontos auxiliar, buscamos na fila de prontos comum.      #
                elif len(readyQueue) > 0:
                    process = readyQueue.pop(0)
                #   Caso ambas as filas estejam vazias, finalizamos o método.                                       #
                else:
                    break
                #   Se encontramos um processo, o alocamos na CPU e trocamos seu estado para executando.            #
                cpu.process = process
                process.readyToRunning()