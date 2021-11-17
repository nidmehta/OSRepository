#Disk Scheduling- SSTF
import sys

def difference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)


def findMinFromHead(diff):
    index = -1
    minimum = sys.maxsize

    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index


def SSTF(arr, head):
    if (len(arr) == 0):
        return

    l = len(arr)
    diff = [0] * l

    for i in range(l):
        diff[i] = [0, 0]

    seek_count = 0
    seek_sequence = [0] * (l + 1)

    for i in range(l):
        seek_sequence[i] = head
        difference(arr, head, diff)
        index = findMinFromHead(diff)

        diff[index][1] = True
        seek_count += diff[index][0]
        head = arr[index]

    seek_sequence[len(seek_sequence) - 1] = head

    print("Total Seek Operations: ", seek_count)
    print("Seek Sequence:", end=' ')
    for i in range(l + 1):
        print(seek_sequence[i], end=' ')


if __name__ == "__main__":
    arr = [98, 183, 41, 122, 14, 124, 65, 67]
    head = 53
    SSTF(arr, head)
