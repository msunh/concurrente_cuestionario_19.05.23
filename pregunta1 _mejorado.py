##Implemente un programa que ejecute 10 hilos que impriman un mensaje identificando al hilo, 
##luego esperen un tiempo aleatorio entre 1 y 5 segundos y luego impriman un mensaje indicando que terminaron (identificando al hilo)


import time
import threading
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def hilo():
    logging.info(f'Arranca {threading.current_thread().name}')
    time.sleep(random.randint(1,5))
    logging.info(f'Termina {threading.current_thread().name}')
    
    
#creo los diez hilos
def main():
    
    for i in range(10):
        hilo_thread = threading.Thread(target=hilo)
        #hilo_thread = threading.Thread(target=hilo, daemon=True)  #hilo demonio , cuando termina el hilo principal, terminan todos los hilos
        hilo_thread.start()
        hilo_thread.join()

       

if __name__ == '__main__':
    main()    