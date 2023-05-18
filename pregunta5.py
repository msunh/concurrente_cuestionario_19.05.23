#Implemente un programa que pueda lanzar 10 hilos tipo A y 2 hilos tipo B, todos con acceso a una variable global X incializada en 0. 
#Los Hilos A incrementan el valor de X hasta 1000000. 
#Los Hilos B imprime el valor de X cada 2 segundos. 
#Colocar líenas de comentario en el código, identificando las zonas críticas y los objetos utilizados para evitar condiciones de carrera.

import time
import threading
import logging
import random


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

x = 0
lock = threading.Lock()

def hilo_A():
    global x 
    logging.info(f'Arranca hilo A {threading.current_thread().name} y el valor de x inicial es: {x}')
    
    #incrementa X en 1 hasta llegar a 1000000
    while x < 1000000:
        #zona crítica
        #adquiero el bloqueo
        try:
            lock.acquire()
            x += 1
            print(f' sumo 1, ahora el valor de x es: ', x)
        #libero bloqueo
        finally:
            lock.release()                        
        
    logging.info(f'Termina hilo A {threading.current_thread().name} y el valor final de x es: {x}')
         
    
def hilo_B():
    global x 
    
    logging.info(f'Arranca Hilo B {threading.current_thread().name}')
    
    #imprimiendo el valor de X cada 2 segundos
    #zona crítica
    #adquiero el lock
    try:
       lock.acquire()
       print(f'Imprimiendo desde B: => El valor de la variable X, es: ', x )
    #libero el lock
    finally:
       lock.release()
       #imprime cada dos segundos  
       time.sleep(2)
    
    logging.info(f'Termina Hilo B {threading.current_thread().name}')
    

def main():
    
    #lanzo diez hilos A
    for i in range(10):
        thread_A = threading.Thread(target=hilo_A)
        thread_A.start()
        thread_A.join()
        
    #lanzo 2 hilos B    
    for i in range (2):
        thread_B = threading.Thread(target=hilo_B)
        thread_B.start()
        thread_B.join()

        

if __name__ == '__main__':
    main()    
