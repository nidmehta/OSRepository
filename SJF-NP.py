## Shortest Job First- Non Preemptive

def sortAt(n, array):
    for i in range(0, n):
        for j in range(i, n - i - 1):
            if array[1][j] > array[1][j + 1]:
                for k in range(0, n):
                    array[k][j], array[k][j + 1] = array[k][j + 1], array[k][j]


def WtAndTat(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i - 1]
        min = array[2][i]
        for j in range(i, n):
            if temp >= array[1][j] and min >= array[2][j]:
                min = array[2][j]
                value = j
        array[3][value] = temp + array[2][value]
        array[5][value] = array[3][value] - array[1][value]
        array[4][value] = array[5][value] - array[2][value]
        for k in range(6):
            array[k][value], array[k][i] = array[k][i], array[k][value]


def averageTime(n, array):
    wtTotal = 0
    tatTotal = 0

    sortAt(n, array)
    WtAndTat(n, array)

    print("Process ID \t Arrival Time \t Burst Time \t Completion Time \t Waiting Time \t Turn Around Time")
    for i in range(n):
        wtTotal += array[4][i]
        tatTotal += array[5][i]
        print("\t", array[0][i], " \t\t ", array[1][i], " \t\t\t ", array[2][i], "\t\t\t", array[3][i], "\t\t\t\t ", array[4][i], " \t\t\t\t ", array[5][i])

    print("Average Waiting Time: ", wtTotal / n)
    print("Average Turn Around Time: ", tatTotal / n)


if __name__ == '__main__':
    pid = [1, 2, 3, 4, 5]
    n = len(pid)

    at = [0, 1, 2, 3, 4]
    bt = [5, 10, 15, 20, 25]

    array = [[int(i) for i in range(1, n + 1)], [int(at[i]) for i in range(0, n)], [int(bt[i]) for i in range(0, n)], [0] * n, [0] * n, [0] * n]

    averageTime(n, array)
