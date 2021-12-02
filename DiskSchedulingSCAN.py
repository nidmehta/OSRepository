#Disk Scheduling- SCAN

def SCAN(arr, size, head, diskSize, direction):
    seek_count, distance, cur_track = 0, 0, 0
    left = []
    right = []
    seek_sequence = []

    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(diskSize - 1)

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()

    run = 2
    while run != 0:
        if direction == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
            direction = "right"

        elif direction == "right":
            for i in range(len(right)):
                cur_track = right[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track
            direction = "left"
        run -= 1

    print("Total Seek Operations: ", seek_count)
    print("Seek Sequence:", end=' ')
    for i in range(len(seek_sequence)):
        print(seek_sequence[i], end=' ')


if __name__ == '__main__':
    arr = [98, 183, 41, 122, 14, 124, 65, 67]
    size = len(arr)
    head = 53
    diskSize = 200
    direction = "right"
    SCAN(arr, size, head, diskSize, direction)
