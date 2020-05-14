import threading
 
class minhaThread (threading.Thread):
    def __init__(self, threadID, nome, contador):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = nome
        self.contador = contador
    def run(self):
        print("Iniciando o trabalho %s com %d tarefas" % (self.name,self.contador))
        processo(self.nome, self.contador)
        print("Finalizando " + self.nome)
 
def processo(nome, contador):
    while contador:
        print("Trabalhador %s fazendo a tarefa %d" % (nome, contador))
        contador -= 1
 
# Criando as threads
thread1 = minhaThread(1, "Alice", 8)
thread2 = minhaThread(2, "Bob", 8)
thread3 = minhaThread(3, "Robson", 8)
thread4 = minhaThread(3, "Igor", 8)

# Comecando novas Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
 
threads = []
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
 
for t in threads:
    t.join()
 
print("Terminado Serviço")