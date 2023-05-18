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
    
    

def main():
    thread1 = threading.Thread(target=hilo)
    thread2 = threading.Thread(target=hilo)
    thread3 = threading.Thread(target=hilo)
    thread4 = threading.Thread(target=hilo)
    thread5 = threading.Thread(target=hilo)
    thread6 = threading.Thread(target=hilo)
    thread7 = threading.Thread(target=hilo)
    thread8 = threading.Thread(target=hilo)
    thread9 = threading.Thread(target=hilo)
    thread10 = threading.Thread(target=hilo)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
        

if __name__ == '__main__':
    main()    