# Producer Consumer using Threads
# Imports
import random
import threading
import multiprocessing
import logging
from threading import Thread
from queue import Queue

logging.basicConfig(
    format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)


# Producer- creating
def producer(queue, finished, max):
    finished.put(False)
    for x in range(max):
        v = random.randint(1, 10)
        queue.put(v)
        display(f'Producing {x}: {v}')
    finished.put(True)
    display('finished')


# Consumer- performing
def consumer(queue, finished):
    count = 0
    while True:
        if not queue.empty():
            v = queue.get()
            display(f'Consuming {count}: {v}')
            count += 1
        else:
            q = finished.get()
            if q == True:
                break
        display('finished')


def display(msg):
    threadName = threading.current_thread().name
    processName = multiprocessing.current_process().name
    logging.info(f'{processName}\{threadName}: {msg}')


if __name__ == "__main__":
    max = 10
    queue = Queue()
    finished = Queue()

    prod = Thread(target = producer, args = [queue, finished, max], daemon = True)
    cons = Thread(target = consumer, args = [queue, finished], daemon = True)

    prod.start()
    cons.start()

    prod.join()
    display('Producer has finished')

    cons.join()
    display('Consumer has finished')

    display('Finished')
