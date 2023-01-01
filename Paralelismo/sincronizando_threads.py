import threading
from time import sleep

#Sincronizando Threads
ls = []

def contador1(n):
    for i in range(1, n+1):
        print(i)
        ls.append(i)
        sleep(0.4)

def contador2(n):
    for i in range(6, n+1):
        print(i)
        ls.append(i)
        sleep(0.5)

x = threading.Thread(target=contador1, args=(5,))
x.start()

y = threading.Thread(target=contador2, args=(10,))
y.start()

x.join()
y.join()

print(ls)
