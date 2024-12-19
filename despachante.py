class Despachante():

    def despachar(auxiliarQueue, readyQueue, cpus):
        for cpu in cpus:
            if cpu.process == None:
                if len(auxiliarQueue) > 0:
                    process = auxiliarQueue.pop(0)
                elif len(readyQueue) > 0:
                    process = readyQueue.pop(0)
                else:
                    break
                cpu.process = process
                process.readyToRunning()