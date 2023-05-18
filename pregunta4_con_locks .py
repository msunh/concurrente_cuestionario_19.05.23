# Modificar el programa anterior para que se ejecuten 2 hilos A y un hilo B. 
# Identificar (con comentarios) las zonas críticas y colocar los objetos necesarios para evitar condiciones de carrera.

import time
import threading
import logging
import random


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = random.randint(1,100)
lock = threading.Lock()

def hilo_A():
    global x 
    logging.info(f'Arranca hilo A {threading.current_thread().name} y el valor de x inicial es: {x}')
    
    #decrementa X en 1 hasta llegar a 0
    while x > 0:
        #adquiero el bloqueo
        try:
            lock.acquire()
            x -= 1
            print(f' resto 1, ahora el valor de x es: ', x)
        #libero bloqueo
        finally:
            lock.release()
            print(f'durmiendo por 1 segundo el decremento...')
            time.sleep(random.randint(0,1))
        
    logging.info(f'Termina hilo A {threading.current_thread().name} y el valor final de x es: {x}')
         
    
def hilo_B():
    global x 
    
    logging.info(f'Arranca Hilo B {threading.current_thread().name}')
    
    #imprimiendo el valor de X en cada iteración hasta que X sea 0
    while x > 0:
        
        #adquiero el lock
        try:
            lock.acquire()
            print(f'Imprimiendo desde B: => El valor de la variable X, es: ', x )
        #libero el lock
        finally:
            lock.release()
            #iteraciones cada un tiempo aleatorio entre 1 y 4 segundos     
            time.sleep(random.randint(1,4))
    
    logging.info(f'Termina Hilo B {threading.current_thread().name}')
    

def main():
    thread_A = threading.Thread(target=hilo_A)
    thread_A_2 = threading.Thread(target=hilo_A)
    thread_B = threading.Thread(target=hilo_B)
  

    thread_A.start()
    thread_A_2.start()
    thread_B.start()
  

    thread_A.join()
    thread_A_2.join()
    thread_B.join()

        

if __name__ == '__main__':
    main()    
