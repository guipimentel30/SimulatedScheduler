from processo import Processo

readyQueue = []
memory = [0] * 32768 

while(True){
    
    #Geradora de Processo gera Processo
        #Tirar Dúvida com Ela
         #Escrever Arquivo com Vários Processos e escolher;
         #Gerar com randint      
         
    # Geração do descritor #
    processo = Processo(1, 2, 3, 4, 5)
    
    # Alocação #
    for i in range(0, processo.size):
        memory[i] = 1
        
    # Troca de estados #
    processo.newToReady();
    
    # Inserção na fila de prontos #
    readyQueue.append(processo);
    
    break
}