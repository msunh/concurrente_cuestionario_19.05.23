#Implemente un programa que tenga dos hilos A y B, los dos con acceso a una variable X (global) inicializa la variable en un valor entero 
# aleatorio (entre 1 y 100). 

#El hilo A decrementa X en 1 hasta llegar a 0 intercalando un retardo aleatorio entre 0 y 1 segundo entre cada decremento de X. 

#El hilo B hará iteraciones cada un tiempo aleatorio entre 1 y 4 segundos, imprimiendo el valor de X en cada iteración hasta que X sea 0. 

#Tanto A como B deberán imprimir mensajes al arrancar y al terminar, identificando al hilo. El hilo A deberá también indicar el valor 
# inicial de X en el mensaje de arranque o final. 

#Pregunta: Hay condiciones de carrera? Como las evitaría?

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
        #libero bloqueo
        finally:
            lock.release()
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
    thread_B = threading.Thread(target=hilo_B)
  

    thread_A.start()
    thread_B.start()
  

    thread_A.join()
    thread_B.join()

        

if __name__ == '__main__':
    main()    
