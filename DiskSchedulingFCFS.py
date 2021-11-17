#Disk Scheduling- FCFS


def FCFS(arr, size, head):
    seek_count = 0
    distance, current = 0, 0

    for i in range(size):
        current = arr[i]
        distance = abs(current - head)
        seek_count += distance
        head = current

    print("Total Seek Operations: ", seek_count)
    print("Seek Sequence:", end = ' ')
    for i in range(size):
        print(arr[i], end = ' ')


if __name__ == '__main__':
    arr = [98, 183, 41, 122, 14, 124, 65, 67]
    size = len(arr)
    head = 53
    FCFS(arr, size, head)