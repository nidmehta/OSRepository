#Demand Paging- LRU Page Replacement

def pageFault(pages, capacity):
    s = []
    fault = 0

    for i in pages:
        if i not in s:
            if len(s) == capacity:
                s.remove(s[0])
                s.append(i)
            else:
                s.append(i)
            fault += 1
        else:
            s.remove(i)
            s.append(i)
    return fault

if __name__ == '__main__':
    pages = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
    capacity = 3
    print("Total Page Faults:", pageFault(pages, capacity))

