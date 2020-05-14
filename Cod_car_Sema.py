import sys
import os
import random
import time
import threading

inicioPonte = 10
larguraPonte = 20

semaCarro = threading.Semaphore(2)
lock = threading.Lock()

class Carro(threading.Thread):

  def __init__(self):
    super().__init__()
    self.posicao = 0
    self.velocidade = random.uniform(0.1, 0.5)

  def avancar(self):
    time.sleep(self.velocidade)
    self.posicao += 1

  def desenhar(self):
    print(' ' * self.posicao + "🚗")

  def run(self):
    while(True):

      if (inicioPonte-1 == self.posicao):
            semaCarro.acquire()
      
      if (30 == self.posicao):
            semaCarro.release()


      self.avancar()
      
      if (self.posicao > 33):
          self.posicao = 36

class CarroMonitor(threading.Thread):
  
  def __init__(self):
    super().__init__()
    self.posicao = 0
    self.velocidade = random.uniform(0.1, 0.5)

  def avancar2(self):
    time.sleep(self.velocidade)
    self.posicao += 1

  def desenhar2(self):
    print(' ' * self.posicao + "🚛")

  def run(self):
    while(True):

      if (inicioPonte-1 == self.posicao):
            lock.acquire()
      
      if (30 == self.posicao):
            lock.release()

      self.avancar2()
      
      if (self.posicao > 33):
          self.posicao = 36

carros = []
for i in range(6):
  v = Carro()
  carros.append(v)
  v.start()

carrosMonitor = []
for i in range(6):
  v = CarroMonitor()
  carrosMonitor.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def desenharPonte():
  print(' ' * inicioPonte + '=' * larguraPonte)

try:
    while(True):
        cls()
        print('Apertar Ctrl + C para sair...')
        print()
        desenharPonte()
        for v in carros:
            v.desenhar()
        desenharPonte()
        desenharPonte()
        for v in carrosMonitor:
            v.desenhar2()
        desenharPonte()
        time.sleep(0.10)

except KeyboardInterrupt:
    print('Interrompido')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
