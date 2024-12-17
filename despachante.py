class Despachante():

    def despachar(self, auxiliarQueue, readyQueue, cpus):
        for cpu in cpus:
            if cpu.processo == None:
                if len(auxiliarQueue) > 0:
                    processo = auxiliarQueue.pop(0)
                elif len(readyQueue) > 0:
                    processo = readyQueue.pop(0)
                else:
                    break
                cpu.processo = processo
                processo.readyToRunning()

                
                    
            
