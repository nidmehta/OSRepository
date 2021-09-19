#Producer Consumer using Semaphores (without threads)
import threading
import time

#Global Variables
max = 5
buffer = [-1 for i in range(max)]
inIdx = 0
outIdx = 0

#Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(max)
full = threading.Semaphore(0)


#Producer
class Producer(threading.Thread):
    def run(self):
        global max, buffer, inIdx, outIdx
        global mutex, empty, full

        produced = 0
        count = 0

        while produced < 10:
            empty.acquire()
            mutex.acquire()

            count += 1
            buffer[inIdx] = count
            inIdx = (inIdx + 1) % max
            print("Producer produced: ", count)

            mutex.release()
            full.release()

            time.sleep(0.5)
            produced += 1


# Consumer
class Consumer(threading.Thread):
    def run(self):
        global max, buffer, inIdx, outIdx, count
        global mutex, empty, full

        consumed = 0

        while consumed < 10:
            full.acquire()
            mutex.acquire()

            item = buffer[outIdx]
            outIdx = (outIdx + 1) % max
            print("Consumer consumed item: ", item)

            mutex.release()
            empty.release()

            time.sleep(0.5)
            consumed += 1

if __name__ == "__main__":
    producer = Producer()
    consumer = Consumer()

    consumer.start()
    producer.start()

    # Waiting for threads to finish
    producer.join()
    consumer.join()