import threading
import time

numero = 0

print('João Paulo Azevedo Baía - 20231370018')
def p1():
    global numero
    while True:
        with threading.Lock():
            numero += 1
            print('P1:', numero)
            time.sleep(1)

def p2():
    global numero
    while True:
        with threading.Lock():
            numero += 1
            print('P2:', numero)
            time.sleep(1)

t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)

t_p1.start()
t_p2.start()