# Non-Preemptive Priority Scheduling

def waitingTime(wt, n, array):
    cbt = [0] * 5
    cbt[0] = 0
    wt[0] = 0

    for i in range(1, n):
        cbt[i] = array[i - 1][1] + cbt[i - 1]
        wt[i] = cbt[i] - array[i][0] + 1

        if wt[i] < 0:
            wt[i] = 0


def turnAroundTime(tat, wt, n, array):
    for i in range(n):
        tat[i] = array[i][1] + wt[i]


def averageTime(n, array):
    wtTotal = 0
    tatTotal = 0
    wt = [0] * n
    tat = [0] * n

    waitingTime(wt, n, array)
    turnAroundTime(tat, wt, n, array)

    print("Process ID \t Arrival Time \t Burst Time \t Priority \t Waiting Time \t Turn Around Time")
    for i in range(n):
        wtTotal += wt[i]
        tatTotal += tat[i]
        print("\t", array[i][3], " \t\t ", array[i][0], " \t\t ", array[i][1], " \t\t\t ", array[i][2], " \t\t\t ", wt[i], " \t\t\t ", tat[i])

    print("Average Waiting Time: ", wtTotal / n)
    print("Average Turn Around Time: ", tatTotal / n)


if __name__ == "__main__":
    pid = [1, 2, 3, 4, 5]
    n = len(pid)

    at = [1, 2, 3, 4, 5]
    bt = [3, 5, 1, 7, 4]
    priority = [3, 4, 1, 7, 8]

    array = []
    for i in range(5):
        temp = []
        for j in range(4):
            temp.append(0)
        array.append(temp)

    for i in range(n):
        array[i][0] = at[i]
        array[i][1] = bt[i]
        array[i][2] = priority[i]
        array[i][3] = pid[i]

    array = sorted(array, key=lambda x: x[2])
    array = sorted(array)

    averageTime(n, array)