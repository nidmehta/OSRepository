#Demand Paging- FIFO Page Replacement
from queue import Queue


def pageFault(pages, n, capacity):
    s = set()
    idx = Queue()
    fault = 0

    for i in range(n):
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])
                fault += 1
                idx.put(pages[i])
        else:
            if pages[i] not in s:
                val = idx.queue[0]
                idx.get()
                s.remove(val)
                s.add(pages[i])
                idx.put(pages[i])
                fault += 1
    return fault


if __name__ == '__main__':
    pages = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
    n = len(pages)
    capacity = 3
    print("Total Page Faults:", pageFault(pages, n, capacity))